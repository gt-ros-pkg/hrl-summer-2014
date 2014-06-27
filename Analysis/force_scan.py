#!/usr/bin/env python
#
#
#  Given a file of ROS messages published by the ATI Mini-45 Force-Torque
#  sensor, this script will separate the time and each of the force and 
#  torque components and save them in separate files.
#
#

import sys
searchfile = open(sys.argv[1],"r")

storage = ""
beta = ""
fx = ""
fy = ""
fz = ""
tx = ""
ty = ""
tz = ""
ft=""

for line in searchfile:
    if "force: " in line:
        ft="f"   
    elif "torque: " in line:
        ft="t"
    elif ft=="f":   
        if "x: " in line :
            fx = fx + line[7:-1]+'\n'
        elif "y: " in line:
            fy= fy + line[7:-1]+'\n'
        elif "z: " in line:
            fz= fz + line[7:-1]+'\n'
    elif ft=="t":    
        if "x: " in line:
            tx= tx+ line[7:-1]+'\n'
        elif "y: " in line:
            ty=ty +line[7:-1]+'\n'  
        elif "z: " in line:
            tz=tz+line[7:-1]+'\n'
    
    if "seq: " in line or "secs: " in line or "nsecs: " in line:
        beta = beta + line

searchfile.close()


printfile = open("force_x","w")
for i in fx :
    printfile.write(i)
printfile.close

printfile = open("force_y","w")
for i in fy :
    printfile.write(i)
printfile.close

printfile = open("force_z","w")
for i in fz :
    printfile.write(i)
printfile.close

printfile = open("torque_x","w")
for i in tx :
    printfile.write(i)
printfile.close

printfile = open("torque_y","w")
for i in ty :
    printfile.write(i)
printfile.close

printfile = open("torque_z","w")
for i in tz :
    printfile.write(i)
printfile.close

printfile = open("Force_Timing","w")
for i in beta :
    printfile.write(i)
printfile.close


