# RFSV-Shift #

Radio Frequency Scan Value Shift (RFSV-Shift): A simple program for adjusting RF scan data in a .sdb2 data-file.


I needed to import RF scan data from an RTL-SDR scanner into WWB6, but the scanner's level was way too hot (it read about 50db greater than a Shure scan). This put the entire RTL-SDR scan spectrum above the WWB exclusion threshold, making the data completely useless. This program adjusts that data to match real Shure data.

* The default shift is -50.
* An optional file path is expected as the first argument and an optional shift value as the second.
* If a file path is not provided, a file dialog will prompt selection of a scan file.

Example usage: 
```python
python rfsv_shift.py
python rfsv_shift.py "C:\Users\example\Documents\scan1.sdb2" -10
```

### Limitations ###
During calibration and comparison with scans from a Shure QLX receiver, I found -50dB to be an appropriate adjustment for the system I had available.

With only limited access to Shure scanning equipment and only a sliver of the spectrum to compare to, however, I cannot guarantee that this value will be correct for everyone. With factors like RTL-SDR gain, FFT size, different capture programs, etc., the necessary shift for any one system could vary.

Though -50 may not completely accurate, I'm confident that for most systems it would be in a range close enough to work with in WWB6 (my guess would be +/- 10 dB at the most).

With adjustment of the "Exclusion Threshold" parameter in WWB6 and refined adjustment of the shift value based on the individual system, this program should be able to make most measurements usable with WWB6.

### System Requirements ###
Python 2.7 (available [here](https://www.python.org/ftp/python/2.7.14/python-2.7.14rc1.amd64.msi) for 64-bit Windows or [here](https://www.python.org/ftp/python/2.7.14/python-2.7.14rc1.msi) for 32-bit Windows)
RTL-SDR Scanning Software capable of outputing to .sdb2 (Reccommended: [https://eartoearoak.com/software/rtlsdr-scanner](https://eartoearoak.com/software/rtlsdr-scanner))

### Contact ###
Jack McKernan ([jmcker@outlook.com](mailto:jmcker@outlook.com))
