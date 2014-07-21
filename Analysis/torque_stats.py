#! /usr/bin/env python
from __future__ import division
from collections import deque
import scipy
from scipy import stats
import sys
import numpy as np
import math

num=input("Enter Trial Number: ")
filemag0=open("Trial%s_tmag_part0"%num, "r")  #open files containing torque magnitude data
filemag1=open("Trial%s_tmag_part1"%num, "r")  #for each part of the trial
filemag2=open("Trial%s_tmag_part2"%num, "r")
filemag3=open("Trial%s_tmag_part3"%num, "r")
filemag4=open("Trial%s_tmag_part4"%num, "r")
filemag5=open("Trial%s_tmag_part5"%num, "r")
filemag6=open("Trial%s_tmag_part6"%num, "r")
filemag7=open("Trial%s_tmag_part7"%num, "r")
filemag8=open("Trial%s_tmag_part8"%num, "r")
filemag9=open("Trial%s_tmag_part9"%num, "r")
filemag10=open("Trial%s_tmag_part10"%num, "r")
filemag11=open("Trial%s_tmag_part11"%num, "r")

tmag0=deque([])  #initialize deques for each part of trial
tmag1=deque([])
tmag2=deque([])
tmag3=deque([])
tmag4=deque([])
tmag5=deque([])
tmag6=deque([])
tmag7=deque([])
tmag8=deque([])
tmag9=deque([])
tmag10=deque([])
tmag11=deque([])

for line in filemag0:     #get data from files and add them to deques
    tmag0.append(float(line))
filemag0.close

for line in filemag1:
    tmag1.append(float(line))
filemag1.close

for line in filemag2:
    tmag2.append(float(line))
filemag2.close

for line in filemag3:
    tmag3.append(float(line))
filemag3.close

for line in filemag4:
    tmag4.append(float(line))
filemag4.close

for line in filemag5:
    tmag5.append(float(line))
filemag5.close

for line in filemag6:
    tmag6.append(float(line))
filemag6.close

for line in filemag7:
    tmag7.append(float(line))
filemag7.close

for line in filemag8:
    tmag8.append(float(line))
filemag8.close

for line in filemag9:
    tmag9.append(float(line))
filemag9.close

for line in filemag10:
    tmag10.append(float(line))
filemag10.close

for line in filemag11:
    tmag11.append(float(line))
filemag11.close

size0, minmax0, amean0, var0, skew0, kurt0=stats.describe(np.array(tmag0))  #get min, max, mean, variance, 
size1, minmax1, amean1, var1, skew1, kurt1=stats.describe(np.array(tmag1))  #skew, and kurtosis data for torque
size2, minmax2, amean2, var2, skew2, kurt2=stats.describe(np.array(tmag2))  #magnitude for each part of the trial
size3, minmax3, amean3, var3, skew3, kurt3=stats.describe(np.array(tmag3))
size4, minmax4, amean4, var4, skew4, kurt4=stats.describe(np.array(tmag4))
size5, minmax5, amean5, var5, skew5, kurt5=stats.describe(np.array(tmag5))
size6, minmax6, amean6, var6, skew6, kurt6=stats.describe(np.array(tmag6))
size7, minmax7, amean7, var7, skew7, kurt7=stats.describe(np.array(tmag7))
size8, minmax8, amean8, var8, skew8, kurt8=stats.describe(np.array(tmag8))
size9, minmax9, amean9, var9, skew9, kurt9=stats.describe(np.array(tmag9))
size10, minmax10, amean10, var10, skew10, kurt10=stats.describe(np.array(tmag10))
size11, minmax11, amean11, var11, skew11, kurt11=stats.describe(np.array(tmag11))

printfile = open('Trial%s_amag_stats'%num,"w")  #write this data to a file
printfile.write("Part 0:\n")
printfile.write("Size: "+ str(size0)+'\n')
printfile.write("Min: "+ str(minmax0[0]) + '\n')
printfile.write("Max: " + str(minmax0[1]) +'\n')
printfile.write("Mean: " +str(amean0) +'\n')
printfile.write("Variance: " + str(var0) + '\n')
printfile.write("Skewness: " + str(skew0) +'\n')
printfile.write("Kurtosis: " +str(kurt0) +'\n\n')

printfile.write("Part 1:\n")
printfile.write("Size: "+ str(size1)+'\n')
printfile.write("Min: "+ str(minmax1[0]) + '\n')
printfile.write("Max: " + str(minmax1[1]) +'\n')
printfile.write("Mean: " +str(amean1) +'\n')
printfile.write("Variance: " + str(var1) + '\n')
printfile.write("Skewness: " + str(skew1) +'\n')
printfile.write("Kurtosis: " +str(kurt1) +'\n\n')

