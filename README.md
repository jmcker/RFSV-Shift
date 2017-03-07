# RFVAdjust #

RFVAdjust: A simple program for adjusting RF Scan values from a .sdb2 data-file by an arbitrary value.

### What is this repository for? ###

* I needed to import RF scan data from an RTL-SDR scanner into WWB6, but the scanner's level was way too hot (it reads about 50db greater than a Shure scan). This put the entire RTL-SDR scan spectrum above the WWB exclusion threshold, making the data completely useless. This little guy fixed that. 
* v1.0