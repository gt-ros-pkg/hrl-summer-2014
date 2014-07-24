#!/usr/bin/env python

import numpy as np

for beta in range(1,12): # Part Numbers (1, n+1)
   for gamma in range(1,21): # Trial Numbers (1, n+1) !~~: 21->30 will likely be faulty states (true positive testing) (need to treat seperately, isolate error points)
      master = np.array([])
      fmag = np.array([])
      tmag = np.array([])
      amag= np.array([])
      ad_1= "./Trial/Trial"+ str(gamma) + "_fmag_part" + str(beta)
      ad_2= "./Trial/Trial"+ str(gamma) + "_tmag_part" + str(beta)
      ad_3= "./Trial/Trial"+ str(gamma) + "_amag_part" + str(beta)
      j = 0
      f = open(ad_1,'r')
      for i in f:
         fmag.resize(j+1)
         fmag[j] = i
         j = j + 1
      f.close()
      j = 0
      f = open(ad_2,'r')
      for i in f:
         tmag.resize(j+1)
         tmag[j] = i
         j = j + 1
      f.close()
      j = 0
      f = open(ad_3,'r')
      for i in f:
         amag.resize(j+1)
         amag[j] = i
         j = j + 1
      f.close()

      length_value = np.min((len(fmag),len(tmag),len(amag)))

      for i in range(0,length_value):
         master.resize(i+1,4)
         master[i][0] = fmag[i]
         master[i][1] = tmag[i]
         master[i][2] = amag[i]
	 master[i][3] = beta

      write_out = "./Sequence/T" + str(beta) + "_" + str(gamma)
      print beta,"_",gamma,":",master.shape

      f = open(write_out, 'w')
      np.save(f,master)
      f.close()
   for gamma in range(21,29): # Trial Numbers (1, n+1) !~~: 21->30 will likely be faulty states (true positive testing) (need to treat seperately, isolate error points)
      master = np.array([])
      fmag = np.array([])
      tmag = np.array([])
      amag = np.array([])
      ad_1= "./Trial/Trial"+ str(gamma) + "_fmag_part" + str(beta)
      ad_2= "./Trial/Trial"+ str(gamma) + "_tmag_part" + str(beta)
      ad_3= "./Trial/Trial"+ str(gamma) + "_amag_part" + str(beta)
      j = 0
      f = open(ad_1,'r')
      for i in f:
         fmag.resize(j+1)
         fmag[j] = i
         j = j + 1
      f.close()
      j = 0
      f = open(ad_2,'r')
      for i in f:
         tmag.resize(j+1)
         tmag[j] = i
         j = j + 1
      f.close()
      j = 0
      f = open(ad_3,'r')
      for i in f:
         amag.resize(j+1)
         amag[j] = i
         j = j + 1
      f.close()

      length_value = np.min((len(fmag),len(tmag),len(amag)))

      for i in range(0,length_value):
         master.resize(i+1,4)
         master[i][0] = fmag[i]
         master[i][1] = tmag[i]
         master[i][2] = amag[i]
         master[i][3] = beta

      write_out = "./Sequence/E" + str(beta) + "_" + str(gamma-20)
      print beta,"_",gamma,":",master.shape

      f = open(write_out, 'w')
      np.save(f,master)
      f.close()
