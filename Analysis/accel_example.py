#!/usr/bin/env python 
#
#
#   Given files containing the already scanned accelerometer and timing information
#   from the ROS messages published by the Bosch BMA150, this script converts these 
#   files into vectors for the time and x, y, and z components of acceleration, finds
#   the magnitude of the acceleration applies a simple moving averager, and plots 
#   the acceleration components.
#
#

import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt
import pylab
from collections import deque
import math

window=100 #window size of the moving averager

fax=open("accel_x","r")
fay=open("accel_y", "r")
faz=open("accel_z", "r")
ftt=open("Accel_Timing", "r")


ax=deque([])
ay=deque([])
az=deque([])
t=deque([])
tn=deque([])

for line in fax:
    ax.append(float(line))
fax.close()

for line in fay:
    ay.append(float(line))
fay.close()

for line in faz:
    az.append(float(line))
faz.close()        

for line in ftt:
    if " secs: " in line:
        t.append(float(line[10:-1]))    
    if "nsecs: " in line:
        tn.append(float(line[11:-1]))
ftt.close()

ax=np.array(ax)
ay=np.array(ay)
az=np.array(az)
tn=np.array(tn)*10**-9  #convert nanoseconds into seconds
t=np.array(t)+tn        #add array of seconds to corresponding array of nanoseconds

amag=deque([])
index=range(0, len(ax))

for i in index:
    amag.append(math.sqrt(ax[i]**2+ay[i]**2+az[i]**2)) #finds magnitude of acceleration

def movingaverage (values, window):          #takes moving average of a vector with a given window size
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'valid')
    return sma

amag_shrink=movingaverage(amag,3)
ax_shrink=movingaverage(ax, 3)    
ay_shrink=movingaverage(ay, 3)
az_shrink=movingaverage(az, 3)

amag_smooth=movingaverage(amag_shrink, window)
ax_smooth=movingaverage(ax_shrink, window)
ay_smooth=movingaverage(ay_shrink, window)
az_smooth=movingaverage(az_shrink, window)


index= np.around(np.linspace(0, len(ax_smooth), len(t), endpoint=False)) 
index=np.int_(index)  #create vector of evenly spaced integers with which the accelerometer data can be indexed 
                      #due there being 3 samples per time-stamped ROS message on average


plt.figure(1)
plt.subplot(311)
plt.plot(t, ax_smooth[index], 'r') 


plt.subplot(312)
plt.plot(t, ay_smooth[index], 'g')


plt.subplot(313)
plt.plot(t, az_smooth[index], 'b')
plt.show()


