#!/usr/bin/env python

import numpy as np
import cPickle as pickle

class tacitus:
    def info(self):
        print "If you have any questions, don't hesitate to ask Caleb."
        print "This core contains formated data for use in the multimodal system"
        print "The following formated data sets exist:"
        print "self.pX_Y   <-> contains raw data for each step. X is the step, Y is the trial"
        print "self.ss_X   <-> contains formatted (compressed) data for each step. X is the step"
        print "self.ts     <-> contains a complete training set for all trials. Does not contain tags."
        print "self.tsw    <-> contains the tags for the aforementioned self.ts"
        print "self.cv_X_Y <-> contains cross validation formated data. X = 19 implies 1->9, X = 21 implies 2->10. Y indicates the related state."
        print "self.cv_X_Yx<-> contains the remaining vector for cross validation. X and Y are the same as above."
        print "self.cv_X_Yw<-> contains the tags for the cross validation sets. X and Y are the same as above."
	print "self.cv_X   <-> contains a training set for cross validation."
	print "self.cv_Xw  <-> contains tag data for the training set for cross validation."
        print "Please note: due to adaptability, some of these sets may have a null column at the end."
        print "Otherwise, formatted sets have the following shape (some may lack element [6])"
        print "[0] -> Force X"
        print "[1] -> Force Y"
        print "[2] -> Force Z"
        print "[3] -> Torque X"
        print "[4] -> Torque Y"
        print "[5] -> Torque Z"
        print "[6] -> State tag"

    def init(self):
        print "Loading Base Data..."
        f = open('T1_1','r')
        self.p1_1 = np.load(f)
        f.close()
        f = open('T1_2','r')
        self.p1_2 = np.load(f)
        f.close()
        f = open('T1_3','r')
        self.p1_3 = np.load(f)
        f.close()
        f = open('T1_4','r')
        self.p1_4 = np.load(f)
        f.close()
        f = open('T1_5','r')
        self.p1_5 = np.load(f)
        f.close()
        f = open('T1_6','r')
        self.p1_6 = np.load(f)
        f.close()
        f = open('T1_7','r')
        self.p1_7 = np.load(f)
        f.close()
        f = open('T1_8','r')
        self.p1_8 = np.load(f)
        f.close()
        f = open('T1_9','r')
        self.p1_9 = np.load(f)
        f.close()
        f = open('T1_10','r')
        self.p1_10 = np.load(f)
        f.close()

        f = open('T2_1','r')
        self.p2_1 = np.load(f)
        f.close()
        f = open('T2_2','r')
        self.p2_2 = np.load(f)
        f.close()
        f = open('T2_3','r')
        self.p2_3 = np.load(f)
        f.close()
        f = open('T2_4','r')
        self.p2_4 = np.load(f)
        f.close()
        f = open('T2_5','r')
        self.p2_5 = np.load(f)
        f.close()
        f = open('T2_6','r')
        self.p2_6 = np.load(f)
        f.close()
        f = open('T2_7','r')
        self.p2_7 = np.load(f)
        f.close()
        f = open('T2_8','r')
        self.p2_8 = np.load(f)
        f.close()
        f = open('T2_9','r')
        self.p2_9 = np.load(f)
        f.close()
        f = open('T2_10','r')
        self.p2_10 = np.load(f)
        f.close()

        f = open('T3_1','r')
        self.p3_1 = np.load(f)
        f.close()
        f = open('T3_2','r')
        self.p3_2 = np.load(f)
        f.close()
        f = open('T3_3','r')
        self.p3_3 = np.load(f)
        f.close()
        f = open('T3_4','r')
        self.p3_4 = np.load(f)
        f.close()
        f = open('T3_5','r')
        self.p3_5 = np.load(f)
        f.close()
        f = open('T3_6','r')
        self.p3_6 = np.load(f)
        f.close()
        f = open('T3_7','r')
        self.p3_7 = np.load(f)
        f.close()
        f = open('T3_8','r')
        self.p3_8 = np.load(f)
        f.close()
        f = open('T3_9','r')
        self.p3_9 = np.load(f)
        f.close()
        f = open('T3_10','r')
        self.p3_10 = np.load(f)
        f.close()

        f = open('T4_1','r')
        self.p4_1 = np.load(f)
        f.close()
        f = open('T4_2','r')
        self.p4_2 = np.load(f)
        f.close()
        f = open('T4_3','r')
        self.p4_3 = np.load(f)
        f.close()
        f = open('T4_4','r')
        self.p4_4 = np.load(f)
        f.close()
        f = open('T4_5','r')
        self.p4_5 = np.load(f)
        f.close()
        f = open('T4_6','r')
        self.p4_6 = np.load(f)
        f.close()
        f = open('T4_7','r')
        self.p4_7 = np.load(f)
        f.close()
        f = open('T4_8','r')
        self.p4_8 = np.load(f)
        f.close()
        f = open('T4_9','r')
        self.p4_9 = np.load(f)
        f.close()
        f = open('T4_10','r')
        self.p4_10 = np.load(f)
        f.close()

        f = open('T5_1','r')
        self.p5_1 = np.load(f)
        f.close()
        f = open('T5_2','r')
        self.p5_2 = np.load(f)
        f.close()
        f = open('T5_3','r')
        self.p5_3 = np.load(f)
        f.close()
        f = open('T5_4','r')
        self.p5_4 = np.load(f)
        f.close()
        f = open('T5_5','r')
        self.p5_5 = np.load(f)
        f.close()
        f = open('T5_6','r')
        self.p5_6 = np.load(f)
        f.close()
        f = open('T5_7','r')
        self.p5_7 = np.load(f)
        f.close()
        f = open('T5_8','r')
        self.p5_8 = np.load(f)
        f.close()
        f = open('T5_9','r')
        self.p5_9 = np.load(f)
        f.close()
        f = open('T5_10','r')
        self.p5_10 = np.load(f)
        f.close()

        f = open('T6_1','r')
        self.p6_1 = np.load(f)
        f.close()
        f = open('T6_2','r')
        self.p6_2 = np.load(f)
        f.close()
        f = open('T6_3','r')
        self.p6_3 = np.load(f)
        f.close()
        f = open('T6_4','r')
        self.p6_4 = np.load(f)
        f.close()
        f = open('T6_5','r')
        self.p6_5 = np.load(f)
        f.close()
        f = open('T6_6','r')
        self.p6_6 = np.load(f)
        f.close()
        f = open('T6_7','r')
        self.p6_7 = np.load(f)
        f.close()
        f = open('T6_8','r')
        self.p6_8 = np.load(f)
        f.close()
        f = open('T6_9','r')
        self.p6_9 = np.load(f)
        f.close()
        f = open('T6_10','r')
        self.p6_10 = np.load(f)
        f.close()

        f = open('T7_1','r')
        self.p7_1 = np.load(f)
        f.close()
        f = open('T7_2','r')
        self.p7_2 = np.load(f)
        f.close()
        f = open('T7_3','r')
        self.p7_3 = np.load(f)
        f.close()
        f = open('T7_4','r')
        self.p7_4 = np.load(f)
        f.close()
        f = open('T7_5','r')
        self.p7_5 = np.load(f)
        f.close()
        f = open('T7_6','r')
        self.p7_6 = np.load(f)
        f.close()
        f = open('T7_7','r')
        self.p7_7 = np.load(f)
        f.close()
        f = open('T7_8','r')
        self.p7_8 = np.load(f)
        f.close()
        f = open('T7_9','r')
        self.p7_9 = np.load(f)
        f.close()
        f = open('T7_10','r')
        self.p7_10 = np.load(f)
        f.close()

        f = open('T8_1','r')
        self.p8_1 = np.load(f)
        f.close()
        f = open('T8_2','r')
        self.p8_2 = np.load(f)
        f.close()
        f = open('T8_3','r')
        self.p8_3 = np.load(f)
        f.close()
        f = open('T8_4','r')
        self.p8_4 = np.load(f)
        f.close()
        f = open('T8_5','r')
        self.p8_5 = np.load(f)
        f.close()
        f = open('T8_6','r')
        self.p8_6 = np.load(f)
        f.close()
        f = open('T8_7','r')
        self.p8_7 = np.load(f)
        f.close()
        f = open('T8_8','r')
        self.p8_8 = np.load(f)
        f.close()
        f = open('T8_9','r')
        self.p8_9 = np.load(f)
        f.close()
        f = open('T8_10','r')
        self.p8_10 = np.load(f)
        f.close()
        
    def single_stages(self):
        print "Computing Single Stages..."
        d1 = min(len(self.p1_1.transpose()),len(self.p1_2.transpose()),len(self.p1_3.transpose()),len(self.p1_4.transpose()),len(self.p1_5.transpose()),len(self.p1_6.transpose()),len(self.p1_7.transpose()),len(self.p1_8.transpose()),len(self.p1_9.transpose()),len(self.p1_10.transpose()))
        d2 = min(len(self.p2_1.transpose()),len(self.p2_2.transpose()),len(self.p2_3.transpose()),len(self.p2_4.transpose()),len(self.p2_5.transpose()),len(self.p2_6.transpose()),len(self.p2_7.transpose()),len(self.p2_8.transpose()),len(self.p2_9.transpose()),len(self.p2_10.transpose()))
        d3 = min(len(self.p3_1.transpose()),len(self.p3_2.transpose()),len(self.p3_3.transpose()),len(self.p3_4.transpose()),len(self.p3_5.transpose()),len(self.p3_6.transpose()),len(self.p3_7.transpose()),len(self.p3_8.transpose()),len(self.p3_9.transpose()),len(self.p3_10.transpose()))
        d4 = min(len(self.p4_1.transpose()),len(self.p4_2.transpose()),len(self.p4_3.transpose()),len(self.p4_4.transpose()),len(self.p4_5.transpose()),len(self.p4_6.transpose()),len(self.p4_7.transpose()),len(self.p4_8.transpose()),len(self.p4_9.transpose()),len(self.p4_10.transpose()))
        d5 = min(len(self.p5_1.transpose()),len(self.p5_2.transpose()),len(self.p5_3.transpose()),len(self.p5_4.transpose()),len(self.p5_5.transpose()),len(self.p5_6.transpose()),len(self.p5_7.transpose()),len(self.p5_8.transpose()),len(self.p5_9.transpose()),len(self.p5_10.transpose()))
        d6 = min(len(self.p6_1.transpose()),len(self.p6_2.transpose()),len(self.p6_3.transpose()),len(self.p6_4.transpose()),len(self.p6_5.transpose()),len(self.p6_6.transpose()),len(self.p6_7.transpose()),len(self.p6_8.transpose()),len(self.p6_9.transpose()),len(self.p6_10.transpose()))
        d7 = min(len(self.p7_1.transpose()),len(self.p7_2.transpose()),len(self.p7_3.transpose()),len(self.p7_4.transpose()),len(self.p7_5.transpose()),len(self.p7_6.transpose()),len(self.p7_7.transpose()),len(self.p7_8.transpose()),len(self.p7_9.transpose()),len(self.p7_10.transpose()))
        d8 = min(len(self.p8_1.transpose()),len(self.p8_2.transpose()),len(self.p8_3.transpose()),len(self.p8_4.transpose()),len(self.p8_5.transpose()),len(self.p8_6.transpose()),len(self.p8_7.transpose()),len(self.p8_8.transpose()),len(self.p8_9.transpose()),len(self.p8_10.transpose()))
        j = 1
        self.ss_1 = np.zeros((7,d1/10+1))
        print "Stage 1"
        for i in range(0,d1):
            if (i % 10) == 0:
              if j == 1:
                  self.ss_1[0][i/10] = self.p1_1[0][i]
                  self.ss_1[1][i/10] = self.p1_1[1][i]
                  self.ss_1[2][i/10] = self.p1_1[2][i]
                  self.ss_1[3][i/10] = self.p1_1[3][i]
                  self.ss_1[4][i/10] = self.p1_1[4][i]
                  self.ss_1[5][i/10] = self.p1_1[5][i]
                  self.ss_1[6][i/10] = self.p1_1[6][i]
              elif j == 2:
                  self.ss_1[0][i/10] = self.p1_2[0][i]
                  self.ss_1[1][i/10] = self.p1_2[1][i]
                  self.ss_1[2][i/10] = self.p1_2[2][i]
                  self.ss_1[3][i/10] = self.p1_2[3][i]
                  self.ss_1[4][i/10] = self.p1_2[4][i]
                  self.ss_1[5][i/10] = self.p1_2[5][i]
                  self.ss_1[6][i/10] = self.p1_2[6][i]
              elif j == 3:
                  self.ss_1[0][i/10] = self.p1_3[0][i]
                  self.ss_1[1][i/10] = self.p1_3[1][i]
                  self.ss_1[2][i/10] = self.p1_3[2][i]
                  self.ss_1[3][i/10] = self.p1_3[3][i]
                  self.ss_1[4][i/10] = self.p1_3[4][i]
                  self.ss_1[5][i/10] = self.p1_3[5][i]
                  self.ss_1[6][i/10] = self.p1_3[6][i]
              elif j == 4:
                  self.ss_1[0][i/10] = self.p1_4[0][i]
                  self.ss_1[1][i/10] = self.p1_4[1][i]
                  self.ss_1[2][i/10] = self.p1_4[2][i]
                  self.ss_1[3][i/10] = self.p1_4[3][i]
                  self.ss_1[4][i/10] = self.p1_4[4][i]
                  self.ss_1[5][i/10] = self.p1_4[5][i]
                  self.ss_1[6][i/10] = self.p1_4[6][i]
              elif j == 5:
                  self.ss_1[0][i/10] = self.p1_5[0][i]
                  self.ss_1[1][i/10] = self.p1_5[1][i]
                  self.ss_1[2][i/10] = self.p1_5[2][i]
                  self.ss_1[3][i/10] = self.p1_5[3][i]
                  self.ss_1[4][i/10] = self.p1_5[4][i]
                  self.ss_1[5][i/10] = self.p1_5[5][i]
                  self.ss_1[6][i/10] = self.p1_5[6][i]
              elif j == 6:
                  self.ss_1[0][i/10] = self.p1_6[0][i]
                  self.ss_1[1][i/10] = self.p1_6[1][i]
                  self.ss_1[2][i/10] = self.p1_6[2][i]
                  self.ss_1[3][i/10] = self.p1_6[3][i]
                  self.ss_1[4][i/10] = self.p1_6[4][i]
                  self.ss_1[5][i/10] = self.p1_6[5][i]
                  self.ss_1[6][i/10] = self.p1_6[6][i]
              elif j == 7:
                  self.ss_1[0][i/10] = self.p1_7[0][i]
                  self.ss_1[1][i/10] = self.p1_7[1][i]
                  self.ss_1[2][i/10] = self.p1_7[2][i]
                  self.ss_1[3][i/10] = self.p1_7[3][i]
                  self.ss_1[4][i/10] = self.p1_7[4][i]
                  self.ss_1[5][i/10] = self.p1_7[5][i]
                  self.ss_1[6][i/10] = self.p1_7[6][i]
              elif j == 8:
                  self.ss_1[0][i/10] = self.p1_8[0][i]
                  self.ss_1[1][i/10] = self.p1_8[1][i]
                  self.ss_1[2][i/10] = self.p1_8[2][i]
                  self.ss_1[3][i/10] = self.p1_8[3][i]
                  self.ss_1[4][i/10] = self.p1_8[4][i]
                  self.ss_1[5][i/10] = self.p1_8[5][i]
                  self.ss_1[6][i/10] = self.p1_8[6][i]
              elif j == 9:
                  self.ss_1[0][i/10] = self.p1_9[0][i]
                  self.ss_1[1][i/10] = self.p1_9[1][i]
                  self.ss_1[2][i/10] = self.p1_9[2][i]
                  self.ss_1[3][i/10] = self.p1_9[3][i]
                  self.ss_1[4][i/10] = self.p1_9[4][i]
                  self.ss_1[5][i/10] = self.p1_9[5][i]
                  self.ss_1[6][i/10] = self.p1_9[6][i]
              elif j == 10:
                  self.ss_1[0][i/10] = self.p1_10[0][i]
                  self.ss_1[1][i/10] = self.p1_10[1][i]
                  self.ss_1[2][i/10] = self.p1_10[2][i]
                  self.ss_1[3][i/10] = self.p1_10[3][i]
                  self.ss_1[4][i/10] = self.p1_10[4][i]
                  self.ss_1[5][i/10] = self.p1_10[5][i]
                  self.ss_1[6][i/10] = self.p1_10[6][i]
                  j = 0
              j = j + 1

        j = 1
        self.ss_2 = np.zeros((7,d2/10+1))
        print "Stage 2"
        for i in range(0,d2):
            if (i % 10) == 0:
              if j == 1:
                  self.ss_2[0][i/10] = self.p2_1[0][i]
                  self.ss_2[1][i/10] = self.p2_1[1][i]
                  self.ss_2[2][i/10] = self.p2_1[2][i]
                  self.ss_2[3][i/10] = self.p2_1[3][i]
                  self.ss_2[4][i/10] = self.p2_1[4][i]
                  self.ss_2[5][i/10] = self.p2_1[5][i]
                  self.ss_2[6][i/10] = self.p2_1[6][i]
              elif j == 2:
                  self.ss_2[0][i/10] = self.p2_2[0][i]
                  self.ss_2[1][i/10] = self.p2_2[1][i]
                  self.ss_2[2][i/10] = self.p2_2[2][i]
                  self.ss_2[3][i/10] = self.p2_2[3][i]
                  self.ss_2[4][i/10] = self.p2_2[4][i]
                  self.ss_2[5][i/10] = self.p2_2[5][i]
                  self.ss_2[6][i/10] = self.p2_2[6][i]
              elif j == 3:
                  self.ss_2[0][i/10] = self.p2_3[0][i]
                  self.ss_2[1][i/10] = self.p2_3[1][i]
                  self.ss_2[2][i/10] = self.p2_3[2][i]
                  self.ss_2[3][i/10] = self.p2_3[3][i]
                  self.ss_2[4][i/10] = self.p2_3[4][i]
                  self.ss_2[5][i/10] = self.p2_3[5][i]
                  self.ss_2[6][i/10] = self.p2_3[6][i]
              elif j == 4:
                  self.ss_2[0][i/10] = self.p2_4[0][i]
                  self.ss_2[1][i/10] = self.p2_4[1][i]
                  self.ss_2[2][i/10] = self.p2_4[2][i]
                  self.ss_2[3][i/10] = self.p2_4[3][i]
                  self.ss_2[4][i/10] = self.p2_4[4][i]
                  self.ss_2[5][i/10] = self.p2_4[5][i]
                  self.ss_2[6][i/10] = self.p2_4[6][i]
              elif j == 5:
                  self.ss_2[0][i/10] = self.p2_5[0][i]
                  self.ss_2[1][i/10] = self.p2_5[1][i]
                  self.ss_2[2][i/10] = self.p2_5[2][i]
                  self.ss_2[3][i/10] = self.p2_5[3][i]
                  self.ss_2[4][i/10] = self.p2_5[4][i]
                  self.ss_2[5][i/10] = self.p2_5[5][i]
                  self.ss_2[6][i/10] = self.p2_5[6][i]
              elif j == 6:
                  self.ss_2[0][i/10] = self.p2_6[0][i]
                  self.ss_2[1][i/10] = self.p2_6[1][i]
                  self.ss_2[2][i/10] = self.p2_6[2][i]
                  self.ss_2[3][i/10] = self.p2_6[3][i]
                  self.ss_2[4][i/10] = self.p2_6[4][i]
                  self.ss_2[5][i/10] = self.p2_6[5][i]
                  self.ss_2[6][i/10] = self.p2_6[6][i]
              elif j == 7:
                  self.ss_2[0][i/10] = self.p2_7[0][i]
                  self.ss_2[1][i/10] = self.p2_7[1][i]
                  self.ss_2[2][i/10] = self.p2_7[2][i]
                  self.ss_2[3][i/10] = self.p2_7[3][i]
                  self.ss_2[4][i/10] = self.p2_7[4][i]
                  self.ss_2[5][i/10] = self.p2_7[5][i]
                  self.ss_2[6][i/10] = self.p2_7[6][i]
              elif j == 8:
                  self.ss_2[0][i/10] = self.p2_8[0][i]
                  self.ss_2[1][i/10] = self.p2_8[1][i]
                  self.ss_2[2][i/10] = self.p2_8[2][i]
                  self.ss_2[3][i/10] = self.p2_8[3][i]
                  self.ss_2[4][i/10] = self.p2_8[4][i]
                  self.ss_2[5][i/10] = self.p2_8[5][i]
                  self.ss_2[6][i/10] = self.p2_8[6][i]
              elif j == 9:
                  self.ss_2[0][i/10] = self.p2_9[0][i]
                  self.ss_2[1][i/10] = self.p2_9[1][i]
                  self.ss_2[2][i/10] = self.p2_9[2][i]
                  self.ss_2[3][i/10] = self.p2_9[3][i]
                  self.ss_2[4][i/10] = self.p2_9[4][i]
                  self.ss_2[5][i/10] = self.p2_9[5][i]
                  self.ss_2[6][i/10] = self.p2_9[6][i]
              elif j == 10:
                  self.ss_2[0][i/10] = self.p2_10[0][i]
                  self.ss_2[1][i/10] = self.p2_10[1][i]
                  self.ss_2[2][i/10] = self.p2_10[2][i]
                  self.ss_2[3][i/10] = self.p2_10[3][i]
                  self.ss_2[4][i/10] = self.p2_10[4][i]
                  self.ss_2[5][i/10] = self.p2_10[5][i]
                  self.ss_2[6][i/10] = self.p2_10[6][i]
                  j = 0
              j = j + 1


        j = 1
        self.ss_3 = np.zeros((7,d3/10+1))
        print "Stage 3"
        for i in range(0,d3):
            if (i % 10) == 0:
              if j == 1:
                  self.ss_3[0][i/10] = self.p3_1[0][i]
                  self.ss_3[1][i/10] = self.p3_1[1][i]
                  self.ss_3[2][i/10] = self.p3_1[2][i]
                  self.ss_3[3][i/10] = self.p3_1[3][i]
                  self.ss_3[4][i/10] = self.p3_1[4][i]
                  self.ss_3[5][i/10] = self.p3_1[5][i]
                  self.ss_3[6][i/10] = self.p3_1[6][i]
              elif j == 2:
                  self.ss_3[0][i/10] = self.p3_2[0][i]
                  self.ss_3[1][i/10] = self.p3_2[1][i]
                  self.ss_3[2][i/10] = self.p3_2[2][i]
                  self.ss_3[3][i/10] = self.p3_2[3][i]
                  self.ss_3[4][i/10] = self.p3_2[4][i]
                  self.ss_3[5][i/10] = self.p3_2[5][i]
                  self.ss_3[6][i/10] = self.p3_2[6][i]
              elif j == 3:
                  self.ss_3[0][i/10] = self.p3_3[0][i]
                  self.ss_3[1][i/10] = self.p3_3[1][i]
                  self.ss_3[2][i/10] = self.p3_3[2][i]
                  self.ss_3[3][i/10] = self.p3_3[3][i]
                  self.ss_3[4][i/10] = self.p3_3[4][i]
                  self.ss_3[5][i/10] = self.p3_3[5][i]
                  self.ss_3[6][i/10] = self.p3_3[6][i]
              elif j == 4:
                  self.ss_3[0][i/10] = self.p3_4[0][i]
                  self.ss_3[1][i/10] = self.p3_4[1][i]
                  self.ss_3[2][i/10] = self.p3_4[2][i]
                  self.ss_3[3][i/10] = self.p3_4[3][i]
                  self.ss_3[4][i/10] = self.p3_4[4][i]
                  self.ss_3[5][i/10] = self.p3_4[5][i]
                  self.ss_3[6][i/10] = self.p3_4[6][i]
              elif j == 5:
                  self.ss_3[0][i/10] = self.p3_5[0][i]
                  self.ss_3[1][i/10] = self.p3_5[1][i]
                  self.ss_3[2][i/10] = self.p3_5[2][i]
                  self.ss_3[3][i/10] = self.p3_5[3][i]
                  self.ss_3[4][i/10] = self.p3_5[4][i]
                  self.ss_3[5][i/10] = self.p3_5[5][i]
                  self.ss_3[6][i/10] = self.p3_5[6][i]
              elif j == 6:
                  self.ss_3[0][i/10] = self.p3_6[0][i]
                  self.ss_3[1][i/10] = self.p3_6[1][i]
                  self.ss_3[2][i/10] = self.p3_6[2][i]
                  self.ss_3[3][i/10] = self.p3_6[3][i]
                  self.ss_3[4][i/10] = self.p3_6[4][i]
                  self.ss_3[5][i/10] = self.p3_6[5][i]
                  self.ss_3[6][i/10] = self.p3_6[6][i]
              elif j == 7:
                  self.ss_3[0][i/10] = self.p3_7[0][i]
                  self.ss_3[1][i/10] = self.p3_7[1][i]
                  self.ss_3[2][i/10] = self.p3_7[2][i]
                  self.ss_3[3][i/10] = self.p3_7[3][i]
                  self.ss_3[4][i/10] = self.p3_7[4][i]
                  self.ss_3[5][i/10] = self.p3_7[5][i]
                  self.ss_3[6][i/10] = self.p3_7[6][i]
              elif j == 8:
                  self.ss_3[0][i/10] = self.p3_8[0][i]
                  self.ss_3[1][i/10] = self.p3_8[1][i]
                  self.ss_3[2][i/10] = self.p3_8[2][i]
                  self.ss_3[3][i/10] = self.p3_8[3][i]
                  self.ss_3[4][i/10] = self.p3_8[4][i]
                  self.ss_3[5][i/10] = self.p3_8[5][i]
                  self.ss_3[6][i/10] = self.p3_8[6][i]
              elif j == 9:
                  self.ss_3[0][i/10] = self.p3_9[0][i]
                  self.ss_3[1][i/10] = self.p3_9[1][i]
                  self.ss_3[2][i/10] = self.p3_9[2][i]
                  self.ss_3[3][i/10] = self.p3_9[3][i]
                  self.ss_3[4][i/10] = self.p3_9[4][i]
                  self.ss_3[5][i/10] = self.p3_9[5][i]
                  self.ss_3[6][i/10] = self.p3_9[6][i]
              elif j == 10:
                  self.ss_3[0][i/10] = self.p3_10[0][i]
                  self.ss_3[1][i/10] = self.p3_10[1][i]
                  self.ss_3[2][i/10] = self.p3_10[2][i]
                  self.ss_3[3][i/10] = self.p3_10[3][i]
                  self.ss_3[4][i/10] = self.p3_10[4][i]
                  self.ss_3[5][i/10] = self.p3_10[5][i]
                  self.ss_3[6][i/10] = self.p3_10[6][i]
                  j = 0
              j = j + 1


        j = 1
        self.ss_4 = np.zeros((7,d4/10+1))
        print "Stage 4"
        for i in range(0,d4):
            if (i % 10) == 0:
              if j == 1:
                  self.ss_4[0][i/10] = self.p4_1[0][i]
                  self.ss_4[1][i/10] = self.p4_1[1][i]
                  self.ss_4[2][i/10] = self.p4_1[2][i]
                  self.ss_4[3][i/10] = self.p4_1[3][i]
                  self.ss_4[4][i/10] = self.p4_1[4][i]
                  self.ss_4[5][i/10] = self.p4_1[5][i]
                  self.ss_4[6][i/10] = self.p4_1[6][i]
              elif j == 2:
                  self.ss_4[0][i/10] = self.p4_2[0][i]
                  self.ss_4[1][i/10] = self.p4_2[1][i]
                  self.ss_4[2][i/10] = self.p4_2[2][i]
                  self.ss_4[3][i/10] = self.p4_2[3][i]
                  self.ss_4[4][i/10] = self.p4_2[4][i]
                  self.ss_4[5][i/10] = self.p4_2[5][i]
                  self.ss_4[6][i/10] = self.p4_2[6][i]
              elif j == 3:
                  self.ss_4[0][i/10] = self.p4_3[0][i]
                  self.ss_4[1][i/10] = self.p4_3[1][i]
                  self.ss_4[2][i/10] = self.p4_3[2][i]
                  self.ss_4[3][i/10] = self.p4_3[3][i]
                  self.ss_4[4][i/10] = self.p4_3[4][i]
                  self.ss_4[5][i/10] = self.p4_3[5][i]
                  self.ss_4[6][i/10] = self.p4_3[6][i]
              elif j == 4:
                  self.ss_4[0][i/10] = self.p4_4[0][i]
                  self.ss_4[1][i/10] = self.p4_4[1][i]
                  self.ss_4[2][i/10] = self.p4_4[2][i]
                  self.ss_4[3][i/10] = self.p4_4[3][i]
                  self.ss_4[4][i/10] = self.p4_4[4][i]
                  self.ss_4[5][i/10] = self.p4_4[5][i]
                  self.ss_4[6][i/10] = self.p4_4[6][i]
              elif j == 5:
                  self.ss_4[0][i/10] = self.p4_5[0][i]
                  self.ss_4[1][i/10] = self.p4_5[1][i]
                  self.ss_4[2][i/10] = self.p4_5[2][i]
                  self.ss_4[3][i/10] = self.p4_5[3][i]
                  self.ss_4[4][i/10] = self.p4_5[4][i]
                  self.ss_4[5][i/10] = self.p4_5[5][i]
                  self.ss_4[6][i/10] = self.p4_5[6][i]
              elif j == 6:
                  self.ss_4[0][i/10] = self.p4_6[0][i]
                  self.ss_4[1][i/10] = self.p4_6[1][i]
                  self.ss_4[2][i/10] = self.p4_6[2][i]
                  self.ss_4[3][i/10] = self.p4_6[3][i]
                  self.ss_4[4][i/10] = self.p4_6[4][i]
                  self.ss_4[5][i/10] = self.p4_6[5][i]
                  self.ss_4[6][i/10] = self.p4_6[6][i]
              elif j == 7:
                  self.ss_4[0][i/10] = self.p4_7[0][i]
                  self.ss_4[1][i/10] = self.p4_7[1][i]
                  self.ss_4[2][i/10] = self.p4_7[2][i]
                  self.ss_4[3][i/10] = self.p4_7[3][i]
                  self.ss_4[4][i/10] = self.p4_7[4][i]
                  self.ss_4[5][i/10] = self.p4_7[5][i]
                  self.ss_4[6][i/10] = self.p4_7[6][i]
              elif j == 8:
                  self.ss_4[0][i/10] = self.p4_8[0][i]
                  self.ss_4[1][i/10] = self.p4_8[1][i]
                  self.ss_4[2][i/10] = self.p4_8[2][i]
                  self.ss_4[3][i/10] = self.p4_8[3][i]
                  self.ss_4[4][i/10] = self.p4_8[4][i]
                  self.ss_4[5][i/10] = self.p4_8[5][i]
                  self.ss_4[6][i/10] = self.p4_8[6][i]
              elif j == 9:
                  self.ss_4[0][i/10] = self.p4_9[0][i]
                  self.ss_4[1][i/10] = self.p4_9[1][i]
                  self.ss_4[2][i/10] = self.p4_9[2][i]
                  self.ss_4[3][i/10] = self.p4_9[3][i]
                  self.ss_4[4][i/10] = self.p4_9[4][i]
                  self.ss_4[5][i/10] = self.p4_9[5][i]
                  self.ss_4[6][i/10] = self.p4_9[6][i]
              elif j == 10:
                  self.ss_4[0][i/10] = self.p4_10[0][i]
                  self.ss_4[1][i/10] = self.p4_10[1][i]
                  self.ss_4[2][i/10] = self.p4_10[2][i]
                  self.ss_4[3][i/10] = self.p4_10[3][i]
                  self.ss_4[4][i/10] = self.p4_10[4][i]
                  self.ss_4[5][i/10] = self.p4_10[5][i]
                  self.ss_4[6][i/10] = self.p4_10[6][i]
                  j = 0
              j = j + 1

        j = 1
        self.ss_5 = np.zeros((7,d5/10+1))
        print "Stage 5"
        for i in range(0,d5):
            if (i % 10) == 0:
              if j == 1:
                  self.ss_5[0][i/10] = self.p5_1[0][i]
                  self.ss_5[1][i/10] = self.p5_1[1][i]
                  self.ss_5[2][i/10] = self.p5_1[2][i]
                  self.ss_5[3][i/10] = self.p5_1[3][i]
                  self.ss_5[4][i/10] = self.p5_1[4][i]
                  self.ss_5[5][i/10] = self.p5_1[5][i]
                  self.ss_5[6][i/10] = self.p5_1[6][i]
              elif j == 2:
                  self.ss_5[0][i/10] = self.p5_2[0][i]
                  self.ss_5[1][i/10] = self.p5_2[1][i]
                  self.ss_5[2][i/10] = self.p5_2[2][i]
                  self.ss_5[3][i/10] = self.p5_2[3][i]
                  self.ss_5[4][i/10] = self.p5_2[4][i]
                  self.ss_5[5][i/10] = self.p5_2[5][i]
                  self.ss_5[6][i/10] = self.p5_2[6][i]
              elif j == 3:
                  self.ss_5[0][i/10] = self.p5_3[0][i]
                  self.ss_5[1][i/10] = self.p5_3[1][i]
                  self.ss_5[2][i/10] = self.p5_3[2][i]
                  self.ss_5[3][i/10] = self.p5_3[3][i]
                  self.ss_5[4][i/10] = self.p5_3[4][i]
                  self.ss_5[5][i/10] = self.p5_3[5][i]
                  self.ss_5[6][i/10] = self.p5_3[6][i]
              elif j == 4:
                  self.ss_5[0][i/10] = self.p5_4[0][i]
                  self.ss_5[1][i/10] = self.p5_4[1][i]
                  self.ss_5[2][i/10] = self.p5_4[2][i]
                  self.ss_5[3][i/10] = self.p5_4[3][i]
                  self.ss_5[4][i/10] = self.p5_4[4][i]
                  self.ss_5[5][i/10] = self.p5_4[5][i]
                  self.ss_5[6][i/10] = self.p5_4[6][i]
              elif j == 5:
                  self.ss_5[0][i/10] = self.p5_5[0][i]
                  self.ss_5[1][i/10] = self.p5_5[1][i]
                  self.ss_5[2][i/10] = self.p5_5[2][i]
                  self.ss_5[3][i/10] = self.p5_5[3][i]
                  self.ss_5[4][i/10] = self.p5_5[4][i]
                  self.ss_5[5][i/10] = self.p5_5[5][i]
                  self.ss_5[6][i/10] = self.p5_5[6][i]
              elif j == 6:
                  self.ss_5[0][i/10] = self.p5_6[0][i]
                  self.ss_5[1][i/10] = self.p5_6[1][i]
                  self.ss_5[2][i/10] = self.p5_6[2][i]
                  self.ss_5[3][i/10] = self.p5_6[3][i]
                  self.ss_5[4][i/10] = self.p5_6[4][i]
                  self.ss_5[5][i/10] = self.p5_6[5][i]
                  self.ss_5[6][i/10] = self.p5_6[6][i]
              elif j == 7:
                  self.ss_5[0][i/10] = self.p5_7[0][i]
                  self.ss_5[1][i/10] = self.p5_7[1][i]
                  self.ss_5[2][i/10] = self.p5_7[2][i]
                  self.ss_5[3][i/10] = self.p5_7[3][i]
                  self.ss_5[4][i/10] = self.p5_7[4][i]
                  self.ss_5[5][i/10] = self.p5_7[5][i]
                  self.ss_5[6][i/10] = self.p5_7[6][i]
              elif j == 8:
                  self.ss_5[0][i/10] = self.p5_8[0][i]
                  self.ss_5[1][i/10] = self.p5_8[1][i]
                  self.ss_5[2][i/10] = self.p5_8[2][i]
                  self.ss_5[3][i/10] = self.p5_8[3][i]
                  self.ss_5[4][i/10] = self.p5_8[4][i]
                  self.ss_5[5][i/10] = self.p5_8[5][i]
                  self.ss_5[6][i/10] = self.p5_8[6][i]
              elif j == 9:
                  self.ss_5[0][i/10] = self.p5_9[0][i]
                  self.ss_5[1][i/10] = self.p5_9[1][i]
                  self.ss_5[2][i/10] = self.p5_9[2][i]
                  self.ss_5[3][i/10] = self.p5_9[3][i]
                  self.ss_5[4][i/10] = self.p5_9[4][i]
                  self.ss_5[5][i/10] = self.p5_9[5][i]
                  self.ss_5[6][i/10] = self.p5_9[6][i]
              elif j == 10:
                  self.ss_5[0][i/10] = self.p5_10[0][i]
                  self.ss_5[1][i/10] = self.p5_10[1][i]
                  self.ss_5[2][i/10] = self.p5_10[2][i]
                  self.ss_5[3][i/10] = self.p5_10[3][i]
                  self.ss_5[4][i/10] = self.p5_10[4][i]
                  self.ss_5[5][i/10] = self.p5_10[5][i]
                  self.ss_5[6][i/10] = self.p5_10[6][i]
                  j = 0
              j = j + 1

        j = 1
        self.ss_6 = np.zeros((7,d6/10+1))
        print "Stage 6"
        for i in range(0,d6):
            if (i % 10) == 0:
              if j == 1:
                  self.ss_6[0][i/10] = self.p6_1[0][i]
                  self.ss_6[1][i/10] = self.p6_1[1][i]
                  self.ss_6[2][i/10] = self.p6_1[2][i]
                  self.ss_6[3][i/10] = self.p6_1[3][i]
                  self.ss_6[4][i/10] = self.p6_1[4][i]
                  self.ss_6[5][i/10] = self.p6_1[5][i]
                  self.ss_6[6][i/10] = self.p6_1[6][i]
              elif j == 2:
                  self.ss_6[0][i/10] = self.p6_2[0][i]
                  self.ss_6[1][i/10] = self.p6_2[1][i]
                  self.ss_6[2][i/10] = self.p6_2[2][i]
                  self.ss_6[3][i/10] = self.p6_2[3][i]
                  self.ss_6[4][i/10] = self.p6_2[4][i]
                  self.ss_6[5][i/10] = self.p6_2[5][i]
                  self.ss_6[6][i/10] = self.p6_2[6][i]
              elif j == 3:
                  self.ss_6[0][i/10] = self.p6_3[0][i]
                  self.ss_6[1][i/10] = self.p6_3[1][i]
                  self.ss_6[2][i/10] = self.p6_3[2][i]
                  self.ss_6[3][i/10] = self.p6_3[3][i]
                  self.ss_6[4][i/10] = self.p6_3[4][i]
                  self.ss_6[5][i/10] = self.p6_3[5][i]
                  self.ss_6[6][i/10] = self.p6_3[6][i]
              elif j == 4:
                  self.ss_6[0][i/10] = self.p6_4[0][i]
                  self.ss_6[1][i/10] = self.p6_4[1][i]
                  self.ss_6[2][i/10] = self.p6_4[2][i]
                  self.ss_6[3][i/10] = self.p6_4[3][i]
                  self.ss_6[4][i/10] = self.p6_4[4][i]
                  self.ss_6[5][i/10] = self.p6_4[5][i]
                  self.ss_6[6][i/10] = self.p6_4[6][i]
              elif j == 5:
                  self.ss_6[0][i/10] = self.p6_5[0][i]
                  self.ss_6[1][i/10] = self.p6_5[1][i]
                  self.ss_6[2][i/10] = self.p6_5[2][i]
                  self.ss_6[3][i/10] = self.p6_5[3][i]
                  self.ss_6[4][i/10] = self.p6_5[4][i]
                  self.ss_6[5][i/10] = self.p6_5[5][i]
                  self.ss_6[6][i/10] = self.p6_5[6][i]
              elif j == 6:
                  self.ss_6[0][i/10] = self.p6_6[0][i]
                  self.ss_6[1][i/10] = self.p6_6[1][i]
                  self.ss_6[2][i/10] = self.p6_6[2][i]
                  self.ss_6[3][i/10] = self.p6_6[3][i]
                  self.ss_6[4][i/10] = self.p6_6[4][i]
                  self.ss_6[5][i/10] = self.p6_6[5][i]
                  self.ss_6[6][i/10] = self.p6_6[6][i]
              elif j == 7:
                  self.ss_6[0][i/10] = self.p6_7[0][i]
                  self.ss_6[1][i/10] = self.p6_7[1][i]
                  self.ss_6[2][i/10] = self.p6_7[2][i]
                  self.ss_6[3][i/10] = self.p6_7[3][i]
                  self.ss_6[4][i/10] = self.p6_7[4][i]
                  self.ss_6[5][i/10] = self.p6_7[5][i]
                  self.ss_6[6][i/10] = self.p6_7[6][i]
              elif j == 8:
                  self.ss_6[0][i/10] = self.p6_8[0][i]
                  self.ss_6[1][i/10] = self.p6_8[1][i]
                  self.ss_6[2][i/10] = self.p6_8[2][i]
                  self.ss_6[3][i/10] = self.p6_8[3][i]
                  self.ss_6[4][i/10] = self.p6_8[4][i]
                  self.ss_6[5][i/10] = self.p6_8[5][i]
                  self.ss_6[6][i/10] = self.p6_8[6][i]
              elif j == 9:
                  self.ss_6[0][i/10] = self.p6_9[0][i]
                  self.ss_6[1][i/10] = self.p6_9[1][i]
                  self.ss_6[2][i/10] = self.p6_9[2][i]
                  self.ss_6[3][i/10] = self.p6_9[3][i]
                  self.ss_6[4][i/10] = self.p6_9[4][i]
                  self.ss_6[5][i/10] = self.p6_9[5][i]
                  self.ss_6[6][i/10] = self.p6_9[6][i]
              elif j == 10:
                  self.ss_6[0][i/10] = self.p6_10[0][i]
                  self.ss_6[1][i/10] = self.p6_10[1][i]
                  self.ss_6[2][i/10] = self.p6_10[2][i]
                  self.ss_6[3][i/10] = self.p6_10[3][i]
                  self.ss_6[4][i/10] = self.p6_10[4][i]
                  self.ss_6[5][i/10] = self.p6_10[5][i]
                  self.ss_6[6][i/10] = self.p6_10[6][i]
                  j = 0
              j = j + 1

        j = 1
        self.ss_7 = np.zeros((7,d7/10+1))
        print "Stage 7"
        for i in range(0,d7):
            if (i % 10) == 0:
              if j == 1:
                  self.ss_7[0][i/10] = self.p7_1[0][i]
                  self.ss_7[1][i/10] = self.p7_1[1][i]
                  self.ss_7[2][i/10] = self.p7_1[2][i]
                  self.ss_7[3][i/10] = self.p7_1[3][i]
                  self.ss_7[4][i/10] = self.p7_1[4][i]
                  self.ss_7[5][i/10] = self.p7_1[5][i]
                  self.ss_7[6][i/10] = self.p7_1[6][i]
              elif j == 2:
                  self.ss_7[0][i/10] = self.p7_2[0][i]
                  self.ss_7[1][i/10] = self.p7_2[1][i]
                  self.ss_7[2][i/10] = self.p7_2[2][i]
                  self.ss_7[3][i/10] = self.p7_2[3][i]
                  self.ss_7[4][i/10] = self.p7_2[4][i]
                  self.ss_7[5][i/10] = self.p7_2[5][i]
                  self.ss_7[6][i/10] = self.p7_2[6][i]
              elif j == 3:
                  self.ss_7[0][i/10] = self.p7_3[0][i]
                  self.ss_7[1][i/10] = self.p7_3[1][i]
                  self.ss_7[2][i/10] = self.p7_3[2][i]
                  self.ss_7[3][i/10] = self.p7_3[3][i]
                  self.ss_7[4][i/10] = self.p7_3[4][i]
                  self.ss_7[5][i/10] = self.p7_3[5][i]
                  self.ss_7[6][i/10] = self.p7_3[6][i]
              elif j == 4:
                  self.ss_7[0][i/10] = self.p7_4[0][i]
                  self.ss_7[1][i/10] = self.p7_4[1][i]
                  self.ss_7[2][i/10] = self.p7_4[2][i]
                  self.ss_7[3][i/10] = self.p7_4[3][i]
                  self.ss_7[4][i/10] = self.p7_4[4][i]
                  self.ss_7[5][i/10] = self.p7_4[5][i]
                  self.ss_7[6][i/10] = self.p7_4[6][i]
              elif j == 5:
                  self.ss_7[0][i/10] = self.p7_5[0][i]
                  self.ss_7[1][i/10] = self.p7_5[1][i]
                  self.ss_7[2][i/10] = self.p7_5[2][i]
                  self.ss_7[3][i/10] = self.p7_5[3][i]
                  self.ss_7[4][i/10] = self.p7_5[4][i]
                  self.ss_7[5][i/10] = self.p7_5[5][i]
                  self.ss_7[6][i/10] = self.p7_5[6][i]
              elif j == 6:
                  self.ss_7[0][i/10] = self.p7_6[0][i]
                  self.ss_7[1][i/10] = self.p7_6[1][i]
                  self.ss_7[2][i/10] = self.p7_6[2][i]
                  self.ss_7[3][i/10] = self.p7_6[3][i]
                  self.ss_7[4][i/10] = self.p7_6[4][i]
                  self.ss_7[5][i/10] = self.p7_6[5][i]
                  self.ss_7[6][i/10] = self.p7_6[6][i]
              elif j == 7:
                  self.ss_7[0][i/10] = self.p7_7[0][i]
                  self.ss_7[1][i/10] = self.p7_7[1][i]
                  self.ss_7[2][i/10] = self.p7_7[2][i]
                  self.ss_7[3][i/10] = self.p7_7[3][i]
                  self.ss_7[4][i/10] = self.p7_7[4][i]
                  self.ss_7[5][i/10] = self.p7_7[5][i]
                  self.ss_7[6][i/10] = self.p7_7[6][i]
              elif j == 8:
                  self.ss_7[0][i/10] = self.p7_8[0][i]
                  self.ss_7[1][i/10] = self.p7_8[1][i]
                  self.ss_7[2][i/10] = self.p7_8[2][i]
                  self.ss_7[3][i/10] = self.p7_8[3][i]
                  self.ss_7[4][i/10] = self.p7_8[4][i]
                  self.ss_7[5][i/10] = self.p7_8[5][i]
                  self.ss_7[6][i/10] = self.p7_8[6][i]
              elif j == 9:
                  self.ss_7[0][i/10] = self.p7_9[0][i]
                  self.ss_7[1][i/10] = self.p7_9[1][i]
                  self.ss_7[2][i/10] = self.p7_9[2][i]
                  self.ss_7[3][i/10] = self.p7_9[3][i]
                  self.ss_7[4][i/10] = self.p7_9[4][i]
                  self.ss_7[5][i/10] = self.p7_9[5][i]
                  self.ss_7[6][i/10] = self.p7_9[6][i]
              elif j == 10:
                  self.ss_7[0][i/10] = self.p7_10[0][i]
                  self.ss_7[1][i/10] = self.p7_10[1][i]
                  self.ss_7[2][i/10] = self.p7_10[2][i]
                  self.ss_7[3][i/10] = self.p7_10[3][i]
                  self.ss_7[4][i/10] = self.p7_10[4][i]
                  self.ss_7[5][i/10] = self.p7_10[5][i]
                  self.ss_7[6][i/10] = self.p7_10[6][i]
                  j = 0
              j = j + 1

        j = 1
        self.ss_8 = np.zeros((7,d8/10+1))
        print "Stage 8"
        for i in range(0,d8):
            if (i % 10) == 0:
              if j == 1:
                  self.ss_8[0][i/10] = self.p8_1[0][i]
                  self.ss_8[1][i/10] = self.p8_1[1][i]
                  self.ss_8[2][i/10] = self.p8_1[2][i]
                  self.ss_8[3][i/10] = self.p8_1[3][i]
                  self.ss_8[4][i/10] = self.p8_1[4][i]
                  self.ss_8[5][i/10] = self.p8_1[5][i]
                  self.ss_8[6][i/10] = self.p8_1[6][i]
              elif j == 2:
                  self.ss_8[0][i/10] = self.p8_2[0][i]
                  self.ss_8[1][i/10] = self.p8_2[1][i]
                  self.ss_8[2][i/10] = self.p8_2[2][i]
                  self.ss_8[3][i/10] = self.p8_2[3][i]
                  self.ss_8[4][i/10] = self.p8_2[4][i]
                  self.ss_8[5][i/10] = self.p8_2[5][i]
                  self.ss_8[6][i/10] = self.p8_2[6][i]
              elif j == 3:
                  self.ss_8[0][i/10] = self.p8_3[0][i]
                  self.ss_8[1][i/10] = self.p8_3[1][i]
                  self.ss_8[2][i/10] = self.p8_3[2][i]
                  self.ss_8[3][i/10] = self.p8_3[3][i]
                  self.ss_8[4][i/10] = self.p8_3[4][i]
                  self.ss_8[5][i/10] = self.p8_3[5][i]
                  self.ss_8[6][i/10] = self.p8_3[6][i]
              elif j == 4:
                  self.ss_8[0][i/10] = self.p8_4[0][i]
                  self.ss_8[1][i/10] = self.p8_4[1][i]
                  self.ss_8[2][i/10] = self.p8_4[2][i]
                  self.ss_8[3][i/10] = self.p8_4[3][i]
                  self.ss_8[4][i/10] = self.p8_4[4][i]
                  self.ss_8[5][i/10] = self.p8_4[5][i]
                  self.ss_8[6][i/10] = self.p8_4[6][i]
              elif j == 5:
                  self.ss_8[0][i/10] = self.p8_5[0][i]
                  self.ss_8[1][i/10] = self.p8_5[1][i]
                  self.ss_8[2][i/10] = self.p8_5[2][i]
                  self.ss_8[3][i/10] = self.p8_5[3][i]
                  self.ss_8[4][i/10] = self.p8_5[4][i]
                  self.ss_8[5][i/10] = self.p8_5[5][i]
                  self.ss_8[6][i/10] = self.p8_5[6][i]
              elif j == 6:
                  self.ss_8[0][i/10] = self.p8_6[0][i]
                  self.ss_8[1][i/10] = self.p8_6[1][i]
                  self.ss_8[2][i/10] = self.p8_6[2][i]
                  self.ss_8[3][i/10] = self.p8_6[3][i]
                  self.ss_8[4][i/10] = self.p8_6[4][i]
                  self.ss_8[5][i/10] = self.p8_6[5][i]
                  self.ss_8[6][i/10] = self.p8_6[6][i]
              elif j == 7:
                  self.ss_8[0][i/10] = self.p8_7[0][i]
                  self.ss_8[1][i/10] = self.p8_7[1][i]
                  self.ss_8[2][i/10] = self.p8_7[2][i]
                  self.ss_8[3][i/10] = self.p8_7[3][i]
                  self.ss_8[4][i/10] = self.p8_7[4][i]
                  self.ss_8[5][i/10] = self.p8_7[5][i]
                  self.ss_8[6][i/10] = self.p8_7[6][i]
              elif j == 8:
                  self.ss_8[0][i/10] = self.p8_8[0][i]
                  self.ss_8[1][i/10] = self.p8_8[1][i]
                  self.ss_8[2][i/10] = self.p8_8[2][i]
                  self.ss_8[3][i/10] = self.p8_8[3][i]
                  self.ss_8[4][i/10] = self.p8_8[4][i]
                  self.ss_8[5][i/10] = self.p8_8[5][i]
                  self.ss_8[6][i/10] = self.p8_8[6][i]
              elif j == 9:
                  self.ss_8[0][i/10] = self.p8_9[0][i]
                  self.ss_8[1][i/10] = self.p8_9[1][i]
                  self.ss_8[2][i/10] = self.p8_9[2][i]
                  self.ss_8[3][i/10] = self.p8_9[3][i]
                  self.ss_8[4][i/10] = self.p8_9[4][i]
                  self.ss_8[5][i/10] = self.p8_9[5][i]
                  self.ss_8[6][i/10] = self.p8_9[6][i]
              elif j == 10:
                  self.ss_8[0][i/10] = self.p8_10[0][i]
                  self.ss_8[1][i/10] = self.p8_10[1][i]
                  self.ss_8[2][i/10] = self.p8_10[2][i]
                  self.ss_8[3][i/10] = self.p8_10[3][i]
                  self.ss_8[4][i/10] = self.p8_10[4][i]
                  self.ss_8[5][i/10] = self.p8_10[5][i]
                  self.ss_8[6][i/10] = self.p8_10[6][i]
                  j = 0
              j = j + 1
        print "Single State Computation Complete:"
        print "1-", np.shape(self.ss_1)
        print "2-", np.shape(self.ss_2)
        print "3-", np.shape(self.ss_3)
        print "4-", np.shape(self.ss_4)
        print "5-", np.shape(self.ss_5)
        print "6-", np.shape(self.ss_6)
        print "7-", np.shape(self.ss_7)
        print "8-", np.shape(self.ss_8)

    def complex_states(self):
        print "Computing Training Sets"
        d1 = len(self.ss_1.transpose())
        d2 = len(self.ss_2.transpose())
        d3 = len(self.ss_3.transpose())
        d4 = len(self.ss_4.transpose())
        d5 = len(self.ss_5.transpose())
        d6 = len(self.ss_6.transpose())
        d7 = len(self.ss_7.transpose())
        d8 = len(self.ss_8.transpose())
        total_set_number = d1+d2+d3+d4+d5+d6+d7+d8
        self.ts = np.zeros((6,total_set_number))
        self.ts_w = np.zeros(total_set_number)
        for i in range(0,total_set_number) :
          if i < d1 :
            self.ts[0][i] = self.ss_1[0][i]
            self.ts[1][i] = self.ss_1[1][i]
            self.ts[2][i] = self.ss_1[2][i]
            self.ts[3][i] = self.ss_1[3][i]
            self.ts[4][i] = self.ss_1[4][i]
            self.ts[5][i] = self.ss_1[5][i]
            self.ts_w[i] = self.ss_1[6][i]
          elif i < d1+d2 :
            self.ts[0][i] = self.ss_2[0][i-d1]
            self.ts[1][i] = self.ss_2[1][i-d1]
            self.ts[2][i] = self.ss_2[2][i-d1]
            self.ts[3][i] = self.ss_2[3][i-d1]
            self.ts[4][i] = self.ss_2[4][i-d1]
            self.ts[5][i] = self.ss_2[5][i-d1]
            self.ts_w[i] = self.ss_2[6][i-d1]
          elif i < d1+d2+d3 :
            self.ts[0][i] = self.ss_3[0][i-d1-d2]
            self.ts[1][i] = self.ss_3[1][i-d1-d2]
            self.ts[2][i] = self.ss_3[2][i-d1-d2]
            self.ts[3][i] = self.ss_3[3][i-d1-d2]
            self.ts[4][i] = self.ss_3[4][i-d1-d2]
            self.ts[5][i] = self.ss_3[5][i-d1-d2]
            self.ts_w[i] = self.ss_3[6][i-d1-d2]
          elif i < d1+d2+d3+d4 :
            self.ts[0][i] = self.ss_4[0][i-d1-d2-d3]
            self.ts[1][i] = self.ss_4[1][i-d1-d2-d3]
            self.ts[2][i] = self.ss_4[2][i-d1-d2-d3]
            self.ts[3][i] = self.ss_4[3][i-d1-d2-d3]
            self.ts[4][i] = self.ss_4[4][i-d1-d2-d3]
            self.ts[5][i] = self.ss_4[5][i-d1-d2-d3]
            self.ts_w[i] = self.ss_4[6][i-d1-d2-d3]
          elif i < d1+d2+d3+d4+d5 :
            self.ts[0][i] = self.ss_5[0][i-d1-d2-d3-d4]
            self.ts[1][i] = self.ss_5[1][i-d1-d2-d3-d4]
            self.ts[2][i] = self.ss_5[2][i-d1-d2-d3-d4]
            self.ts[3][i] = self.ss_5[3][i-d1-d2-d3-d4]
            self.ts[4][i] = self.ss_5[4][i-d1-d2-d3-d4]
            self.ts[5][i] = self.ss_5[5][i-d1-d2-d3-d4]
            self.ts_w[i] = self.ss_5[6][i-d1-d2-d3-d4]
          elif i < d1+d2+d3+d4+d5+d6 :
            self.ts[0][i] = self.ss_6[0][i-d1-d2-d3-d4-d5]
            self.ts[1][i] = self.ss_6[1][i-d1-d2-d3-d4-d5]
            self.ts[2][i] = self.ss_6[2][i-d1-d2-d3-d4-d5]
            self.ts[3][i] = self.ss_6[3][i-d1-d2-d3-d4-d5]
            self.ts[4][i] = self.ss_6[4][i-d1-d2-d3-d4-d5]
            self.ts[5][i] = self.ss_6[5][i-d1-d2-d3-d4-d5]
            self.ts_w[i] = self.ss_6[6][i-d1-d2-d3-d4-d5]
          elif i < d1+d2+d3+d4+d5+d6+d7 :
            self.ts[0][i] = self.ss_7[0][i-d1-d2-d3-d4-d5-d6]
            self.ts[1][i] = self.ss_7[1][i-d1-d2-d3-d4-d5-d6]
            self.ts[2][i] = self.ss_7[2][i-d1-d2-d3-d4-d5-d6]
            self.ts[3][i] = self.ss_7[3][i-d1-d2-d3-d4-d5-d6]
            self.ts[4][i] = self.ss_7[4][i-d1-d2-d3-d4-d5-d6]
            self.ts[5][i] = self.ss_7[5][i-d1-d2-d3-d4-d5-d6]
            self.ts_w[i] = self.ss_7[6][i-d1-d2-d3-d4-d5-d6]
          else :
            self.ts[0][i] = self.ss_8[0][i-d1-d2-d3-d4-d5-d6-d7]
            self.ts[1][i] = self.ss_8[1][i-d1-d2-d3-d4-d5-d6-d7]
            self.ts[2][i] = self.ss_8[2][i-d1-d2-d3-d4-d5-d6-d7]
            self.ts[3][i] = self.ss_8[3][i-d1-d2-d3-d4-d5-d6-d7]
            self.ts[4][i] = self.ss_8[4][i-d1-d2-d3-d4-d5-d6-d7]
            self.ts[5][i] = self.ss_8[5][i-d1-d2-d3-d4-d5-d6-d7]
            self.ts_w[i] = self.ss_8[6][i-d1-d2-d3-d4-d5-d6-d7]
        print "Training Set Complete"

    def cross_validation(self):
        print "creating cross validation tests"
        print "1-9"
        # Every 10th item comes from the target
        hold = len(self.ss_1.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_19_1 = np.zeros((6,hold))
        self.cv_19_1x = np.zeros((6,remain))
        self.cv_19_1w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_1.transpose())):
            if (i+1) % 10 == 0:
                self.cv_19_1x[0][j] = self.ss_1[0][i]
                self.cv_19_1x[1][j] = self.ss_1[1][i]
                self.cv_19_1x[2][j] = self.ss_1[2][i]
                self.cv_19_1x[3][j] = self.ss_1[3][i]
                self.cv_19_1x[4][j] = self.ss_1[4][i]
                self.cv_19_1x[5][j] = self.ss_1[5][i]
                j = j + 1
            else:
                self.cv_19_1[0][i-j] = self.ss_1[0][i]
                self.cv_19_1[1][i-j] = self.ss_1[1][i]
                self.cv_19_1[2][i-j] = self.ss_1[2][i]
                self.cv_19_1[3][i-j] = self.ss_1[3][i]
                self.cv_19_1[4][i-j] = self.ss_1[4][i]
                self.cv_19_1[5][i-j] = self.ss_1[5][i]
                self.cv_19_1w[i-j] = self.ss_1[6][i]

        hold = len(self.ss_2.transpose()) *9/10 +1
        remain = hold/9 + 1
        self.cv_19_2 = np.zeros((6,hold))
        self.cv_19_2x = np.zeros((6,remain))
        self.cv_19_2w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_2.transpose())):
            if (i+1) % 10 == 0:
                self.cv_19_2x[0][j] = self.ss_2[0][i]
                self.cv_19_2x[1][j] = self.ss_2[1][i]
                self.cv_19_2x[2][j] = self.ss_2[2][i]
                self.cv_19_2x[3][j] = self.ss_2[3][i]
                self.cv_19_2x[4][j] = self.ss_2[4][i]
                self.cv_19_2x[5][j] = self.ss_2[5][i]
                j = j + 1
            else:
                self.cv_19_2[0][i-j] = self.ss_2[0][i]
                self.cv_19_2[1][i-j] = self.ss_2[1][i]
                self.cv_19_2[2][i-j] = self.ss_2[2][i]
                self.cv_19_2[3][i-j] = self.ss_2[3][i]
                self.cv_19_2[4][i-j] = self.ss_2[4][i]
                self.cv_19_2[5][i-j] = self.ss_2[5][i]
                self.cv_19_2w[i-j] = self.ss_2[6][i]

        hold = len(self.ss_3.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_19_3 = np.zeros((6,hold))
        self.cv_19_3x = np.zeros((6,remain))
        self.cv_19_3w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_3.transpose())):
            if (i+1) % 10 == 0:
                self.cv_19_3x[0][j] = self.ss_3[0][i]
                self.cv_19_3x[1][j] = self.ss_3[1][i]
                self.cv_19_3x[2][j] = self.ss_3[2][i]
                self.cv_19_3x[3][j] = self.ss_3[3][i]
                self.cv_19_3x[4][j] = self.ss_3[4][i]
                self.cv_19_3x[5][j] = self.ss_3[5][i]
                j = j + 1
            else:
                self.cv_19_3[0][i-j] = self.ss_3[0][i]
                self.cv_19_3[1][i-j] = self.ss_3[1][i]
                self.cv_19_3[2][i-j] = self.ss_3[2][i]
                self.cv_19_3[3][i-j] = self.ss_3[3][i]
                self.cv_19_3[4][i-j] = self.ss_3[4][i]
                self.cv_19_3[5][i-j] = self.ss_3[5][i]
                self.cv_19_3w[i-j] = self.ss_3[6][i]

        hold = len(self.ss_4.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_19_4 = np.zeros((6,hold))
        self.cv_19_4x = np.zeros((6,remain))
        self.cv_19_4w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_4.transpose())):
            if (i+1) % 10 == 0:
                self.cv_19_4x[0][j] = self.ss_4[0][i]
                self.cv_19_4x[1][j] = self.ss_4[1][i]
                self.cv_19_4x[2][j] = self.ss_4[2][i]
                self.cv_19_4x[3][j] = self.ss_4[3][i]
                self.cv_19_4x[4][j] = self.ss_4[4][i]
                self.cv_19_4x[5][j] = self.ss_4[5][i]
                j = j + 1
            else:
                self.cv_19_4[0][i-j] = self.ss_4[0][i]
                self.cv_19_4[1][i-j] = self.ss_4[1][i]
                self.cv_19_4[2][i-j] = self.ss_4[2][i]
                self.cv_19_4[3][i-j] = self.ss_4[3][i]
                self.cv_19_4[4][i-j] = self.ss_4[4][i]
                self.cv_19_4[5][i-j] = self.ss_4[5][i]
                self.cv_19_4w[i-j] = self.ss_4[6][i]

        hold = len(self.ss_5.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_19_5 = np.zeros((6,hold))
        self.cv_19_5x = np.zeros((6,remain))
        self.cv_19_5w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_5.transpose())):
            if (i+1) % 10 == 0:
                self.cv_19_5x[0][j] = self.ss_5[0][i]
                self.cv_19_5x[1][j] = self.ss_5[1][i]
                self.cv_19_5x[2][j] = self.ss_5[2][i]
                self.cv_19_5x[3][j] = self.ss_5[3][i]
                self.cv_19_5x[4][j] = self.ss_5[4][i]
                self.cv_19_5x[5][j] = self.ss_5[5][i]
                j = j + 1
            else:
                self.cv_19_5[0][i-j] = self.ss_5[0][i]
                self.cv_19_5[1][i-j] = self.ss_5[1][i]
                self.cv_19_5[2][i-j] = self.ss_5[2][i]
                self.cv_19_5[3][i-j] = self.ss_5[3][i]
                self.cv_19_5[4][i-j] = self.ss_5[4][i]
                self.cv_19_5[5][i-j] = self.ss_5[5][i]
                self.cv_19_5w[i-j] = self.ss_5[6][i]

        hold = len(self.ss_6.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_19_6 = np.zeros((6,hold))
        self.cv_19_6x = np.zeros((6,remain))
        self.cv_19_6w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_6.transpose())):
            if (i+1) % 10 == 0:
                self.cv_19_6x[0][j] = self.ss_6[0][i]
                self.cv_19_6x[1][j] = self.ss_6[1][i]
                self.cv_19_6x[2][j] = self.ss_6[2][i]
                self.cv_19_6x[3][j] = self.ss_6[3][i]
                self.cv_19_6x[4][j] = self.ss_6[4][i]
                self.cv_19_6x[5][j] = self.ss_6[5][i]
                j = j + 1
            else:
                self.cv_19_6[0][i-j] = self.ss_6[0][i]
                self.cv_19_6[1][i-j] = self.ss_6[1][i]
                self.cv_19_6[2][i-j] = self.ss_6[2][i]
                self.cv_19_6[3][i-j] = self.ss_6[3][i]
                self.cv_19_6[4][i-j] = self.ss_6[4][i]
                self.cv_19_6[5][i-j] = self.ss_6[5][i]
                self.cv_19_6w[i-j] = self.ss_6[6][i]

        hold = len(self.ss_7.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_19_7 = np.zeros((6,hold))
        self.cv_19_7x = np.zeros((6,remain))
        self.cv_19_7w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_7.transpose())):
            if (i+1) % 10 == 0:
                self.cv_19_7x[0][j] = self.ss_7[0][i]
                self.cv_19_7x[1][j] = self.ss_7[1][i]
                self.cv_19_7x[2][j] = self.ss_7[2][i]
                self.cv_19_7x[3][j] = self.ss_7[3][i]
                self.cv_19_7x[4][j] = self.ss_7[4][i]
                self.cv_19_7x[5][j] = self.ss_7[5][i]
                j = j + 1
            else:
                self.cv_19_7[0][i-j] = self.ss_7[0][i]
                self.cv_19_7[1][i-j] = self.ss_7[1][i]
                self.cv_19_7[2][i-j] = self.ss_7[2][i]
                self.cv_19_7[3][i-j] = self.ss_7[3][i]
                self.cv_19_7[4][i-j] = self.ss_7[4][i]
                self.cv_19_7[5][i-j] = self.ss_7[5][i]
                self.cv_19_7w[i-j] = self.ss_7[6][i]

        hold = len(self.ss_8.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_19_8 = np.zeros((6,hold))
        self.cv_19_8x = np.zeros((6,remain))
        self.cv_19_8w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_8.transpose())):
            if (i+1) % 10 == 0:
                self.cv_19_8x[0][j] = self.ss_8[0][i]
                self.cv_19_8x[1][j] = self.ss_8[1][i]
                self.cv_19_8x[2][j] = self.ss_8[2][i]
                self.cv_19_8x[3][j] = self.ss_8[3][i]
                self.cv_19_8x[4][j] = self.ss_8[4][i]
                self.cv_19_8x[5][j] = self.ss_8[5][i]
                j = j + 1
            else:
                self.cv_19_8[0][i-j] = self.ss_8[0][i]
                self.cv_19_8[1][i-j] = self.ss_8[1][i]
                self.cv_19_8[2][i-j] = self.ss_8[2][i]
                self.cv_19_8[3][i-j] = self.ss_8[3][i]
                self.cv_19_8[4][i-j] = self.ss_8[4][i]
                self.cv_19_8[5][i-j] = self.ss_8[5][i]
                self.cv_19_8w[i-j] = self.ss_8[6][i]

        print "2-10" ########################################################################################################################################################################

        hold = len(self.ss_1.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_21_1 = np.zeros((6,hold))
        self.cv_21_1x = np.zeros((6,remain))
        self.cv_21_1w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_1.transpose())):
            if i % 10 == 0:
                self.cv_21_1x[0][j] = self.ss_1[0][i]
                self.cv_21_1x[1][j] = self.ss_1[1][i]
                self.cv_21_1x[2][j] = self.ss_1[2][i]
                self.cv_21_1x[3][j] = self.ss_1[3][i]
                self.cv_21_1x[4][j] = self.ss_1[4][i]
                self.cv_21_1x[5][j] = self.ss_1[5][i]
                j = j + 1
            else:
                self.cv_21_1[0][i-j] = self.ss_1[0][i]
                self.cv_21_1[1][i-j] = self.ss_1[1][i]
                self.cv_21_1[2][i-j] = self.ss_1[2][i]
                self.cv_21_1[3][i-j] = self.ss_1[3][i]
                self.cv_21_1[4][i-j] = self.ss_1[4][i]
                self.cv_21_1[5][i-j] = self.ss_1[5][i]
                self.cv_21_1w[i-j] = self.ss_1[6][i]

        hold = len(self.ss_2.transpose()) *9/10 +1
        remain = hold/9 + 1
        self.cv_21_2 = np.zeros((6,hold))
        self.cv_21_2x = np.zeros((6,remain))
        self.cv_21_2w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_2.transpose())):
            if i % 10 == 0:
                self.cv_21_2x[0][j] = self.ss_2[0][i]
                self.cv_21_2x[1][j] = self.ss_2[1][i]
                self.cv_21_2x[2][j] = self.ss_2[2][i]
                self.cv_21_2x[3][j] = self.ss_2[3][i]
                self.cv_21_2x[4][j] = self.ss_2[4][i]
                self.cv_21_2x[5][j] = self.ss_2[5][i]
                j = j + 1
            else:
                self.cv_21_2[0][i-j] = self.ss_2[0][i]
                self.cv_21_2[1][i-j] = self.ss_2[1][i]
                self.cv_21_2[2][i-j] = self.ss_2[2][i]
                self.cv_21_2[3][i-j] = self.ss_2[3][i]
                self.cv_21_2[4][i-j] = self.ss_2[4][i]
                self.cv_21_2[5][i-j] = self.ss_2[5][i]
                self.cv_21_2w[i-j] = self.ss_2[6][i]

        hold = len(self.ss_3.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_21_3 = np.zeros((6,hold))
        self.cv_21_3x = np.zeros((6,remain))
        self.cv_21_3w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_3.transpose())):
            if i % 10 == 0:
                self.cv_21_3x[0][j] = self.ss_3[0][i]
                self.cv_21_3x[1][j] = self.ss_3[1][i]
                self.cv_21_3x[2][j] = self.ss_3[2][i]
                self.cv_21_3x[3][j] = self.ss_3[3][i]
                self.cv_21_3x[4][j] = self.ss_3[4][i]
                self.cv_21_3x[5][j] = self.ss_3[5][i]
                j = j + 1
            else:
                self.cv_21_3[0][i-j] = self.ss_3[0][i]
                self.cv_21_3[1][i-j] = self.ss_3[1][i]
                self.cv_21_3[2][i-j] = self.ss_3[2][i]
                self.cv_21_3[3][i-j] = self.ss_3[3][i]
                self.cv_21_3[4][i-j] = self.ss_3[4][i]
                self.cv_21_3[5][i-j] = self.ss_3[5][i]
                self.cv_21_3w[i-j] = self.ss_3[6][i]

        hold = len(self.ss_4.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_21_4 = np.zeros((6,hold))
        self.cv_21_4x = np.zeros((6,remain))
        self.cv_21_4w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_4.transpose())):
            if i % 10 == 0:
                self.cv_21_4x[0][j] = self.ss_4[0][i]
                self.cv_21_4x[1][j] = self.ss_4[1][i]
                self.cv_21_4x[2][j] = self.ss_4[2][i]
                self.cv_21_4x[3][j] = self.ss_4[3][i]
                self.cv_21_4x[4][j] = self.ss_4[4][i]
                self.cv_21_4x[5][j] = self.ss_4[5][i]
                j = j + 1
            else:
                self.cv_21_4[0][i-j] = self.ss_4[0][i]
                self.cv_21_4[1][i-j] = self.ss_4[1][i]
                self.cv_21_4[2][i-j] = self.ss_4[2][i]
                self.cv_21_4[3][i-j] = self.ss_4[3][i]
                self.cv_21_4[4][i-j] = self.ss_4[4][i]
                self.cv_21_4[5][i-j] = self.ss_4[5][i]
                self.cv_21_4w[i-j] = self.ss_4[6][i]

        hold = len(self.ss_5.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_21_5 = np.zeros((6,hold))
        self.cv_21_5x = np.zeros((6,remain))
        self.cv_21_5w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_5.transpose())):
            if i % 10 == 0:
                self.cv_21_5x[0][j] = self.ss_5[0][i]
                self.cv_21_5x[1][j] = self.ss_5[1][i]
                self.cv_21_5x[2][j] = self.ss_5[2][i]
                self.cv_21_5x[3][j] = self.ss_5[3][i]
                self.cv_21_5x[4][j] = self.ss_5[4][i]
                self.cv_21_5x[5][j] = self.ss_5[5][i]
                j = j + 1
            else:
                self.cv_21_5[0][i-j] = self.ss_5[0][i]
                self.cv_21_5[1][i-j] = self.ss_5[1][i]
                self.cv_21_5[2][i-j] = self.ss_5[2][i]
                self.cv_21_5[3][i-j] = self.ss_5[3][i]
                self.cv_21_5[4][i-j] = self.ss_5[4][i]
                self.cv_21_5[5][i-j] = self.ss_5[5][i]
                self.cv_21_5w[i-j] = self.ss_5[6][i]

        hold = len(self.ss_6.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_21_6 = np.zeros((6,hold))
        self.cv_21_6x = np.zeros((6,remain))
        self.cv_21_6w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_6.transpose())):
            if i % 10 == 0:
                self.cv_21_6x[0][j] = self.ss_6[0][i]
                self.cv_21_6x[1][j] = self.ss_6[1][i]
                self.cv_21_6x[2][j] = self.ss_6[2][i]
                self.cv_21_6x[3][j] = self.ss_6[3][i]
                self.cv_21_6x[4][j] = self.ss_6[4][i]
                self.cv_21_6x[5][j] = self.ss_6[5][i]
                j = j + 1
            else:
                self.cv_21_6[0][i-j] = self.ss_6[0][i]
                self.cv_21_6[1][i-j] = self.ss_6[1][i]
                self.cv_21_6[2][i-j] = self.ss_6[2][i]
                self.cv_21_6[3][i-j] = self.ss_6[3][i]
                self.cv_21_6[4][i-j] = self.ss_6[4][i]
                self.cv_21_6[5][i-j] = self.ss_6[5][i]
                self.cv_21_6w[i-j] = self.ss_6[6][i]

        hold = len(self.ss_7.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_21_7 = np.zeros((6,hold))
        self.cv_21_7x = np.zeros((6,remain))
        self.cv_21_7w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_7.transpose())):
            if i % 10 == 0:
                self.cv_21_7x[0][j] = self.ss_7[0][i]
                self.cv_21_7x[1][j] = self.ss_7[1][i]
                self.cv_21_7x[2][j] = self.ss_7[2][i]
                self.cv_21_7x[3][j] = self.ss_7[3][i]
                self.cv_21_7x[4][j] = self.ss_7[4][i]
                self.cv_21_7x[5][j] = self.ss_7[5][i]
                j = j + 1
            else:
                self.cv_21_7[0][i-j] = self.ss_7[0][i]
                self.cv_21_7[1][i-j] = self.ss_7[1][i]
                self.cv_21_7[2][i-j] = self.ss_7[2][i]
                self.cv_21_7[3][i-j] = self.ss_7[3][i]
                self.cv_21_7[4][i-j] = self.ss_7[4][i]
                self.cv_21_7[5][i-j] = self.ss_7[5][i]
                self.cv_21_7w[i-j] = self.ss_7[6][i]

        hold = len(self.ss_8.transpose()) *9/10 +1
        remain = hold/9 +1
        self.cv_21_8 = np.zeros((6,hold))
        self.cv_21_8x = np.zeros((6,remain))
        self.cv_21_8w = np.zeros(hold)
        j = 0
        for i in range(0,len(self.ss_8.transpose())):
            if i % 10 == 0:
                self.cv_21_8x[0][j] = self.ss_8[0][i]
                self.cv_21_8x[1][j] = self.ss_8[1][i]
                self.cv_21_8x[2][j] = self.ss_8[2][i]
                self.cv_21_8x[3][j] = self.ss_8[3][i]
                self.cv_21_8x[4][j] = self.ss_8[4][i]
                self.cv_21_8x[5][j] = self.ss_8[5][i]
                j = j + 1
            else:
                self.cv_21_8[0][i-j] = self.ss_8[0][i]
                self.cv_21_8[1][i-j] = self.ss_8[1][i]
                self.cv_21_8[2][i-j] = self.ss_8[2][i]
                self.cv_21_8[3][i-j] = self.ss_8[3][i]
                self.cv_21_8[4][i-j] = self.ss_8[4][i]
                self.cv_21_8[5][i-j] = self.ss_8[5][i]
                self.cv_21_8w[i-j] = self.ss_8[6][i]

        d1 = len(self.cv_19_1.transpose())
        d2 = len(self.cv_19_2.transpose())
        d3 = len(self.cv_19_3.transpose())
        d4 = len(self.cv_19_4.transpose())
        d5 = len(self.cv_19_5.transpose())
        d6 = len(self.cv_19_6.transpose())
        d7 = len(self.cv_19_7.transpose())
        d8 = len(self.cv_19_8.transpose())
        total_set_number = d1+d2+d3+d4+d5+d6+d7+d8
        self.cv_19 = np.zeros((6,total_set_number))
        self.cv_19w = np.zeros(total_set_number)
        for i in range(0,total_set_number) :
          if i < d1 :
            self.cv_19[0][i] = self.cv_19_1[0][i]
            self.cv_19[1][i] = self.cv_19_1[1][i]
            self.cv_19[2][i] = self.cv_19_1[2][i]
            self.cv_19[3][i] = self.cv_19_1[3][i]
            self.cv_19[4][i] = self.cv_19_1[4][i]
            self.cv_19[5][i] = self.cv_19_1[5][i]
            self.cv_19w[i] = self.cv_19_1w[i]
          elif i < d1+d2 :
            self.cv_19[0][i] = self.cv_19_2[0][i-d1]
            self.cv_19[1][i] = self.cv_19_2[1][i-d1]
            self.cv_19[2][i] = self.cv_19_2[2][i-d1]
            self.cv_19[3][i] = self.cv_19_2[3][i-d1]
            self.cv_19[4][i] = self.cv_19_2[4][i-d1]
            self.cv_19[5][i] = self.cv_19_2[5][i-d1]
            self.cv_19w[i] = self.cv_19_2w[i-d1]
          elif i < d1+d2+d3 :
            self.cv_19[0][i] = self.cv_19_3[0][i-d1-d2]
            self.cv_19[1][i] = self.cv_19_3[1][i-d1-d2]
            self.cv_19[2][i] = self.cv_19_3[2][i-d1-d2]
            self.cv_19[3][i] = self.cv_19_3[3][i-d1-d2]
            self.cv_19[4][i] = self.cv_19_3[4][i-d1-d2]
            self.cv_19[5][i] = self.cv_19_3[5][i-d1-d2]
            self.cv_19w[i] = self.cv_19_3w[i-d1-d2]
          elif i < d1+d2+d3+d4 :
            self.cv_19[0][i] = self.cv_19_4[0][i-d1-d2-d3]
            self.cv_19[1][i] = self.cv_19_4[1][i-d1-d2-d3]
            self.cv_19[2][i] = self.cv_19_4[2][i-d1-d2-d3]
            self.cv_19[3][i] = self.cv_19_4[3][i-d1-d2-d3]
            self.cv_19[4][i] = self.cv_19_4[4][i-d1-d2-d3]
            self.cv_19[5][i] = self.cv_19_4[5][i-d1-d2-d3]
            self.cv_19w[i] = self.cv_19_4w[i-d1-d2-d3]
          elif i < d1+d2+d3+d4+d5 :
            self.cv_19[0][i] = self.cv_19_5[0][i-d1-d2-d3-d4]
            self.cv_19[1][i] = self.cv_19_5[1][i-d1-d2-d3-d4]
            self.cv_19[2][i] = self.cv_19_5[2][i-d1-d2-d3-d4]
            self.cv_19[3][i] = self.cv_19_5[3][i-d1-d2-d3-d4]
            self.cv_19[4][i] = self.cv_19_5[4][i-d1-d2-d3-d4]
            self.cv_19[5][i] = self.cv_19_5[5][i-d1-d2-d3-d4]
            self.cv_19w[i] = self.cv_19_5w[i-d1-d2-d3-d4]
          elif i < d1+d2+d3+d4+d5+d6 :
            self.cv_19[0][i] = self.cv_19_6[0][i-d1-d2-d3-d4-d5]
            self.cv_19[1][i] = self.cv_19_6[1][i-d1-d2-d3-d4-d5]
            self.cv_19[2][i] = self.cv_19_6[2][i-d1-d2-d3-d4-d5]
            self.cv_19[3][i] = self.cv_19_6[3][i-d1-d2-d3-d4-d5]
            self.cv_19[4][i] = self.cv_19_6[4][i-d1-d2-d3-d4-d5]
            self.cv_19[5][i] = self.cv_19_6[5][i-d1-d2-d3-d4-d5]
            self.cv_19w[i] = self.cv_19_6w[i-d1-d2-d3-d4-d5]
          elif i < d1+d2+d3+d4+d5+d6+d7 :
            self.cv_19[0][i] = self.cv_19_7[0][i-d1-d2-d3-d4-d5-d6]
            self.cv_19[1][i] = self.cv_19_7[1][i-d1-d2-d3-d4-d5-d6]
            self.cv_19[2][i] = self.cv_19_7[2][i-d1-d2-d3-d4-d5-d6]
            self.cv_19[3][i] = self.cv_19_7[3][i-d1-d2-d3-d4-d5-d6]
            self.cv_19[4][i] = self.cv_19_7[4][i-d1-d2-d3-d4-d5-d6]
            self.cv_19[5][i] = self.cv_19_7[5][i-d1-d2-d3-d4-d5-d6]
            self.cv_19w[i] = self.cv_19_7w[i-d1-d2-d3-d4-d5-d6]
          else :
            self.cv_19[0][i] = self.cv_19_8[0][i-d1-d2-d3-d4-d5-d6-d7]
            self.cv_19[1][i] = self.cv_19_8[1][i-d1-d2-d3-d4-d5-d6-d7]
            self.cv_19[2][i] = self.cv_19_8[2][i-d1-d2-d3-d4-d5-d6-d7]
            self.cv_19[3][i] = self.cv_19_8[3][i-d1-d2-d3-d4-d5-d6-d7]
            self.cv_19[4][i] = self.cv_19_8[4][i-d1-d2-d3-d4-d5-d6-d7]
            self.cv_19[5][i] = self.cv_19_8[5][i-d1-d2-d3-d4-d5-d6-d7]
            self.cv_19w[i] = self.cv_19_8w[i-d1-d2-d3-d4-d5-d6-d7]

        d1 = len(self.cv_21_1.transpose())
        d2 = len(self.cv_21_2.transpose())
        d3 = len(self.cv_21_3.transpose())
        d4 = len(self.cv_21_4.transpose())
        d5 = len(self.cv_21_5.transpose())
        d6 = len(self.cv_21_6.transpose())
        d7 = len(self.cv_21_7.transpose())
        d8 = len(self.cv_21_8.transpose())
        total_set_number = d1+d2+d3+d4+d5+d6+d7+d8
        self.cv_21 = np.zeros((6,total_set_number))
        self.cv_21w = np.zeros(total_set_number)
        for i in range(0,total_set_number) :
          if i < d1 :
            self.cv_21[0][i] = self.cv_21_1[0][i]
            self.cv_21[1][i] = self.cv_21_1[1][i]
            self.cv_21[2][i] = self.cv_21_1[2][i]
            self.cv_21[3][i] = self.cv_21_1[3][i]
            self.cv_21[4][i] = self.cv_21_1[4][i]
            self.cv_21[5][i] = self.cv_21_1[5][i]
            self.cv_21w[i] = self.cv_21_1w[i]
          elif i < d1+d2 :
            self.cv_21[0][i] = self.cv_21_2[0][i-d1]
            self.cv_21[1][i] = self.cv_21_2[1][i-d1]
            self.cv_21[2][i] = self.cv_21_2[2][i-d1]
            self.cv_21[3][i] = self.cv_21_2[3][i-d1]
            self.cv_21[4][i] = self.cv_21_2[4][i-d1]
            self.cv_21[5][i] = self.cv_21_2[5][i-d1]
            self.cv_21w[i] = self.cv_21_2w[i-d1]
          elif i < d1+d2+d3 :
            self.cv_21[0][i] = self.cv_21_3[0][i-d1-d2]
            self.cv_21[1][i] = self.cv_21_3[1][i-d1-d2]
            self.cv_21[2][i] = self.cv_21_3[2][i-d1-d2]
            self.cv_21[3][i] = self.cv_21_3[3][i-d1-d2]
            self.cv_21[4][i] = self.cv_21_3[4][i-d1-d2]
            self.cv_21[5][i] = self.cv_21_3[5][i-d1-d2]
            self.cv_21w[i] = self.cv_21_3w[i-d1-d2]
          elif i < d1+d2+d3+d4 :
            self.cv_21[0][i] = self.cv_21_4[0][i-d1-d2-d3]
            self.cv_21[1][i] = self.cv_21_4[1][i-d1-d2-d3]
            self.cv_21[2][i] = self.cv_21_4[2][i-d1-d2-d3]
            self.cv_21[3][i] = self.cv_21_4[3][i-d1-d2-d3]
            self.cv_21[4][i] = self.cv_21_4[4][i-d1-d2-d3]
            self.cv_21[5][i] = self.cv_21_4[5][i-d1-d2-d3]
            self.cv_21w[i] = self.cv_21_4w[i-d1-d2-d3]
          elif i < d1+d2+d3+d4+d5 :
            self.cv_21[0][i] = self.cv_21_5[0][i-d1-d2-d3-d4]
            self.cv_21[1][i] = self.cv_21_5[1][i-d1-d2-d3-d4]
            self.cv_21[2][i] = self.cv_21_5[2][i-d1-d2-d3-d4]
            self.cv_21[3][i] = self.cv_21_5[3][i-d1-d2-d3-d4]
            self.cv_21[4][i] = self.cv_21_5[4][i-d1-d2-d3-d4]
            self.cv_21[5][i] = self.cv_21_5[5][i-d1-d2-d3-d4]
            self.cv_21w[i] = self.cv_21_5w[i-d1-d2-d3-d4]
          elif i < d1+d2+d3+d4+d5+d6 :
            self.cv_21[0][i] = self.cv_21_6[0][i-d1-d2-d3-d4-d5]
            self.cv_21[1][i] = self.cv_21_6[1][i-d1-d2-d3-d4-d5]
            self.cv_21[2][i] = self.cv_21_6[2][i-d1-d2-d3-d4-d5]
            self.cv_21[3][i] = self.cv_21_6[3][i-d1-d2-d3-d4-d5]
            self.cv_21[4][i] = self.cv_21_6[4][i-d1-d2-d3-d4-d5]
            self.cv_21[5][i] = self.cv_21_6[5][i-d1-d2-d3-d4-d5]
            self.cv_21w[i] = self.cv_21_6w[i-d1-d2-d3-d4-d5]
          elif i < d1+d2+d3+d4+d5+d6+d7 :
            self.cv_21[0][i] = self.cv_21_7[0][i-d1-d2-d3-d4-d5-d6]
            self.cv_21[1][i] = self.cv_21_7[1][i-d1-d2-d3-d4-d5-d6]
            self.cv_21[2][i] = self.cv_21_7[2][i-d1-d2-d3-d4-d5-d6]
            self.cv_21[3][i] = self.cv_21_7[3][i-d1-d2-d3-d4-d5-d6]
            self.cv_21[4][i] = self.cv_21_7[4][i-d1-d2-d3-d4-d5-d6]
            self.cv_21[5][i] = self.cv_21_7[5][i-d1-d2-d3-d4-d5-d6]
            self.cv_21w[i] = self.cv_21_7w[i-d1-d2-d3-d4-d5-d6]
          else :
            self.cv_21[0][i] = self.cv_21_8[0][i-d1-d2-d3-d4-d5-d6-d7]
            self.cv_21[1][i] = self.cv_21_8[1][i-d1-d2-d3-d4-d5-d6-d7]
            self.cv_21[2][i] = self.cv_21_8[2][i-d1-d2-d3-d4-d5-d6-d7]
            self.cv_21[3][i] = self.cv_21_8[3][i-d1-d2-d3-d4-d5-d6-d7]
            self.cv_21[4][i] = self.cv_21_8[4][i-d1-d2-d3-d4-d5-d6-d7]
            self.cv_21[5][i] = self.cv_21_8[5][i-d1-d2-d3-d4-d5-d6-d7]
            self.cv_21w[i] = self.cv_21_8w[i-d1-d2-d3-d4-d5-d6-d7]  