printfile.write("Part 2:\n")
printfile.write("Size: "+ str(size2)+'\n')
printfile.write("Min: "+ str(minmax2[0]) + '\n')
printfile.write("Max: " + str(minmax2[1]) +'\n')
printfile.write("Mean: " +str(amean2) +'\n')
printfile.write("Variance: " + str(var2) + '\n')
printfile.write("Skewness: " + str(skew2) +'\n')
printfile.write("Kurtosis: " +str(kurt2) +'\n\n')

printfile.write("Part 3:\n")
printfile.write("Size: "+ str(size3)+'\n')
printfile.write("Min: "+ str(minmax3[0]) + '\n')
printfile.write("Max: " + str(minmax3[1]) +'\n')
printfile.write("Mean: " +str(amean3) +'\n')
printfile.write("Variance: " + str(var3) + '\n')
printfile.write("Skewness: " + str(skew3) +'\n')
printfile.write("Kurtosis: " +str(kurt3) +'\n\n')

printfile.write("Part 4:\n")
printfile.write("Size: "+ str(size4)+'\n')
printfile.write("Min: "+ str(minmax4[0]) + '\n')
printfile.write("Max: " + str(minmax4[1]) +'\n')
printfile.write("Mean: " +str(amean4) +'\n')
printfile.write("Variance: " + str(var4) + '\n')
printfile.write("Skewness: " + str(skew4) +'\n')
printfile.write("Kurtosis: " +str(kurt4) +'\n\n')

printfile.write("Part 5:\n")
printfile.write("Size: "+ str(size5)+'\n')
printfile.write("Min: "+ str(minmax5[0]) + '\n')
printfile.write("Max: " + str(minmax5[1]) +'\n')
printfile.write("Mean: " +str(amean5) +'\n')
printfile.write("Variance: " + str(var5) + '\n')
printfile.write("Skewness: " + str(skew5) +'\n')
printfile.write("Kurtosis: " +str(kurt5) +'\n\n')

printfile.write("Part 6:\n")
printfile.write("Size: "+ str(size6)+'\n')
printfile.write("Min: "+ str(minmax6[0]) + '\n')
printfile.write("Max: " + str(minmax6[1]) +'\n')
printfile.write("Mean: " +str(amean6) +'\n')
printfile.write("Variance: " + str(var6) + '\n')
printfile.write("Skewness: " + str(skew6) +'\n')
printfile.write("Kurtosis: " +str(kurt6) +'\n\n')

printfile.write("Part 7:\n")
printfile.write("Size: "+ str(size7)+'\n')
printfile.write("Min: "+ str(minmax7[0]) + '\n')
printfile.write("Max: " + str(minmax7[1]) +'\n')
printfile.write("Mean: " +str(amean7) +'\n')
printfile.write("Variance: " + str(var7) + '\n')
printfile.write("Skewness: " + str(skew7) +'\n')
printfile.write("Kurtosis: " +str(kurt7) +'\n\n')

printfile.write("Part 8:\n")
printfile.write("Size: "+ str(size8)+'\n')
printfile.write("Min: "+ str(minmax8[0]) + '\n')
printfile.write("Max: " + str(minmax8[1]) +'\n')
printfile.write("Mean: " +str(amean8) +'\n')
printfile.write("Variance: " + str(var8) + '\n')
printfile.write("Skewness: " + str(skew8) +'\n')
printfile.write("Kurtosis: " +str(kurt8) +'\n\n')

printfile.write("Part 9:\n")
printfile.write("Size: "+ str(size9)+'\n')
printfile.write("Min: "+ str(minmax9[0]) + '\n')
printfile.write("Max: " + str(minmax9[1]) +'\n')
printfile.write("Mean: " +str(amean9) +'\n')
printfile.write("Variance: " + str(var9) + '\n')
printfile.write("Skewness: " + str(skew9) +'\n')
printfile.write("Kurtosis: " +str(kurt9) +'\n\n')

printfile.write("Part 10:\n")
printfile.write("Size: "+ str(size10)+'\n')
printfile.write("Min: "+ str(minmax10[0]) + '\n')
printfile.write("Max: " + str(minmax10[1]) +'\n')
printfile.write("Mean: " +str(amean10) +'\n')
printfile.write("Variance: " + str(var10) + '\n')
printfile.write("Skewness: " + str(skew10) +'\n')
printfile.write("Kurtosis: " +str(kurt10) +'\n\n')

printfile.write("Part 11:\n")
printfile.write("Size: "+ str(size11)+'\n')
printfile.write("Min: "+ str(minmax11[0]) + '\n')
printfile.write("Max: " + str(minmax11[1]) +'\n')
printfile.write("Mean: " +str(amean11) +'\n')
printfile.write("Variance: " + str(var11) + '\n')
printfile.write("Skewness: " + str(skew10) +'\n')
printfile.write("Kurtosis: " +str(kurt11) +'\n\n')

printfile.close
