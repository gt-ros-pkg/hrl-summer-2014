#!/usr/bin/env python
#
#
#  Given a file of ROS messages published by the Bosch BMA150, this script 
#  will separate the time and each of the acceleration components and save 
#  them in separate files.
#
#

import sys

fh1 = open(sys.argv[1],"r")

beta = ""
ax = ""
ay = ""
az = ""

for line in fh1:
    if "x: " in line :
        ax = ax + line[7:-1]+'\n'
    elif "y: " in line:
        ay= ay + line[7:-1]+'\n'
    elif "z: " in line:
        az= az + line[7:-1]+'\n'
    if "seq: " in line or "secs: " in line or "nsecs: " in line:
        beta = beta + line

fh1.close()


printfile = open("accel_x","w")
for i in ax :
    printfile.write(i)
printfile.close

printfile = open("accel_y","w")
for i in ay :
    printfile.write(i)
printfile.close

printfile = open("accel_z","w")
for i in az :
    printfile.write(i)
printfile.close

printfile = open("Accel_Timing","w")
for i in beta :
    printfile.write(i)
printfile.close