class vs:
    def init(self, data): # weights might not need to be transposed
        self.ss_1 = data.ss_1.transpose()
        self.ss_2 = data.ss_2.transpose()
        self.ss_3 = data.ss_3.transpose()
        self.ss_4 = data.ss_4.transpose()
        self.ss_5 = data.ss_5.transpose()
        self.ss_6 = data.ss_6.transpose()
        self.ss_7 = data.ss_7.transpose()
        self.ss_8 = data.ss_8.transpose()
        self.ts = data.ts.transpose()
        self.tsw = data.ts_w.transpose()
        self.cv_19_1 = data.cv_21_1.transpose()
        self.cv_19_2 = data.cv_21_2.transpose()
        self.cv_19_3 = data.cv_21_3.transpose()
        self.cv_19_4 = data.cv_21_4.transpose()
        self.cv_19_5 = data.cv_21_5.transpose()
        self.cv_19_6 = data.cv_21_6.transpose()
        self.cv_19_7 = data.cv_21_7.transpose()
        self.cv_19_8 = data.cv_21_8.transpose()
        self.cv_21_1 = data.cv_21_1.transpose()
        self.cv_21_2 = data.cv_21_2.transpose()
        self.cv_21_3 = data.cv_21_3.transpose()
        self.cv_21_4 = data.cv_21_4.transpose()
        self.cv_21_5 = data.cv_21_5.transpose()
        self.cv_21_6 = data.cv_21_6.transpose()
        self.cv_21_7 = data.cv_21_7.transpose()
        self.cv_21_8 = data.cv_21_8.transpose()
	self.cv_19_1x = data.cv_19_1x.transpose()
	self.cv_19_2x = data.cv_19_1x.transpose()
	self.cv_19_3x = data.cv_19_1x.transpose()
	self.cv_19_4x = data.cv_19_1x.transpose()
	self.cv_19_5x = data.cv_19_1x.transpose()
	self.cv_19_6x = data.cv_19_1x.transpose()
	self.cv_19_7x = data.cv_19_1x.transpose()
	self.cv_19_8x = data.cv_19_1x.transpose()
	self.cv_21_1x = data.cv_21_1x.transpose()
	self.cv_21_2x = data.cv_21_2x.transpose()
	self.cv_21_3x = data.cv_21_3x.transpose()
	self.cv_21_4x = data.cv_21_4x.transpose()
	self.cv_21_5x = data.cv_21_5x.transpose()
	self.cv_21_6x = data.cv_21_6x.transpose()
	self.cv_21_7x = data.cv_21_7x.transpose()
	self.cv_21_8x = data.cv_21_8x.transpose()
        self.cv_19 = data.cv_19.transpose()
        self.cv_21 = data.cv_21.transpose()
        self.cv_19w = data.cv_19w.transpose()
        self.cv_21w = data.cv_21w.transpose()

    def info(self):
        print "If you have any questions, don't hesitate to ask Caleb."
        print "This core contains formated data for use in the multimodal system"
        print "The following formated data sets exist:"
        print "self.pX_Y   <-> contains raw data for each step. X is the step, Y is the trial"
        print "self.ss_X   <-> contains formatted (compressed) data for each step. X is the step"
        print "self.ts     <-> contains a complete training set for all trials. Does not contain tags."
        print "self.tsw    <-> contains the tags for the aforementioned self.ts"
        print "self.cv_X_Y <-> contains cross validation formated data. X = 19 implies 1->9, X = 21 implies 2->10. Y indicates the related state."
        print "self.cv_X_Yx<-> contains the remaining vector for cross validation. X and Y are the same as above."
        print "self.cv_X_Yw<-> contains the tags for the cross validation sets. X and Y are the same as above."
	print "self.cv_X   <-> contains a training set for cross validation."
	print "self.cv_Xw  <-> contains tag data for the training set for cross validation."
        print "Please note: due to adaptability, some of these sets may have a null column at the end."
        print "Otherwise, formatted sets have the following shape (some may lack element [6])"
        print "[0] -> Force X"
        print "[1] -> Force Y"
        print "[2] -> Force Z"
        print "[3] -> Torque X"
        print "[4] -> Torque Y"
        print "[5] -> Torque Z"
        print "[6] -> State tag"

if __name__ == "__main__":
    data = tacitus()
    data.init()
    data.single_stages()
    data.complex_states()
    data.cross_validation()
    push_me = vs()
    push_me.init(data)
    print "Saving Core"
    f = open("DataCore","w")
    pickle.dump(push_me,f)
    f.close()
