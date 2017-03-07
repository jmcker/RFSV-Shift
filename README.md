# RFSV-Shift #

Radio Frequency Scan Value Shift (RFSV-Shift): A simple program for shifting RF Scan values from a .sdb2 data-file by an arbitrary value.

### What is this repository for? ###

* I needed to import RF scan data from an RTL-SDR scanner into WWB6, but the scanner's level was way too hot (it reads about 50db greater than a Shure scan). This put the entire RTL-SDR scan spectrum above the WWB exclusion threshold, making the data completely useless. This little guy fixes that. 
* v1.0

* The default shift is -50.
* It expects a file path as the first argument and an optional shift value as the second.

Example: 
```
#!python

python rfsv_shift C:\Users\example\Documents\scan1.sdb2 -10
```