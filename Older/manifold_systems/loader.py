#!/usr/bin/env python

import numpy as np

for beta in range(1,9):
   for gamma in range(1,11):
      master = np.array([])
      f_x = np.array([])
      f_y = np.array([])
      f_z = np.array([])
      t_x = np.array([])
      t_y = np.array([])
      t_z = np.array([])
      ad_1= "Part"+ str(beta) + "/fx_" + str(gamma)
      ad_2= "Part"+ str(beta) + "/fy_" + str(gamma)
      ad_3= "Part"+ str(beta) + "/fz_" + str(gamma)
      ad_4= "Part"+ str(beta) + "/tx_" + str(gamma)
      ad_5= "Part"+ str(beta) + "/ty_" + str(gamma)
      ad_6= "Part"+ str(beta) + "/tz_" + str(gamma)
   
      j = 0
      f = open(ad_1,'r')
      for i in f:
         f_x.resize(j+1)
         f_x[j] = i
         j = j + 1
      f.close()
      j = 0
      f = open(ad_2,'r')
      for i in f:
         f_y.resize(j+1)
         f_y[j] = i
         j = j + 1
      f.close()
      j = 0
      f = open(ad_3,'r')
      for i in f:
         f_z.resize(j+1)
         f_z[j] = i
         j = j + 1
      f.close()
      j = 0
      f = open(ad_4,'r')
      for i in f:
         t_x.resize(j+1)
         t_x[j] = i
         j = j + 1
      f.close()
      j = 0
      f = open(ad_5,'r')
      for i in f:
         t_y.resize(j+1)
         t_y[j] = i
         j = j + 1
      f.close()
      j = 0
      f = open(ad_6,'r')
      for i in f:
         t_z.resize(j+1)
         t_z[j] = i
         j = j + 1
      f.close()


      for i in range(0,len(f_x)):
         master.resize(i+1,7)
         master[i][0] = f_x[i]
         master[i][1] = f_y[i]
         master[i][2] = f_z[i]
         master[i][3] = t_x[i]
         master[i][4] = t_y[i]
         master[i][5] = t_z[i]
         master[i][6] = beta
      reality = master.transpose()

      s1 = "T" + str(beta) + "_1"
      s2 = "T" + str(beta) + "_2"
      s3 = "T" + str(beta) + "_3"
      s4 = "T" + str(beta) + "_4"
      s5 = "T" + str(beta) + "_5"
      s6 = "T" + str(beta) + "_6"
      s7 = "T" + str(beta) + "_7"
      s8 = "T" + str(beta) + "_8"
      s9 = "T" + str(beta) + "_9" 
      s10 = "T" + str(beta) + "_10"

      print beta,"_",gamma,":",reality.shape

      if gamma == 1:
         f = open(s1, 'w')
         np.save(f,reality)
         f.close()
      elif gamma == 2:
         f = open(s2, 'w')
         np.save(f,reality)
         f.close()
      elif gamma == 3:
         f = open(s3, 'w')
         np.save(f,reality)
         f.close()
      elif gamma == 4:
         f = open(s4, 'w')
         np.save(f,reality)
         f.close()
      elif gamma == 5:
         f = open(s5, 'w')
         np.save(f,reality)
         f.close()
      elif gamma == 6:
         f = open(s6, 'w')
         np.save(f,reality)
         f.close()
      elif gamma == 7:
         f = open(s7, 'w')
         np.save(f,reality)
         f.close()
      elif gamma == 8:
         f = open(s8, 'w')
         np.save(f,reality)
         f.close()
      elif gamma == 9:
         f = open(s9, 'w')
         np.save(f,reality)
         f.close()
      elif gamma == 10:
         f = open(s10, 'w')
         np.save(f,reality)
         f.close()
