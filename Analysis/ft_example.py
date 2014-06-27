#!/usr/bin/env python 
#
#
#  Given files containing the already scanned force/torque and timing information
#  from the ROS messages published by the ATI Mini-45 Force Torque Sensor, this 
#  script converts these files into vectors for the forces, torques, and times, 
#  calculates the magnitude of the force and moment vectors, smooths them with a 
#  moving averager, and plots them. 
#
#
import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt
import pylab
from collections import deque
import math

window=100 #window size of the moving averager

ffx=open("force_x","r")
ffy=open("force_y", "r")
ffz=open("force_z", "r")
ftx=open("torque_x", "r")
fty=open("torque_y", "r")
ftz=open("torque_z", "r")
ftt=open("Force_Timing", "r")


fx=deque([])
fy=deque([])
fz=deque([])
tx=deque([])
ty=deque([])
tz=deque([])
t=deque([])
tn=deque([])

for line in ffx:
    fx.append(float(line))
ffx.close()

for line in ffy:
    fy.append(float(line))
ffy.close()

for line in ffz:
    fz.append(float(line))
ffz.close()        

for line in ftx:
    tx.append(float(line))
ftx.close()

for line in fty:
    ty.append(float(line))
fty.close()     

for line in ftz:
    tz.append(float(line))
ftz.close()

for line in ftt:
    if " secs: " in line:
        t.append(float(line[10:-1]))    
    if "nsecs: " in line:
        tn.append(float(line[11:-1]))
ftt.close()

fx=np.array(fx)
fy=np.array(fy)
fz=np.array(fz)
tx=np.array(tx)
ty=np.array(ty)
tn=np.array(tn)*10**-9   #convert nanoseconds into seconds
t=np.array(t)+tn         #add array of seconds to corresponding array of nanoseconds

fmag=deque([])
tmag=deque([])
index=range(0, len(fx))

for i in index:
    fmag.append(math.sqrt(fx[i]**2+fy[i]**2+fz[i]**2))  #calculate magnitude of force vectors
for i in index:
    tmag.append(math.sqrt(tx[i]**2+ty[i]**2+tz[i]**2))  #calculate magnitude of moment vectors

def movingaverage (values, window):             #takes moving average of a vector with a given window size
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'valid')
    return sma

fmag=np.array(fmag)
tmag=np.array(tmag)
tmag_smooth=movingaverage(tmag, window)
fmag_smooth=movingaverage(fmag, window)
fx_smooth=movingaverage(fx, window)
fy_smooth=movingaverage(fy, window)
fz_smooth=movingaverage(fz, window)
tx_smooth=movingaverage(tx, window)
ty_smooth=movingaverage(ty, window)
tz_smooth=movingaverage(tz, window)


plt.figure(1)                            
plt.subplot(311)
plt.plot(t[0:len(fx_smooth)], fx_smooth, 'r')

plt.subplot(312)
plt.plot(t[0:len(fy_smooth)], fy_smooth, 'g')


plt.subplot(313)
plt.plot(t[0:len(fz_smooth)], fz_smooth, 'b')
plt.show()





