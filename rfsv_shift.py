import os
import sys
from Tkinter import Tk
from tkFileDialog import askopenfilename

global ADJUST_LEVEL
ADJUST_LEVEL = -50

def main(args):
    global ADJUST_LEVEL

    print
    print "----------------------------------------------------------------"
    print "          RF Scan Adjustment for Shure WWB6 Import"
    print "----------------------------------------------------------------"
    print

    if (len(args) < 1):
        args = [getUserFilepath()]
    elif len(args) > 1:
        ADJUST_LEVEL = args[1]
    
    fullFilepath = os.path.normpath(args[0])
    folder = os.path.split(fullFilepath)[0]
    filename = os.path.split(fullFilepath)[1]
    ext = os.path.splitext(filename)[1]
    try:
        if fullFilepath == ".":
            exit()
        if ext.lower() != ".sdb2":
            raise IOError("Invalid file extension")
    except IOError, e:
        errorPrint("Input file could not be opened. Please ensure the file exists and is of the proper type.", e)

    print
    print "Selected scan file: ", filename
    print "Adjustment: ", ADJUST_LEVEL, "dB"

    newFilename = "Adjusted_" + str(ADJUST_LEVEL) + "_" + filename
    newFullFilepath = os.path.join(folder, newFilename)
    if os.path.exists(newFullFilepath):
        print
        print "The file: " + newFullFilepath + " already exists."
        while True:
            print "Would you like to overwrite?"
            print "(Y / N): ",
            ans = raw_input()
            if ans.upper() == "Y":
                break
            elif ans.upper() == "N":
                errorPrint("Failed to write output. File already exists.")
            else:
                print
                print ans + " is not a valid option. Please try again."
                print
    
    with open(newFullFilepath, 'w') as adjFile:
        with open(fullFilepath, 'r') as origFile:
            for line in origFile:
                if "<v>" in line:
                    val = float(line[line.index("<v>") + 3 : line.index("</v>")])
                    adjVal = val + ADJUST_LEVEL
                    line = "			<v>" + str(adjVal) + "</v>\n"
                adjFile.write(line)

    print
    print
    print "Saved to: ", newFullFilepath
    print
    print "Press ENTER to continue..."
    raw_input()
    exit()

def errorPrint(message, standardErr = ""):
    print "\n\n"
    print message
    if standardErr:
        print "Error message: ", standardErr
    print
    print "Press ENTER to exit..."
    raw_input()
    exit()

def getUserFilepath():
    Tk().withdraw() # Prevents full GUI
    filetypes = [('all files', '.*'), ('Shure WWB DB Files', '.sdb2')]
    filepath = askopenfilename(filetypes = filetypes, multiple = False, title = "Select the RF Scan file to be adjusted...")
    return filepath

if __name__ == "__main__":
    main(sys.argv[1:])
