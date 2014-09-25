#!/usr/bin/env python

import numpy as np
import cPickle as pickle
import random as rand

class tacitus:

    def init(self):
        print "Loading Base Data..."
        f = open('./Sequence/T1_1','r')
        self.p1_1 = np.load(f)
        f.close()
        f = open('./Sequence/T1_2','r')
        self.p1_2 = np.load(f)
        f.close()
        f = open('./Sequence/T1_3','r')
        self.p1_3 = np.load(f)
        f.close()
        f = open('./Sequence/T1_4','r')
        self.p1_4 = np.load(f)
        f.close()
        f = open('./Sequence/T1_5','r')
        self.p1_5 = np.load(f)
        f.close()
        f = open('./Sequence/T1_6','r')
        self.p1_6 = np.load(f)
        f.close()
        f = open('./Sequence/T1_7','r')
        self.p1_7 = np.load(f)
        f.close()
        f = open('./Sequence/T1_8','r')
        self.p1_8 = np.load(f)
        f.close()
        f = open('./Sequence/T1_9','r')
        self.p1_9 = np.load(f)
        f.close()
        f = open('./Sequence/T1_10','r')
        self.p1_10 = np.load(f)
        f.close()
        f = open('./Sequence/T1_11','r')
        self.p1_11 = np.load(f)
        f.close()
        f = open('./Sequence/T1_12','r')
        self.p1_12 = np.load(f)
        f.close()
        f = open('./Sequence/T1_13','r')
        self.p1_13 = np.load(f)
        f.close()
        f = open('./Sequence/T1_14','r')
        self.p1_14 = np.load(f)
        f.close()
        f = open('./Sequence/T1_15','r')
        self.p1_15 = np.load(f)
        f.close()
        f = open('./Sequence/T1_16','r')
        self.p1_16 = np.load(f)
        f.close()
        f = open('./Sequence/T1_17','r')
        self.p1_17 = np.load(f)
        f.close()
        f = open('./Sequence/T1_18','r')
        self.p1_18 = np.load(f)
        f.close()
        f = open('./Sequence/T1_19','r')
        self.p1_19 = np.load(f)
        f.close()
        f = open('./Sequence/T1_20','r')
        self.p1_20 = np.load(f)
        f.close()
      
        f = open('./Sequence/T2_1','r')
        self.p2_1 = np.load(f)
        f.close()
        f = open('./Sequence/T2_2','r')
        self.p2_2 = np.load(f)
        f.close()
        f = open('./Sequence/T2_3','r')
        self.p2_3 = np.load(f)
        f.close()
        f = open('./Sequence/T2_4','r')
        self.p2_4 = np.load(f)
        f.close()
        f = open('./Sequence/T2_5','r')
        self.p2_5 = np.load(f)
        f.close()
        f = open('./Sequence/T2_6','r')
        self.p2_6 = np.load(f)
        f.close()
        f = open('./Sequence/T2_7','r')
        self.p2_7 = np.load(f)
        f.close()
        f = open('./Sequence/T2_8','r')
        self.p2_8 = np.load(f)
        f.close()
        f = open('./Sequence/T2_9','r')
        self.p2_9 = np.load(f)
        f.close()
        f = open('./Sequence/T2_10','r')
        self.p2_10 = np.load(f)
        f.close()
        f = open('./Sequence/T2_11','r')
        self.p2_11 = np.load(f)
        f.close()
        f = open('./Sequence/T2_12','r')
        self.p2_12 = np.load(f)
        f.close()
        f = open('./Sequence/T2_13','r')
        self.p2_13 = np.load(f)
        f.close()
        f = open('./Sequence/T2_14','r')
        self.p2_14 = np.load(f)
        f.close()
        f = open('./Sequence/T2_15','r')
        self.p2_15 = np.load(f)
        f.close()
        f = open('./Sequence/T2_16','r')
        self.p2_16 = np.load(f)
        f.close()
        f = open('./Sequence/T2_17','r')
        self.p2_17 = np.load(f)
        f.close()
        f = open('./Sequence/T2_18','r')
        self.p2_18 = np.load(f)
        f.close()
        f = open('./Sequence/T2_19','r')
        self.p2_19 = np.load(f)
        f.close()
        f = open('./Sequence/T2_20','r')
        self.p2_20 = np.load(f)
        f.close()

        f = open('./Sequence/T3_1','r')
        self.p3_1 = np.load(f)
        f.close()
        f = open('./Sequence/T3_2','r')
        self.p3_2 = np.load(f)
        f.close()
        f = open('./Sequence/T3_3','r')
        self.p3_3 = np.load(f)
        f.close()
        f = open('./Sequence/T3_4','r')
        self.p3_4 = np.load(f)
        f.close()
        f = open('./Sequence/T3_5','r')
        self.p3_5 = np.load(f)
        f.close()
        f = open('./Sequence/T3_6','r')
        self.p3_6 = np.load(f)
        f.close()
        f = open('./Sequence/T3_7','r')
        self.p3_7 = np.load(f)
        f.close()
        f = open('./Sequence/T3_8','r')
        self.p3_8 = np.load(f)
        f.close()
        f = open('./Sequence/T3_9','r')
        self.p3_9 = np.load(f)
        f.close()
        f = open('./Sequence/T3_10','r')
        self.p3_10 = np.load(f)
        f.close()
        f = open('./Sequence/T3_11','r')
        self.p3_11 = np.load(f)
        f.close()
        f = open('./Sequence/T3_12','r')
        self.p3_12 = np.load(f)
        f.close()
        f = open('./Sequence/T3_13','r')
        self.p3_13 = np.load(f)
        f.close()
        f = open('./Sequence/T3_14','r')
        self.p3_14 = np.load(f)
        f.close()
        f = open('./Sequence/T3_15','r')
        self.p3_15 = np.load(f)
        f.close()
        f = open('./Sequence/T3_16','r')
        self.p3_16 = np.load(f)
        f.close()
        f = open('./Sequence/T3_17','r')
        self.p3_17 = np.load(f)
        f.close()
        f = open('./Sequence/T3_18','r')
        self.p3_18 = np.load(f)
        f.close()
        f = open('./Sequence/T3_19','r')
        self.p3_19 = np.load(f)
        f.close()
        f = open('./Sequence/T3_20','r')
        self.p3_20 = np.load(f)
        f.close()

        f = open('./Sequence/T4_1','r')
        self.p4_1 = np.load(f)
        f.close()
        f = open('./Sequence/T4_2','r')
        self.p4_2 = np.load(f)
        f.close()
        f = open('./Sequence/T4_3','r')
        self.p4_3 = np.load(f)
        f.close()
        f = open('./Sequence/T4_4','r')
        self.p4_4 = np.load(f)
        f.close()
        f = open('./Sequence/T4_5','r')
        self.p4_5 = np.load(f)
        f.close()
        f = open('./Sequence/T4_6','r')
        self.p4_6 = np.load(f)
        f.close()
        f = open('./Sequence/T4_7','r')
        self.p4_7 = np.load(f)
        f.close()
        f = open('./Sequence/T4_8','r')
        self.p4_8 = np.load(f)
        f.close()
        f = open('./Sequence/T4_9','r')
        self.p4_9 = np.load(f)
        f.close()
        f = open('./Sequence/T4_10','r')
        self.p4_10 = np.load(f)
        f.close()
        f = open('./Sequence/T4_11','r')
        self.p4_11 = np.load(f)
        f.close()
        f = open('./Sequence/T4_12','r')
        self.p4_12 = np.load(f)
        f.close()
        f = open('./Sequence/T4_13','r')
        self.p4_13 = np.load(f)
        f.close()
        f = open('./Sequence/T4_14','r')
        self.p4_14 = np.load(f)
        f.close()
        f = open('./Sequence/T4_15','r')
        self.p4_15 = np.load(f)
        f.close()
        f = open('./Sequence/T4_16','r')
        self.p4_16 = np.load(f)
        f.close()
        f = open('./Sequence/T4_17','r')
        self.p4_17 = np.load(f)
        f.close()
        f = open('./Sequence/T4_18','r')
        self.p4_18 = np.load(f)
        f.close()
        f = open('./Sequence/T4_19','r')
        self.p4_19 = np.load(f)
        f.close()
        f = open('./Sequence/T4_20','r')
        self.p4_20 = np.load(f)
        f.close()

        f = open('./Sequence/T5_1','r')
        self.p5_1 = np.load(f)
        f.close()
        f = open('./Sequence/T5_2','r')
        self.p5_2 = np.load(f)
        f.close()
        f = open('./Sequence/T5_3','r')
        self.p5_3 = np.load(f)
        f.close()
        f = open('./Sequence/T5_4','r')
        self.p5_4 = np.load(f)
        f.close()
        f = open('./Sequence/T5_5','r')
        self.p5_5 = np.load(f)
        f.close()
        f = open('./Sequence/T5_6','r')
        self.p5_6 = np.load(f)
        f.close()
        f = open('./Sequence/T5_7','r')
        self.p5_7 = np.load(f)
        f.close()
        f = open('./Sequence/T5_8','r')
        self.p5_8 = np.load(f)
        f.close()
        f = open('./Sequence/T5_9','r')
        self.p5_9 = np.load(f)
        f.close()
        f = open('./Sequence/T5_10','r')
        self.p5_10 = np.load(f)
        f.close()
        f = open('./Sequence/T5_11','r')
        self.p5_11 = np.load(f)
        f.close()
        f = open('./Sequence/T5_12','r')
        self.p5_12 = np.load(f)
        f.close()
        f = open('./Sequence/T5_13','r')
        self.p5_13 = np.load(f)
        f.close()
        f = open('./Sequence/T5_14','r')
        self.p5_14 = np.load(f)
        f.close()
        f = open('./Sequence/T5_15','r')
        self.p5_15 = np.load(f)
        f.close()
        f = open('./Sequence/T5_16','r')
        self.p5_16 = np.load(f)
        f.close()
        f = open('./Sequence/T5_17','r')
        self.p5_17 = np.load(f)
        f.close()
        f = open('./Sequence/T5_18','r')
        self.p5_18 = np.load(f)
        f.close()
        f = open('./Sequence/T5_19','r')
        self.p5_19 = np.load(f)
        f.close()
        f = open('./Sequence/T5_20','r')
        self.p5_20 = np.load(f)
        f.close()

        f = open('./Sequence/T6_1','r')
        self.p6_1 = np.load(f)
        f.close()
        f = open('./Sequence/T6_2','r')
        self.p6_2 = np.load(f)
        f.close()
        f = open('./Sequence/T6_3','r')
        self.p6_3 = np.load(f)
        f.close()
        f = open('./Sequence/T6_4','r')
        self.p6_4 = np.load(f)
        f.close()
        f = open('./Sequence/T6_5','r')
        self.p6_5 = np.load(f)
        f.close()
        f = open('./Sequence/T6_6','r')
        self.p6_6 = np.load(f)
        f.close()
        f = open('./Sequence/T6_7','r')
        self.p6_7 = np.load(f)
        f.close()
        f = open('./Sequence/T6_8','r')
        self.p6_8 = np.load(f)
        f.close()
        f = open('./Sequence/T6_9','r')
        self.p6_9 = np.load(f)
        f.close()
        f = open('./Sequence/T6_10','r')
        self.p6_10 = np.load(f)
        f.close()
        f = open('./Sequence/T6_11','r')
        self.p6_11 = np.load(f)
        f.close()
        f = open('./Sequence/T6_12','r')
        self.p6_12 = np.load(f)
        f.close()
        f = open('./Sequence/T6_13','r')
        self.p6_13 = np.load(f)
        f.close()
        f = open('./Sequence/T6_14','r')
        self.p6_14 = np.load(f)
        f.close()
        f = open('./Sequence/T6_15','r')
        self.p6_15 = np.load(f)
        f.close()
        f = open('./Sequence/T6_16','r')
        self.p6_16 = np.load(f)
        f.close()
        f = open('./Sequence/T6_17','r')
        self.p6_17 = np.load(f)
        f.close()
        f = open('./Sequence/T6_18','r')
        self.p6_18 = np.load(f)
        f.close()
        f = open('./Sequence/T6_19','r')
        self.p6_19 = np.load(f)
        f.close()
        f = open('./Sequence/T6_20','r')
        self.p6_20 = np.load(f)
        f.close()

        f = open('./Sequence/T7_1','r')
        self.p7_1 = np.load(f)
        f.close()
        f = open('./Sequence/T7_2','r')
        self.p7_2 = np.load(f)
        f.close()
        f = open('./Sequence/T7_3','r')
        self.p7_3 = np.load(f)
        f.close()
        f = open('./Sequence/T7_4','r')
        self.p7_4 = np.load(f)
        f.close()
        f = open('./Sequence/T7_5','r')
        self.p7_5 = np.load(f)
        f.close()
        f = open('./Sequence/T7_6','r')
        self.p7_6 = np.load(f)
        f.close()
        f = open('./Sequence/T7_7','r')
        self.p7_7 = np.load(f)
        f.close()
        f = open('./Sequence/T7_8','r')
        self.p7_8 = np.load(f)
        f.close()
        f = open('./Sequence/T7_9','r')
        self.p7_9 = np.load(f)
        f.close()
        f = open('./Sequence/T7_10','r')
        self.p7_10 = np.load(f)
        f.close()
        f = open('./Sequence/T7_11','r')
        self.p7_11 = np.load(f)
        f.close()
        f = open('./Sequence/T7_12','r')
        self.p7_12 = np.load(f)
        f.close()
        f = open('./Sequence/T7_13','r')
        self.p7_13 = np.load(f)
        f.close()
        f = open('./Sequence/T7_14','r')
        self.p7_14 = np.load(f)
        f.close()
        f = open('./Sequence/T7_15','r')
        self.p7_15 = np.load(f)
        f.close()
        f = open('./Sequence/T7_16','r')
        self.p7_16 = np.load(f)
        f.close()
        f = open('./Sequence/T7_17','r')
        self.p7_17 = np.load(f)
        f.close()
        f = open('./Sequence/T7_18','r')
        self.p7_18 = np.load(f)
        f.close()
        f = open('./Sequence/T7_19','r')
        self.p7_19 = np.load(f)
        f.close()
        f = open('./Sequence/T7_20','r')
        self.p7_20 = np.load(f)
        f.close()

        f = open('./Sequence/T8_1','r')
        self.p8_1 = np.load(f)
        f.close()
        f = open('./Sequence/T8_2','r')
        self.p8_2 = np.load(f)
        f.close()
        f = open('./Sequence/T8_3','r')
        self.p8_3 = np.load(f)
        f.close()
        f = open('./Sequence/T8_4','r')
        self.p8_4 = np.load(f)
        f.close()
        f = open('./Sequence/T8_5','r')
        self.p8_5 = np.load(f)
        f.close()
        f = open('./Sequence/T8_6','r')
        self.p8_6 = np.load(f)
        f.close()
        f = open('./Sequence/T8_7','r')
        self.p8_7 = np.load(f)
        f.close()
        f = open('./Sequence/T8_8','r')
        self.p8_8 = np.load(f)
        f.close()
        f = open('./Sequence/T8_9','r')
        self.p8_9 = np.load(f)
        f.close()
        f = open('./Sequence/T8_10','r')
        self.p8_10 = np.load(f)
        f.close()
        f = open('./Sequence/T8_11','r')
        self.p8_11 = np.load(f)
        f.close()
        f = open('./Sequence/T8_12','r')
        self.p8_12 = np.load(f)
        f.close()
        f = open('./Sequence/T8_13','r')
        self.p8_13 = np.load(f)
        f.close()
        f = open('./Sequence/T8_14','r')
        self.p8_14 = np.load(f)
        f.close()
        f = open('./Sequence/T8_15','r')
        self.p8_15 = np.load(f)
        f.close()
        f = open('./Sequence/T8_16','r')
        self.p8_16 = np.load(f)
        f.close()
        f = open('./Sequence/T8_17','r')
        self.p8_17 = np.load(f)
        f.close()
        f = open('./Sequence/T8_18','r')
        self.p8_18 = np.load(f)
        f.close()
        f = open('./Sequence/T8_19','r')
        self.p8_19 = np.load(f)
        f.close()
        f = open('./Sequence/T8_20','r')
        self.p8_20 = np.load(f)
        f.close()

        f = open('./Sequence/T9_1','r')
        self.p9_1 = np.load(f)
        f.close()
        f = open('./Sequence/T9_2','r')
        self.p9_2 = np.load(f)
        f.close()
        f = open('./Sequence/T9_3','r')
        self.p9_3 = np.load(f)
        f.close()
        f = open('./Sequence/T9_4','r')
        self.p9_4 = np.load(f)
        f.close()
        f = open('./Sequence/T9_5','r')
        self.p9_5 = np.load(f)
        f.close()
        f = open('./Sequence/T9_6','r')
        self.p9_6 = np.load(f)
        f.close()
        f = open('./Sequence/T9_7','r')
        self.p9_7 = np.load(f)
        f.close()
        f = open('./Sequence/T9_8','r')
        self.p9_8 = np.load(f)
        f.close()
        f = open('./Sequence/T9_9','r')
        self.p9_9 = np.load(f)
        f.close()
        f = open('./Sequence/T9_10','r')
        self.p9_10 = np.load(f)
        f.close()
        f = open('./Sequence/T9_11','r')
        self.p9_11 = np.load(f)
        f.close()
        f = open('./Sequence/T9_12','r')
        self.p9_12 = np.load(f)
        f.close()
        f = open('./Sequence/T9_13','r')
        self.p9_13 = np.load(f)
        f.close()
        f = open('./Sequence/T9_14','r')
        self.p9_14 = np.load(f)
        f.close()
        f = open('./Sequence/T9_15','r')
        self.p9_15 = np.load(f)
        f.close()
        f = open('./Sequence/T9_16','r')
        self.p9_16 = np.load(f)
        f.close()
        f = open('./Sequence/T9_17','r')
        self.p9_17 = np.load(f)
        f.close()
        f = open('./Sequence/T9_18','r')
        self.p9_18 = np.load(f)
        f.close()
        f = open('./Sequence/T9_19','r')
        self.p9_19 = np.load(f)
        f.close()
        f = open('./Sequence/T9_20','r')
        self.p9_20 = np.load(f)
        f.close()

        f = open('./Sequence/T10_1','r')
        self.p10_1 = np.load(f)
        f.close()
        f = open('./Sequence/T10_2','r')
        self.p10_2 = np.load(f)
        f.close()
        f = open('./Sequence/T10_3','r')
        self.p10_3 = np.load(f)
        f.close()
        f = open('./Sequence/T10_4','r')
        self.p10_4 = np.load(f)
        f.close()
        f = open('./Sequence/T10_5','r')
        self.p10_5 = np.load(f)
        f.close()
        f = open('./Sequence/T10_6','r')
        self.p10_6 = np.load(f)
        f.close()
        f = open('./Sequence/T10_7','r')
        self.p10_7 = np.load(f)
        f.close()
        f = open('./Sequence/T10_8','r')
        self.p10_8 = np.load(f)
        f.close()
        f = open('./Sequence/T10_9','r')
        self.p10_9 = np.load(f)
        f.close()
        f = open('./Sequence/T10_10','r')
        self.p10_10 = np.load(f)
        f.close()
        f = open('./Sequence/T10_11','r')
        self.p10_11 = np.load(f)
        f.close()
        f = open('./Sequence/T10_12','r')
        self.p10_12 = np.load(f)
        f.close()
        f = open('./Sequence/T10_13','r')
        self.p10_13 = np.load(f)
        f.close()
        f = open('./Sequence/T10_14','r')
        self.p10_14 = np.load(f)
        f.close()
        f = open('./Sequence/T10_15','r')
        self.p10_15 = np.load(f)
        f.close()
        f = open('./Sequence/T10_16','r')
        self.p10_16 = np.load(f)
        f.close()
        f = open('./Sequence/T10_17','r')
        self.p10_17 = np.load(f)
        f.close()
        f = open('./Sequence/T10_18','r')
        self.p10_18 = np.load(f)
        f.close()
        f = open('./Sequence/T10_19','r')
        self.p10_19 = np.load(f)
        f.close()
        f = open('./Sequence/T10_20','r')
        self.p10_20 = np.load(f)
        f.close()

        f = open('./Sequence/T11_1','r')
        self.p11_1 = np.load(f)
        f.close()
        f = open('./Sequence/T11_2','r')
        self.p11_2 = np.load(f)
        f.close()
        f = open('./Sequence/T11_3','r')
        self.p11_3 = np.load(f)
        f.close()
        f = open('./Sequence/T11_4','r')
        self.p11_4 = np.load(f)
        f.close()
        f = open('./Sequence/T11_5','r')
        self.p11_5 = np.load(f)
        f.close()
        f = open('./Sequence/T11_6','r')
        self.p11_6 = np.load(f)
        f.close()
        f = open('./Sequence/T11_7','r')
        self.p11_7 = np.load(f)
        f.close()
        f = open('./Sequence/T11_8','r')
        self.p11_8 = np.load(f)
        f.close()
        f = open('./Sequence/T11_9','r')
        self.p11_9 = np.load(f)
        f.close()
        f = open('./Sequence/T11_10','r')
        self.p11_10 = np.load(f)
        f.close()
        f = open('./Sequence/T11_11','r')
        self.p11_11 = np.load(f)
        f.close()
        f = open('./Sequence/T11_12','r')
        self.p11_12 = np.load(f)
        f.close()
        f = open('./Sequence/T11_13','r')
        self.p11_13 = np.load(f)
        f.close()
        f = open('./Sequence/T11_14','r')
        self.p11_14 = np.load(f)
        f.close()
        f = open('./Sequence/T11_15','r')
        self.p11_15 = np.load(f)
        f.close()
        f = open('./Sequence/T11_16','r')
        self.p11_16 = np.load(f)
        f.close()
        f = open('./Sequence/T11_17','r')
        self.p11_17 = np.load(f)
        f.close()
        f = open('./Sequence/T11_18','r')
        self.p11_18 = np.load(f)
        f.close()
        f = open('./Sequence/T11_19','r')
        self.p11_19 = np.load(f)
        f.close()
        f = open('./Sequence/T11_20','r')
        self.p11_20 = np.load(f)
        f.close()
      

        f = open('./Sequence/E1_1', 'r')
        self.e1p_1 = np.load(f)
        f.close()
        f = open('./Sequence/E1_2', 'r')
        self.e1p_2 = np.load(f)
        f.close()
        f = open('./Sequence/E1_3', 'r')
        self.e1p_3 = np.load(f)
        f.close()
        f = open('./Sequence/E1_4', 'r')
        self.e1p_4 = np.load(f)
        f.close()
        f = open('./Sequence/E1_5', 'r')
        self.e1p_5 = np.load(f)
        f.close()
        f = open('./Sequence/E1_6', 'r')
        self.e1p_6 = np.load(f)
        f.close()
        f = open('./Sequence/E1_7', 'r')
        self.e1p_7 = np.load(f)
        f.close()
        f = open('./Sequence/E1_8', 'r')
        self.e1p_8 = np.load(f)
        f.close()

        f = open('./Sequence/E2_1', 'r')
        self.e2p_1 = np.load(f)
        f.close()
        f = open('./Sequence/E2_2', 'r')
        self.e2p_2 = np.load(f)
        f.close()
        f = open('./Sequence/E2_3', 'r')
        self.e2p_3 = np.load(f)
        f.close()
        f = open('./Sequence/E2_4', 'r')
        self.e2p_4 = np.load(f)
        f.close()
        f = open('./Sequence/E2_5', 'r')
        self.e2p_5 = np.load(f)
        f.close()
        f = open('./Sequence/E2_6', 'r')
        self.e2p_6 = np.load(f)
        f.close()
        f = open('./Sequence/E2_7', 'r')
        self.e2p_7 = np.load(f)
        f.close()
        f = open('./Sequence/E2_8', 'r')
        self.e2p_8 = np.load(f)
        f.close()

        f = open('./Sequence/E3_1', 'r')
        self.e3p_1 = np.load(f)
        f.close()
        f = open('./Sequence/E3_2', 'r')
        self.e3p_2 = np.load(f)
        f.close()
        f = open('./Sequence/E3_3', 'r')
        self.e3p_3 = np.load(f)
        f.close()
        f = open('./Sequence/E3_4', 'r')
        self.e3p_4 = np.load(f)
        f.close()
        f = open('./Sequence/E3_5', 'r')
        self.e3p_5 = np.load(f)
        f.close()
        f = open('./Sequence/E3_6', 'r')
        self.e3p_6 = np.load(f)
        f.close()
        f = open('./Sequence/E3_7', 'r')
        self.e3p_7 = np.load(f)
        f.close()
        f = open('./Sequence/E3_8', 'r')
        self.e3p_8 = np.load(f)
        f.close()

        f = open('./Sequence/E4_1', 'r')
        self.e4p_1 = np.load(f)
        f.close()
        f = open('./Sequence/E4_2', 'r')
        self.e4p_2 = np.load(f)
        f.close()
        f = open('./Sequence/E4_3', 'r')
        self.e4p_3 = np.load(f)
        f.close()
        f = open('./Sequence/E4_4', 'r')
        self.e4p_4 = np.load(f)
        f.close()
        f = open('./Sequence/E4_5', 'r')
        self.e4p_5 = np.load(f)
        f.close()
        f = open('./Sequence/E4_6', 'r')
        self.e4p_6 = np.load(f)
        f.close()
        f = open('./Sequence/E4_7', 'r')
        self.e4p_7 = np.load(f)
        f.close()
        f = open('./Sequence/E4_8', 'r')
        self.e4p_8 = np.load(f)
        f.close()

        f = open('./Sequence/E5_1', 'r')
        self.e5p_1 = np.load(f)
        f.close()
        f = open('./Sequence/E5_2', 'r')
        self.e5p_2 = np.load(f)
        f.close()
        f = open('./Sequence/E5_3', 'r')
        self.e5p_3 = np.load(f)
        f.close()
        f = open('./Sequence/E5_4', 'r')
        self.e5p_4 = np.load(f)
        f.close()
        f = open('./Sequence/E5_5', 'r')
        self.e5p_5 = np.load(f)
        f.close()
        f = open('./Sequence/E5_6', 'r')
        self.e5p_6 = np.load(f)
        f.close()
        f = open('./Sequence/E5_7', 'r')
        self.e5p_7 = np.load(f)
        f.close()
        f = open('./Sequence/E5_8', 'r')
        self.e5p_8 = np.load(f)
        f.close()

        f = open('./Sequence/E6_1', 'r')
        self.e6p_1 = np.load(f)
        f.close()
        f = open('./Sequence/E6_2', 'r')
        self.e6p_2 = np.load(f)
        f.close()
        f = open('./Sequence/E6_3', 'r')
        self.e6p_3 = np.load(f)
        f.close()
        f = open('./Sequence/E6_4', 'r')
        self.e6p_4 = np.load(f)
        f.close()
        f = open('./Sequence/E6_5', 'r')
        self.e6p_5 = np.load(f)
        f.close()
        f = open('./Sequence/E6_6', 'r')
        self.e6p_6 = np.load(f)
        f.close()
        f = open('./Sequence/E6_7', 'r')
        self.e6p_7 = np.load(f)
        f.close()
        f = open('./Sequence/E6_8', 'r')
        self.e6p_8 = np.load(f)
        f.close()

        f = open('./Sequence/E7_1', 'r')
        self.e7p_1 = np.load(f)
        f.close()
        f = open('./Sequence/E7_2', 'r')
        self.e7p_2 = np.load(f)
        f.close()
        f = open('./Sequence/E7_3', 'r')
        self.e7p_3 = np.load(f)
        f.close()
        f = open('./Sequence/E7_4', 'r')
        self.e7p_4 = np.load(f)
        f.close()
        f = open('./Sequence/E7_5', 'r')
        self.e7p_5 = np.load(f)
        f.close()
        f = open('./Sequence/E7_6', 'r')
        self.e7p_6 = np.load(f)
        f.close()
        f = open('./Sequence/E7_7', 'r')
        self.e7p_7 = np.load(f)
        f.close()
        f = open('./Sequence/E7_8', 'r')
        self.e7p_8 = np.load(f)
        f.close()

        f = open('./Sequence/E8_1', 'r')
        self.e8p_1 = np.load(f)
        f.close()
        f = open('./Sequence/E8_2', 'r')
        self.e8p_2 = np.load(f)
        f.close()
        f = open('./Sequence/E8_3', 'r')
        self.e8p_3 = np.load(f)
        f.close()
        f = open('./Sequence/E8_4', 'r')
        self.e8p_4 = np.load(f)
        f.close()
        f = open('./Sequence/E8_5', 'r')
        self.e8p_5 = np.load(f)
        f.close()
        f = open('./Sequence/E8_6', 'r')
        self.e8p_6 = np.load(f)
        f.close()
        f = open('./Sequence/E8_7', 'r')
        self.e8p_7 = np.load(f)
        f.close()
        f = open('./Sequence/E8_8', 'r')
        self.e8p_8 = np.load(f)
        f.close()

        f = open('./Sequence/E9_1', 'r')
        self.e9p_1 = np.load(f)
        f.close()
        f = open('./Sequence/E9_2', 'r')
        self.e9p_2 = np.load(f)
        f.close()
        f = open('./Sequence/E9_3', 'r')
        self.e9p_3 = np.load(f)
        f.close()
        f = open('./Sequence/E9_4', 'r')
        self.e9p_4 = np.load(f)
        f.close()
        f = open('./Sequence/E9_5', 'r')
        self.e9p_5 = np.load(f)
        f.close()
        f = open('./Sequence/E9_6', 'r')
        self.e9p_6 = np.load(f)
        f.close()
        f = open('./Sequence/E9_7', 'r')
        self.e9p_7 = np.load(f)
        f.close()
        f = open('./Sequence/E9_8', 'r')
        self.e9p_8 = np.load(f)
        f.close()

        f = open('./Sequence/E10_1', 'r')
        self.e10p_1 = np.load(f)
        f.close()
        f = open('./Sequence/E10_2', 'r')
        self.e10p_2 = np.load(f)
        f.close()
        f = open('./Sequence/E10_3', 'r')
        self.e10p_3 = np.load(f)
        f.close()
        f = open('./Sequence/E10_4', 'r')
        self.e10p_4 = np.load(f)
        f.close()
        f = open('./Sequence/E10_5', 'r')
        self.e10p_5 = np.load(f)
        f.close()
        f = open('./Sequence/E10_6', 'r')
        self.e10p_6 = np.load(f)
        f.close()
        f = open('./Sequence/E10_7', 'r')
        self.e10p_7 = np.load(f)
        f.close()
        f = open('./Sequence/E10_8', 'r')
        self.e10p_8 = np.load(f)
        f.close()

        f = open('./Sequence/E11_1', 'r')
        self.e11p_1 = np.load(f)
        f.close()
        f = open('./Sequence/E11_2', 'r')
        self.e11p_2 = np.load(f)
        f.close()
        f = open('./Sequence/E11_3', 'r')
        self.e11p_3 = np.load(f)
        f.close()
        f = open('./Sequence/E11_4', 'r')
        self.e11p_4 = np.load(f)
        f.close()
        f = open('./Sequence/E11_5', 'r')
        self.e11p_5 = np.load(f)
        f.close()
        f = open('./Sequence/E11_6', 'r')
        self.e11p_6 = np.load(f)
        f.close()
        f = open('./Sequence/E11_7', 'r')
        self.e11p_7 = np.load(f)
        f.close()
        f = open('./Sequence/E11_8', 'r')
        self.e11p_8 = np.load(f)
        f.close()

    def single_stages(self):
        print "Computing Single Stages..."
        d1 = min(len(self.p1_1),len(self.p1_2),len(self.p1_3),len(self.p1_4),len(self.p1_5),len(self.p1_6),len(self.p1_7),len(self.p1_8),len(self.p1_9),len(self.p1_10),len(self.p1_11),len(self.p1_12),len(self.p1_13),len(self.p1_14),len(self.p1_15),len(self.p1_16),len(self.p1_17),len(self.p1_18),len(self.p1_19),len(self.p1_20))
        d2 = min(len(self.p2_1),len(self.p2_2),len(self.p2_3),len(self.p2_4),len(self.p2_5),len(self.p2_6),len(self.p2_7),len(self.p2_8),len(self.p2_9),len(self.p2_10),len(self.p2_11),len(self.p2_12),len(self.p2_13),len(self.p2_14),len(self.p2_15),len(self.p2_6),len(self.p2_17),len(self.p2_18),len(self.p2_19),len(self.p2_20))
        d3 = min(len(self.p3_1),len(self.p3_2),len(self.p3_3),len(self.p3_4),len(self.p3_5),len(self.p3_6),len(self.p3_7),len(self.p3_8),len(self.p3_9),len(self.p3_10),len(self.p3_11),len(self.p3_12),len(self.p3_13),len(self.p3_14),len(self.p3_15),len(self.p3_16),len(self.p3_17),len(self.p3_18),len(self.p3_19),len(self.p3_20))
        d4 = min(len(self.p4_1),len(self.p4_2),len(self.p4_3),len(self.p4_4),len(self.p4_5),len(self.p4_6),len(self.p4_7),len(self.p4_8),len(self.p4_9),len(self.p4_10),len(self.p4_11),len(self.p4_12),len(self.p4_13),len(self.p4_14),len(self.p4_15),len(self.p4_16),len(self.p4_17),len(self.p4_18),len(self.p4_19),len(self.p4_20))
        d5 = min(len(self.p5_1),len(self.p5_2),len(self.p5_3),len(self.p5_4),len(self.p5_5),len(self.p5_6),len(self.p5_7),len(self.p5_8),len(self.p5_9),len(self.p5_10),len(self.p5_11),len(self.p5_12),len(self.p5_13),len(self.p5_14),len(self.p5_15),len(self.p5_16),len(self.p5_17),len(self.p5_18),len(self.p5_19),len(self.p5_20))
        d6 = min(len(self.p6_1),len(self.p6_2),len(self.p6_3),len(self.p6_4),len(self.p6_5),len(self.p6_6),len(self.p6_7),len(self.p6_8),len(self.p6_9),len(self.p6_10),len(self.p6_11),len(self.p6_12),len(self.p6_13),len(self.p6_14),len(self.p6_15),len(self.p6_16),len(self.p6_17),len(self.p6_18),len(self.p6_19),len(self.p6_20))
        d7 = min(len(self.p7_1),len(self.p7_2),len(self.p7_3),len(self.p7_4),len(self.p7_5),len(self.p7_6),len(self.p7_7),len(self.p7_8),len(self.p7_9),len(self.p7_10),len(self.p7_11),len(self.p7_12),len(self.p7_13),len(self.p7_14),len(self.p7_15),len(self.p7_16),len(self.p7_17),len(self.p7_18),len(self.p7_19),len(self.p7_20))
        d8 = min(len(self.p8_1),len(self.p8_2),len(self.p8_3),len(self.p8_4),len(self.p8_5),len(self.p8_6),len(self.p8_7),len(self.p8_8),len(self.p8_9),len(self.p8_10),len(self.p8_11),len(self.p8_12),len(self.p8_13),len(self.p8_14),len(self.p8_15),len(self.p8_16),len(self.p8_17),len(self.p8_18),len(self.p8_19),len(self.p8_20))
        d9 = min(len(self.p9_1),len(self.p9_2),len(self.p9_3),len(self.p9_4),len(self.p9_5),len(self.p9_6),len(self.p9_7),len(self.p9_8),len(self.p9_9),len(self.p9_10),len(self.p9_11),len(self.p9_12),len(self.p9_13),len(self.p9_14),len(self.p9_15),len(self.p9_16),len(self.p9_17),len(self.p9_18),len(self.p9_19),len(self.p9_20))
        d10 = min(len(self.p10_1),len(self.p10_2),len(self.p10_3),len(self.p10_4),len(self.p10_5),len(self.p10_6),len(self.p10_7),len(self.p10_8),len(self.p10_9),len(self.p10_10),len(self.p10_11),len(self.p10_12),len(self.p10_13),len(self.p10_14),len(self.p10_15),len(self.p10_16),len(self.p10_17),len(self.p10_18),len(self.p10_19),len(self.p10_20))
        d11 = min(len(self.p11_1),len(self.p11_2),len(self.p11_3),len(self.p11_4),len(self.p11_5),len(self.p11_6),len(self.p11_7),len(self.p11_8),len(self.p11_9),len(self.p11_10),len(self.p11_11),len(self.p11_12),len(self.p11_13),len(self.p11_14),len(self.p11_15),len(self.p11_16),len(self.p11_17),len(self.p11_18),len(self.p11_19),len(self.p11_20))
        j = 1
        self.ss_1 = np.zeros((4,d1/5+1))
        print "Stage 1"
        for i in range(0,d1):
            if (i % 5) == 0:
              if j == 1:
                  self.ss_1[0][i/5] = self.p1_1[i][0]
                  self.ss_1[1][i/5] = self.p1_1[i][1]
                  self.ss_1[2][i/5] = self.p1_1[i][2]
                  self.ss_1[3][i/5] = self.p1_1[i][3]
              elif j == 2:
                  self.ss_1[0][i/5] = self.p1_2[i][0]
                  self.ss_1[1][i/5] = self.p1_2[i][1]
                  self.ss_1[2][i/5] = self.p1_2[i][2]
                  self.ss_1[3][i/5] = self.p1_2[i][3]
              elif j == 3:
                  self.ss_1[0][i/5] = self.p1_3[i][0]
                  self.ss_1[1][i/5] = self.p1_3[i][1]
                  self.ss_1[2][i/5] = self.p1_3[i][2]
                  self.ss_1[3][i/5] = self.p1_3[i][3]
              elif j == 4:
                  self.ss_1[0][i/5] = self.p1_4[i][0]
                  self.ss_1[1][i/5] = self.p1_4[i][1]
                  self.ss_1[2][i/5] = self.p1_4[i][2]
                  self.ss_1[3][i/5] = self.p1_4[i][3]
              elif j == 5:
                  self.ss_1[0][i/5] = self.p1_5[i][0]
                  self.ss_1[1][i/5] = self.p1_5[i][1]
                  self.ss_1[2][i/5] = self.p1_5[i][2]
                  self.ss_1[3][i/5] = self.p1_5[i][3]
              elif j == 6:
                  self.ss_1[0][i/5] = self.p1_6[i][0]
                  self.ss_1[1][i/5] = self.p1_6[i][1]
                  self.ss_1[2][i/5] = self.p1_6[i][2]
                  self.ss_1[3][i/5] = self.p1_6[i][3]
              elif j == 7:
                  self.ss_1[0][i/5] = self.p1_7[i][0]
                  self.ss_1[1][i/5] = self.p1_7[i][1]
                  self.ss_1[2][i/5] = self.p1_7[i][2]
                  self.ss_1[3][i/5] = self.p1_7[i][3]
              elif j == 8:
                  self.ss_1[0][i/5] = self.p1_8[i][0]
                  self.ss_1[1][i/5] = self.p1_8[i][1]
                  self.ss_1[2][i/5] = self.p1_8[i][2]
                  self.ss_1[3][i/5] = self.p1_8[i][3]
              elif j == 9:
                  self.ss_1[0][i/5] = self.p1_9[i][0]
                  self.ss_1[1][i/5] = self.p1_9[i][1]
                  self.ss_1[2][i/5] = self.p1_9[i][2]
                  self.ss_1[3][i/5] = self.p1_9[i][3]
              elif j == 10:
                  self.ss_1[0][i/5] = self.p1_10[i][0]
                  self.ss_1[1][i/5] = self.p1_10[i][1]
                  self.ss_1[2][i/5] = self.p1_10[i][2]
                  self.ss_1[3][i/5] = self.p1_10[i][3]
              if j == 11:
                  self.ss_1[0][i/5] = self.p1_11[i][0]
                  self.ss_1[1][i/5] = self.p1_11[i][1]
                  self.ss_1[2][i/5] = self.p1_11[i][2]
                  self.ss_1[3][i/5] = self.p1_11[i][3]
              elif j == 12:
                  self.ss_1[0][i/5] = self.p1_12[i][0]
                  self.ss_1[1][i/5] = self.p1_12[i][1]
                  self.ss_1[2][i/5] = self.p1_12[i][2]
                  self.ss_1[3][i/5] = self.p1_12[i][3]
              elif j == 13:
                  self.ss_1[0][i/5] = self.p1_13[i][0]
                  self.ss_1[1][i/5] = self.p1_13[i][1]
                  self.ss_1[2][i/5] = self.p1_13[i][2]
                  self.ss_1[3][i/5] = self.p1_13[i][3]
              elif j == 14:
                  self.ss_1[0][i/5] = self.p1_14[i][0]
                  self.ss_1[1][i/5] = self.p1_14[i][1]
                  self.ss_1[2][i/5] = self.p1_14[i][2]
                  self.ss_1[3][i/5] = self.p1_14[i][3]
              elif j == 15:
                  self.ss_1[0][i/5] = self.p1_15[i][0]
                  self.ss_1[1][i/5] = self.p1_15[i][1]
                  self.ss_1[2][i/5] = self.p1_15[i][2]
                  self.ss_1[3][i/5] = self.p1_15[i][3]
              elif j == 16:
                  self.ss_1[0][i/5] = self.p1_16[i][0]
                  self.ss_1[1][i/5] = self.p1_16[i][1]
                  self.ss_1[2][i/5] = self.p1_16[i][2]
                  self.ss_1[3][i/5] = self.p1_16[i][3]
              elif j == 17:
                  self.ss_1[0][i/5] = self.p1_17[i][0]
                  self.ss_1[1][i/5] = self.p1_17[i][1]
                  self.ss_1[2][i/5] = self.p1_17[i][2]
                  self.ss_1[3][i/5] = self.p1_17[i][3]
              elif j == 18:
                  self.ss_1[0][i/5] = self.p1_18[i][0]
                  self.ss_1[1][i/5] = self.p1_18[i][1]
                  self.ss_1[2][i/5] = self.p1_18[i][2]
                  self.ss_1[3][i/5] = self.p1_18[i][3]
              elif j == 19:
                  self.ss_1[0][i/5] = self.p1_19[i][0]
                  self.ss_1[1][i/5] = self.p1_19[i][1]
                  self.ss_1[2][i/5] = self.p1_19[i][2]
                  self.ss_1[3][i/5] = self.p1_19[i][3]
              elif j == 20:
                  self.ss_1[0][i/5] = self.p1_20[i][0]
                  self.ss_1[1][i/5] = self.p1_20[i][1]
                  self.ss_1[2][i/5] = self.p1_20[i][2]
                  self.ss_1[3][i/5] = self.p1_20[i][3]
                  j = 0
              j = j + 1

        j = 1
        self.ss_2 = np.zeros((4,d2/5+1))
        print "Stage 2"
        for i in range(0,d2):
            if (i % 5) == 0:
              if j == 1:
                  self.ss_2[0][i/5] = self.p2_1[i][0]
                  self.ss_2[1][i/5] = self.p2_1[i][1]
                  self.ss_2[2][i/5] = self.p2_1[i][2]
                  self.ss_2[3][i/5] = self.p2_1[i][3]
              elif j == 2:
                  self.ss_2[0][i/5] = self.p2_2[i][0]
                  self.ss_2[1][i/5] = self.p2_2[i][1]
                  self.ss_2[2][i/5] = self.p2_2[i][2]
                  self.ss_2[3][i/5] = self.p2_2[i][3]
              elif j == 3:
                  self.ss_2[0][i/5] = self.p2_3[i][0]
                  self.ss_2[1][i/5] = self.p2_3[i][1]
                  self.ss_2[2][i/5] = self.p2_3[i][2]
                  self.ss_2[3][i/5] = self.p2_3[i][3]
              elif j == 4:
                  self.ss_2[0][i/5] = self.p2_4[i][0]
                  self.ss_2[1][i/5] = self.p2_4[i][1]
                  self.ss_2[2][i/5] = self.p2_4[i][2]
                  self.ss_2[3][i/5] = self.p2_4[i][3]
              elif j == 5:
                  self.ss_2[0][i/5] = self.p2_5[i][0]
                  self.ss_2[1][i/5] = self.p2_5[i][1]
                  self.ss_2[2][i/5] = self.p2_5[i][2]
                  self.ss_2[3][i/5] = self.p2_5[i][3]
              elif j == 6:
                  self.ss_2[0][i/5] = self.p2_6[i][0]
                  self.ss_2[1][i/5] = self.p2_6[i][1]
                  self.ss_2[2][i/5] = self.p2_6[i][2]
                  self.ss_2[3][i/5] = self.p2_6[i][3]
              elif j == 7:
                  self.ss_2[0][i/5] = self.p2_7[i][0]
                  self.ss_2[1][i/5] = self.p2_7[i][1]
                  self.ss_2[2][i/5] = self.p2_7[i][2]
                  self.ss_2[3][i/5] = self.p2_7[i][3]
              elif j == 8:
                  self.ss_2[0][i/5] = self.p2_8[i][0]
                  self.ss_2[1][i/5] = self.p2_8[i][1]
                  self.ss_2[2][i/5] = self.p2_8[i][2]
                  self.ss_2[3][i/5] = self.p2_8[i][3]
              elif j == 9:
                  self.ss_2[0][i/5] = self.p2_9[i][0]
                  self.ss_2[1][i/5] = self.p2_9[i][1]
                  self.ss_2[2][i/5] = self.p2_9[i][2]
                  self.ss_2[3][i/5] = self.p2_9[i][3]
              elif j == 10:
                  self.ss_2[0][i/5] = self.p2_10[i][0]
                  self.ss_2[1][i/5] = self.p2_10[i][1]
                  self.ss_2[2][i/5] = self.p2_10[i][2]
                  self.ss_2[3][i/5] = self.p2_10[i][3]

              if j == 11:
                  self.ss_2[0][i/5] = self.p2_11[i][0]
                  self.ss_2[1][i/5] = self.p2_11[i][1]
                  self.ss_2[2][i/5] = self.p2_11[i][2]
                  self.ss_2[3][i/5] = self.p2_11[i][3]
              elif j == 12:
                  self.ss_2[0][i/5] = self.p2_12[i][0]
                  self.ss_2[1][i/5] = self.p2_12[i][1]
                  self.ss_2[2][i/5] = self.p2_12[i][2]
                  self.ss_2[3][i/5] = self.p2_12[i][3]
              elif j == 13:
                  self.ss_2[0][i/5] = self.p2_13[i][0]
                  self.ss_2[1][i/5] = self.p2_13[i][1]
                  self.ss_2[2][i/5] = self.p2_13[i][2]
                  self.ss_2[3][i/5] = self.p2_13[i][3]
              elif j == 14:
                  self.ss_2[0][i/5] = self.p2_14[i][0]
                  self.ss_2[1][i/5] = self.p2_14[i][1]
                  self.ss_2[2][i/5] = self.p2_14[i][2]
                  self.ss_2[3][i/5] = self.p2_14[i][3]
              elif j == 15:
                  self.ss_2[0][i/5] = self.p2_15[i][0]
                  self.ss_2[1][i/5] = self.p2_15[i][1]
                  self.ss_2[2][i/5] = self.p2_15[i][2]
                  self.ss_2[3][i/5] = self.p2_15[i][3]
              elif j == 16:
                  self.ss_2[0][i/5] = self.p2_16[i][0]
                  self.ss_2[1][i/5] = self.p2_16[i][1]
                  self.ss_2[2][i/5] = self.p2_16[i][2]
                  self.ss_2[3][i/5] = self.p2_16[i][3]
              elif j == 17:
                  self.ss_2[0][i/5] = self.p2_17[i][0]
                  self.ss_2[1][i/5] = self.p2_17[i][1]
                  self.ss_2[2][i/5] = self.p2_17[i][2]
                  self.ss_2[3][i/5] = self.p2_17[i][3]
              elif j == 18:
                  self.ss_2[0][i/5] = self.p2_18[i][0]
                  self.ss_2[1][i/5] = self.p2_18[i][1]
                  self.ss_2[2][i/5] = self.p2_18[i][2]
                  self.ss_2[3][i/5] = self.p2_18[i][3]
              elif j == 19:
                  self.ss_2[0][i/5] = self.p2_19[i][0]
                  self.ss_2[1][i/5] = self.p2_19[i][1]
                  self.ss_2[2][i/5] = self.p2_19[i][2]
                  self.ss_2[3][i/5] = self.p2_19[i][3]
              elif j == 20:
                  self.ss_2[0][i/5] = self.p2_20[i][0]
                  self.ss_2[1][i/5] = self.p2_20[i][1]
                  self.ss_2[2][i/5] = self.p2_20[i][2]
                  self.ss_2[3][i/5] = self.p2_20[i][3]
                  j = 0
              j = j + 1

        j = 1
        self.ss_3 = np.zeros((4,d3/5+1))
        print "Stage 3"
        for i in range(0,d3):
            if (i % 5) == 0:
              if j == 1:
                  self.ss_3[0][i/5] = self.p3_1[i][0]
                  self.ss_3[1][i/5] = self.p3_1[i][1]
                  self.ss_3[2][i/5] = self.p3_1[i][2]
                  self.ss_3[3][i/5] = self.p3_1[i][3]
              elif j == 2:
                  self.ss_3[0][i/5] = self.p3_2[i][0]
                  self.ss_3[1][i/5] = self.p3_2[i][1]
                  self.ss_3[2][i/5] = self.p3_2[i][2]
                  self.ss_3[3][i/5] = self.p3_2[i][3]
              elif j == 3:
                  self.ss_3[0][i/5] = self.p3_3[i][0]
                  self.ss_3[1][i/5] = self.p3_3[i][1]
                  self.ss_3[2][i/5] = self.p3_3[i][2]
                  self.ss_3[3][i/5] = self.p3_3[i][3]
              elif j == 4:
                  self.ss_3[0][i/5] = self.p3_4[i][0]
                  self.ss_3[1][i/5] = self.p3_4[i][1]
                  self.ss_3[2][i/5] = self.p3_4[i][2]
                  self.ss_3[3][i/5] = self.p3_4[i][3]
              elif j == 5:
                  self.ss_3[0][i/5] = self.p3_5[i][0]
                  self.ss_3[1][i/5] = self.p3_5[i][1]
                  self.ss_3[2][i/5] = self.p3_5[i][2]
                  self.ss_3[3][i/5] = self.p3_5[i][3]
              elif j == 6:
                  self.ss_3[0][i/5] = self.p3_6[i][0]
                  self.ss_3[1][i/5] = self.p3_6[i][1]
                  self.ss_3[2][i/5] = self.p3_6[i][2]
                  self.ss_3[3][i/5] = self.p3_6[i][3]
              elif j == 7:
                  self.ss_3[0][i/5] = self.p3_7[i][0]
                  self.ss_3[1][i/5] = self.p3_7[i][1]
                  self.ss_3[2][i/5] = self.p3_7[i][2]
                  self.ss_3[3][i/5] = self.p3_7[i][3]
              elif j == 8:
                  self.ss_3[0][i/5] = self.p3_8[i][0]
                  self.ss_3[1][i/5] = self.p3_8[i][1]
                  self.ss_3[2][i/5] = self.p3_8[i][2]
                  self.ss_3[3][i/5] = self.p3_8[i][3]
              elif j == 9:
                  self.ss_3[0][i/5] = self.p3_9[i][0]
                  self.ss_3[1][i/5] = self.p3_9[i][1]
                  self.ss_3[2][i/5] = self.p3_9[i][2]
                  self.ss_3[3][i/5] = self.p3_9[i][3]
              elif j == 10:
                  self.ss_3[0][i/5] = self.p3_10[i][0]
                  self.ss_3[1][i/5] = self.p3_10[i][1]
                  self.ss_3[2][i/5] = self.p3_10[i][2]
                  self.ss_3[3][i/5] = self.p3_10[i][3]

              if j == 11:
                  self.ss_3[0][i/5] = self.p3_11[i][0]
                  self.ss_3[1][i/5] = self.p3_11[i][1]
                  self.ss_3[2][i/5] = self.p3_11[i][2]
                  self.ss_3[3][i/5] = self.p3_11[i][3]
              elif j == 12:
                  self.ss_3[0][i/5] = self.p3_12[i][0]
                  self.ss_3[1][i/5] = self.p3_12[i][1]
                  self.ss_3[2][i/5] = self.p3_12[i][2]
                  self.ss_3[3][i/5] = self.p3_12[i][3]
              elif j == 13:
                  self.ss_3[0][i/5] = self.p3_13[i][0]
                  self.ss_3[1][i/5] = self.p3_13[i][1]
                  self.ss_3[2][i/5] = self.p3_13[i][2]
                  self.ss_3[3][i/5] = self.p3_13[i][3]
              elif j == 14:
                  self.ss_3[0][i/5] = self.p3_14[i][0]
                  self.ss_3[1][i/5] = self.p3_14[i][1]
                  self.ss_3[2][i/5] = self.p3_14[i][2]
                  self.ss_3[3][i/5] = self.p3_14[i][3]
              elif j == 15:
                  self.ss_3[0][i/5] = self.p3_15[i][0]
                  self.ss_3[1][i/5] = self.p3_15[i][1]
                  self.ss_3[2][i/5] = self.p3_15[i][2]
                  self.ss_3[3][i/5] = self.p3_15[i][3]
              elif j == 16:
                  self.ss_3[0][i/5] = self.p3_16[i][0]
                  self.ss_3[1][i/5] = self.p3_16[i][1]
                  self.ss_3[2][i/5] = self.p3_16[i][2]
                  self.ss_3[3][i/5] = self.p3_16[i][3]
              elif j == 17:
                  self.ss_3[0][i/5] = self.p3_17[i][0]
                  self.ss_3[1][i/5] = self.p3_17[i][1]
                  self.ss_3[2][i/5] = self.p3_17[i][2]
                  self.ss_3[3][i/5] = self.p3_17[i][3]
              elif j == 18:
                  self.ss_3[0][i/5] = self.p3_18[i][0]
                  self.ss_3[1][i/5] = self.p3_18[i][1]
                  self.ss_3[2][i/5] = self.p3_18[i][2]
                  self.ss_3[3][i/5] = self.p3_18[i][3]
              elif j == 19:
                  self.ss_3[0][i/5] = self.p3_19[i][0]
                  self.ss_3[1][i/5] = self.p3_19[i][1]
                  self.ss_3[2][i/5] = self.p3_19[i][2]
                  self.ss_3[3][i/5] = self.p3_19[i][3]
              elif j == 20:
                  self.ss_3[0][i/5] = self.p3_20[i][0]
                  self.ss_3[1][i/5] = self.p3_20[i][1]
                  self.ss_3[2][i/5] = self.p3_20[i][2]
                  self.ss_3[3][i/5] = self.p3_20[i][3]
                  j = 0
              j = j + 1

        j = 1
        self.ss_4 = np.zeros((4,d4/5+1))
        print "Stage 4"
        for i in range(0,d4):
            if (i % 5) == 0:
              if j == 1:
                  self.ss_4[0][i/5] = self.p4_1[i][0]
                  self.ss_4[1][i/5] = self.p4_1[i][1]
                  self.ss_4[2][i/5] = self.p4_1[i][2]
                  self.ss_4[3][i/5] = self.p4_1[i][3]
              elif j == 2:
                  self.ss_4[0][i/5] = self.p4_2[i][0]
                  self.ss_4[1][i/5] = self.p4_2[i][1]
                  self.ss_4[2][i/5] = self.p4_2[i][2]
                  self.ss_4[3][i/5] = self.p4_2[i][3]
              elif j == 3:
                  self.ss_4[0][i/5] = self.p4_3[i][0]
                  self.ss_4[1][i/5] = self.p4_3[i][1]
                  self.ss_4[2][i/5] = self.p4_3[i][2]
                  self.ss_4[3][i/5] = self.p4_3[i][3]
              elif j == 4:
                  self.ss_4[0][i/5] = self.p4_4[i][0]
                  self.ss_4[1][i/5] = self.p4_4[i][1]
                  self.ss_4[2][i/5] = self.p4_4[i][2]
                  self.ss_4[3][i/5] = self.p4_4[i][3]
              elif j == 5:
                  self.ss_4[0][i/5] = self.p4_5[i][0]
                  self.ss_4[1][i/5] = self.p4_5[i][1]
                  self.ss_4[2][i/5] = self.p4_5[i][2]
                  self.ss_4[3][i/5] = self.p4_5[i][3]
              elif j == 6:
                  self.ss_4[0][i/5] = self.p4_6[i][0]
                  self.ss_4[1][i/5] = self.p4_6[i][1]
                  self.ss_4[2][i/5] = self.p4_6[i][2]
                  self.ss_4[3][i/5] = self.p4_6[i][3]
              elif j == 7:
                  self.ss_4[0][i/5] = self.p4_7[i][0]
                  self.ss_4[1][i/5] = self.p4_7[i][1]
                  self.ss_4[2][i/5] = self.p4_7[i][2]
                  self.ss_4[3][i/5] = self.p4_7[i][3]
              elif j == 8:
                  self.ss_4[0][i/5] = self.p4_8[i][0]
                  self.ss_4[1][i/5] = self.p4_8[i][1]
                  self.ss_4[2][i/5] = self.p4_8[i][2]
                  self.ss_4[3][i/5] = self.p4_8[i][3]
              elif j == 9:
                  self.ss_4[0][i/5] = self.p4_9[i][0]
                  self.ss_4[1][i/5] = self.p4_9[i][1]
                  self.ss_4[2][i/5] = self.p4_9[i][2]
                  self.ss_4[3][i/5] = self.p4_9[i][3]
              elif j == 10:
                  self.ss_4[0][i/5] = self.p4_10[i][0]
                  self.ss_4[1][i/5] = self.p4_10[i][1]
                  self.ss_4[2][i/5] = self.p4_10[i][2]
                  self.ss_4[3][i/5] = self.p4_10[i][3]

              if j == 11:
                  self.ss_4[0][i/5] = self.p4_11[i][0]
                  self.ss_4[1][i/5] = self.p4_11[i][1]
                  self.ss_4[2][i/5] = self.p4_11[i][2]
                  self.ss_4[3][i/5] = self.p4_11[i][3]
              elif j == 12:
                  self.ss_4[0][i/5] = self.p4_12[i][0]
                  self.ss_4[1][i/5] = self.p4_12[i][1]
                  self.ss_4[2][i/5] = self.p4_12[i][2]
                  self.ss_4[3][i/5] = self.p4_12[i][3]
              elif j == 13:
                  self.ss_4[0][i/5] = self.p4_13[i][0]
                  self.ss_4[1][i/5] = self.p4_13[i][1]
                  self.ss_4[2][i/5] = self.p4_13[i][2]
                  self.ss_4[3][i/5] = self.p4_13[i][3]
              elif j == 14:
                  self.ss_4[0][i/5] = self.p4_14[i][0]
                  self.ss_4[1][i/5] = self.p4_14[i][1]
                  self.ss_4[2][i/5] = self.p4_14[i][2]
                  self.ss_4[3][i/5] = self.p4_14[i][3]
              elif j == 15:
                  self.ss_4[0][i/5] = self.p4_15[i][0]
                  self.ss_4[1][i/5] = self.p4_15[i][1]
                  self.ss_4[2][i/5] = self.p4_15[i][2]
                  self.ss_4[3][i/5] = self.p4_15[i][3]
              elif j == 16:
                  self.ss_4[0][i/5] = self.p4_16[i][0]
                  self.ss_4[1][i/5] = self.p4_16[i][1]
                  self.ss_4[2][i/5] = self.p4_16[i][2]
                  self.ss_4[3][i/5] = self.p4_16[i][3]
              elif j == 17:
                  self.ss_4[0][i/5] = self.p4_17[i][0]
                  self.ss_4[1][i/5] = self.p4_17[i][1]
                  self.ss_4[2][i/5] = self.p4_17[i][2]
                  self.ss_4[3][i/5] = self.p4_17[i][3]
              elif j == 18:
                  self.ss_4[0][i/5] = self.p4_18[i][0]
                  self.ss_4[1][i/5] = self.p4_18[i][1]
                  self.ss_4[2][i/5] = self.p4_18[i][2]
                  self.ss_4[3][i/5] = self.p4_18[i][3]
              elif j == 19:
                  self.ss_4[0][i/5] = self.p4_19[i][0]
                  self.ss_4[1][i/5] = self.p4_19[i][1]
                  self.ss_4[2][i/5] = self.p4_19[i][2]
                  self.ss_4[3][i/5] = self.p4_19[i][3]
              elif j == 20:
                  self.ss_4[0][i/5] = self.p4_20[i][0]
                  self.ss_4[1][i/5] = self.p4_20[i][1]
                  self.ss_4[2][i/5] = self.p4_20[i][2]
                  self.ss_4[3][i/5] = self.p4_20[i][3]
                  j = 0
              j = j + 1
        j = 1

        self.ss_5 = np.zeros((4,d5/5+1))
        print "Stage 5"
        for i in range(0,d5):
            if (i % 5) == 0:
              if j == 1:
                  self.ss_5[0][i/5] = self.p5_1[i][0]
                  self.ss_5[1][i/5] = self.p5_1[i][1]
                  self.ss_5[2][i/5] = self.p5_1[i][2]
                  self.ss_5[3][i/5] = self.p5_1[i][3]
              elif j == 2:
                  self.ss_5[0][i/5] = self.p5_2[i][0]
                  self.ss_5[1][i/5] = self.p5_2[i][1]
                  self.ss_5[2][i/5] = self.p5_2[i][2]
                  self.ss_5[3][i/5] = self.p5_2[i][3]
              elif j == 3:
                  self.ss_5[0][i/5] = self.p5_3[i][0]
                  self.ss_5[1][i/5] = self.p5_3[i][1]
                  self.ss_5[2][i/5] = self.p5_3[i][2]
                  self.ss_5[3][i/5] = self.p5_3[i][3]
              elif j == 4:
                  self.ss_5[0][i/5] = self.p5_4[i][0]
                  self.ss_5[1][i/5] = self.p5_4[i][1]
                  self.ss_5[2][i/5] = self.p5_4[i][2]
                  self.ss_5[3][i/5] = self.p5_4[i][3]
              elif j == 5:
                  self.ss_5[0][i/5] = self.p5_5[i][0]
                  self.ss_5[1][i/5] = self.p5_5[i][1]
                  self.ss_5[2][i/5] = self.p5_5[i][2]
                  self.ss_5[3][i/5] = self.p5_5[i][3]
              elif j == 6:
                  self.ss_5[0][i/5] = self.p5_6[i][0]
                  self.ss_5[1][i/5] = self.p5_6[i][1]
                  self.ss_5[2][i/5] = self.p5_6[i][2]
                  self.ss_5[3][i/5] = self.p5_6[i][3]
              elif j == 7:
                  self.ss_5[0][i/5] = self.p5_7[i][0]
                  self.ss_5[1][i/5] = self.p5_7[i][1]
                  self.ss_5[2][i/5] = self.p5_7[i][2]
                  self.ss_5[3][i/5] = self.p5_7[i][3]
              elif j == 8:
                  self.ss_5[0][i/5] = self.p5_8[i][0]
                  self.ss_5[1][i/5] = self.p5_8[i][1]
                  self.ss_5[2][i/5] = self.p5_8[i][2]
                  self.ss_5[3][i/5] = self.p5_8[i][3]
              elif j == 9:
                  self.ss_5[0][i/5] = self.p5_9[i][0]
                  self.ss_5[1][i/5] = self.p5_9[i][1]
                  self.ss_5[2][i/5] = self.p5_9[i][2]
                  self.ss_5[3][i/5] = self.p5_9[i][3]
              elif j == 10:
                  self.ss_5[0][i/5] = self.p5_10[i][0]
                  self.ss_5[1][i/5] = self.p5_10[i][1]
                  self.ss_5[2][i/5] = self.p5_10[i][2]
                  self.ss_5[3][i/5] = self.p5_10[i][3]

              if j == 11:
                  self.ss_5[0][i/5] = self.p5_11[i][0]
                  self.ss_5[1][i/5] = self.p5_11[i][1]
                  self.ss_5[2][i/5] = self.p5_11[i][2]
                  self.ss_5[3][i/5] = self.p5_11[i][3]
              elif j == 12:
                  self.ss_5[0][i/5] = self.p5_12[i][0]
                  self.ss_5[1][i/5] = self.p5_12[i][1]
                  self.ss_5[2][i/5] = self.p5_12[i][2]
                  self.ss_5[3][i/5] = self.p5_12[i][3]
              elif j == 13:
                  self.ss_5[0][i/5] = self.p5_13[i][0]
                  self.ss_5[1][i/5] = self.p5_13[i][1]
                  self.ss_5[2][i/5] = self.p5_13[i][2]
                  self.ss_5[3][i/5] = self.p5_13[i][3]
              elif j == 14:
                  self.ss_5[0][i/5] = self.p5_14[i][0]
                  self.ss_5[1][i/5] = self.p5_14[i][1]
                  self.ss_5[2][i/5] = self.p5_14[i][2]
                  self.ss_5[3][i/5] = self.p5_14[i][3]
              elif j == 15:
                  self.ss_5[0][i/5] = self.p5_15[i][0]
                  self.ss_5[1][i/5] = self.p5_15[i][1]
                  self.ss_5[2][i/5] = self.p5_15[i][2]
                  self.ss_5[3][i/5] = self.p5_15[i][3]
              elif j == 16:
                  self.ss_5[0][i/5] = self.p5_16[i][0]
                  self.ss_5[1][i/5] = self.p5_16[i][1]
                  self.ss_5[2][i/5] = self.p5_16[i][2]
                  self.ss_5[3][i/5] = self.p5_16[i][3]
              elif j == 17:
                  self.ss_5[0][i/5] = self.p5_17[i][0]
                  self.ss_5[1][i/5] = self.p5_17[i][1]
                  self.ss_5[2][i/5] = self.p5_17[i][2]
                  self.ss_5[3][i/5] = self.p5_17[i][3]
              elif j == 18:
                  self.ss_5[0][i/5] = self.p5_18[i][0]
                  self.ss_5[1][i/5] = self.p5_18[i][1]
                  self.ss_5[2][i/5] = self.p5_18[i][2]
                  self.ss_5[3][i/5] = self.p5_18[i][3]
              elif j == 19:
                  self.ss_5[0][i/5] = self.p5_19[i][0]
                  self.ss_5[1][i/5] = self.p5_19[i][1]
                  self.ss_5[2][i/5] = self.p5_19[i][2]
                  self.ss_5[3][i/5] = self.p5_19[i][3]
              elif j == 20:
                  self.ss_5[0][i/5] = self.p5_20[i][0]
                  self.ss_5[1][i/5] = self.p5_20[i][1]
                  self.ss_5[2][i/5] = self.p5_20[i][2]
                  self.ss_5[3][i/5] = self.p5_20[i][3]
                  j = 0
              j = j + 1

        j = 1
        self.ss_6 = np.zeros((4,d6/5+1))
        print "Stage 6"
        for i in range(0,d6):
            if (i % 5) == 0:
              if j == 1:
                  self.ss_6[0][i/5] = self.p6_1[i][0]
                  self.ss_6[1][i/5] = self.p6_1[i][1]
                  self.ss_6[2][i/5] = self.p6_1[i][2]
                  self.ss_6[3][i/5] = self.p6_1[i][3]
              elif j == 2:
                  self.ss_6[0][i/5] = self.p6_2[i][0]
                  self.ss_6[1][i/5] = self.p6_2[i][1]
                  self.ss_6[2][i/5] = self.p6_2[i][2]
                  self.ss_6[3][i/5] = self.p6_2[i][3]
              elif j == 3:
                  self.ss_6[0][i/5] = self.p6_3[i][0]
                  self.ss_6[1][i/5] = self.p6_3[i][1]
                  self.ss_6[2][i/5] = self.p6_3[i][2]
                  self.ss_6[3][i/5] = self.p6_3[i][3]
              elif j == 4:
                  self.ss_6[0][i/5] = self.p6_4[i][0]
                  self.ss_6[1][i/5] = self.p6_4[i][1]
                  self.ss_6[2][i/5] = self.p6_4[i][2]
                  self.ss_6[3][i/5] = self.p6_4[i][3]
              elif j == 5:
                  self.ss_6[0][i/5] = self.p6_5[i][0]
                  self.ss_6[1][i/5] = self.p6_5[i][1]
                  self.ss_6[2][i/5] = self.p6_5[i][2]
                  self.ss_6[3][i/5] = self.p6_5[i][3]
              elif j == 6:
                  self.ss_6[0][i/5] = self.p6_6[i][0]
                  self.ss_6[1][i/5] = self.p6_6[i][1]
                  self.ss_6[2][i/5] = self.p6_6[i][2]
                  self.ss_6[3][i/5] = self.p6_6[i][3]
              elif j == 7:
                  self.ss_6[0][i/5] = self.p6_7[i][0]
                  self.ss_6[1][i/5] = self.p6_7[i][1]
                  self.ss_6[2][i/5] = self.p6_7[i][2]
                  self.ss_6[3][i/5] = self.p6_7[i][3]
              elif j == 8:
                  self.ss_6[0][i/5] = self.p6_8[i][0]
                  self.ss_6[1][i/5] = self.p6_8[i][1]
                  self.ss_6[2][i/5] = self.p6_8[i][2]
                  self.ss_6[3][i/5] = self.p6_8[i][3]
              elif j == 9:
                  self.ss_6[0][i/5] = self.p6_9[i][0]
                  self.ss_6[1][i/5] = self.p6_9[i][1]
                  self.ss_6[2][i/5] = self.p6_9[i][2]
                  self.ss_6[3][i/5] = self.p6_9[i][3]
              elif j == 10:
                  self.ss_6[0][i/5] = self.p6_10[i][0]
                  self.ss_6[1][i/5] = self.p6_10[i][1]
                  self.ss_6[2][i/5] = self.p6_10[i][2]
                  self.ss_6[3][i/5] = self.p6_10[i][3]

              if j == 11:
                  self.ss_6[0][i/5] = self.p6_11[i][0]
                  self.ss_6[1][i/5] = self.p6_11[i][1]
                  self.ss_6[2][i/5] = self.p6_11[i][2]
                  self.ss_6[3][i/5] = self.p6_11[i][3]
              elif j == 12:
                  self.ss_6[0][i/5] = self.p6_12[i][0]
                  self.ss_6[1][i/5] = self.p6_12[i][1]
                  self.ss_6[2][i/5] = self.p6_12[i][2]
                  self.ss_6[3][i/5] = self.p6_12[i][3]
              elif j == 13:
                  self.ss_6[0][i/5] = self.p6_13[i][0]
                  self.ss_6[1][i/5] = self.p6_13[i][1]
                  self.ss_6[2][i/5] = self.p6_13[i][2]
                  self.ss_6[3][i/5] = self.p6_13[i][3]
              elif j == 14:
                  self.ss_6[0][i/5] = self.p6_14[i][0]
                  self.ss_6[1][i/5] = self.p6_14[i][1]
                  self.ss_6[2][i/5] = self.p6_14[i][2]
                  self.ss_6[3][i/5] = self.p6_14[i][3]
              elif j == 15:
                  self.ss_6[0][i/5] = self.p6_15[i][0]
                  self.ss_6[1][i/5] = self.p6_15[i][1]
                  self.ss_6[2][i/5] = self.p6_15[i][2]
                  self.ss_6[3][i/5] = self.p6_15[i][3]
              elif j == 16:
                  self.ss_6[0][i/5] = self.p6_16[i][0]
                  self.ss_6[1][i/5] = self.p6_16[i][1]
                  self.ss_6[2][i/5] = self.p6_16[i][2]
                  self.ss_6[3][i/5] = self.p6_16[i][3]
              elif j == 17:
                  self.ss_6[0][i/5] = self.p6_17[i][0]
                  self.ss_6[1][i/5] = self.p6_17[i][1]
                  self.ss_6[2][i/5] = self.p6_17[i][2]
                  self.ss_6[3][i/5] = self.p6_17[i][3]
              elif j == 18:
                  self.ss_6[0][i/5] = self.p6_18[i][0]
                  self.ss_6[1][i/5] = self.p6_18[i][1]
                  self.ss_6[2][i/5] = self.p6_18[i][2]
                  self.ss_6[3][i/5] = self.p6_18[i][3]
              elif j == 19:
                  self.ss_6[0][i/5] = self.p6_19[i][0]
                  self.ss_6[1][i/5] = self.p6_19[i][1]
                  self.ss_6[2][i/5] = self.p6_19[i][2]
                  self.ss_6[3][i/5] = self.p6_19[i][3]
              elif j == 20:
                  self.ss_6[0][i/5] = self.p6_20[i][0]
                  self.ss_6[1][i/5] = self.p6_20[i][1]
                  self.ss_6[2][i/5] = self.p6_20[i][2]
                  self.ss_6[3][i/5] = self.p6_20[i][3]
                  j = 0
              j = j + 1

        j = 1
        self.ss_7 = np.zeros((4,d7/5+1))
        print "Stage 7"
        for i in range(0,d7):
            if (i % 5) == 0:
              if j == 1:
                  self.ss_7[0][i/5] = self.p7_1[i][0]
                  self.ss_7[1][i/5] = self.p7_1[i][1]
                  self.ss_7[2][i/5] = self.p7_1[i][2]
                  self.ss_7[3][i/5] = self.p7_1[i][3]
              elif j == 2:
                  self.ss_7[0][i/5] = self.p7_2[i][0]
                  self.ss_7[1][i/5] = self.p7_2[i][1]
                  self.ss_7[2][i/5] = self.p7_2[i][2]
                  self.ss_7[3][i/5] = self.p7_2[i][3]
              elif j == 3:
                  self.ss_7[0][i/5] = self.p7_3[i][0]
                  self.ss_7[1][i/5] = self.p7_3[i][1]
                  self.ss_7[2][i/5] = self.p7_3[i][2]
                  self.ss_7[3][i/5] = self.p7_3[i][3]
              elif j == 4:
                  self.ss_7[0][i/5] = self.p7_4[i][0]
                  self.ss_7[1][i/5] = self.p7_4[i][1]
                  self.ss_7[2][i/5] = self.p7_4[i][2]
                  self.ss_7[3][i/5] = self.p7_4[i][3]
              elif j == 5:
                  self.ss_7[0][i/5] = self.p7_5[i][0]
                  self.ss_7[1][i/5] = self.p7_5[i][1]
                  self.ss_7[2][i/5] = self.p7_5[i][2]
                  self.ss_7[3][i/5] = self.p7_5[i][3]
              elif j == 6:
                  self.ss_7[0][i/5] = self.p7_6[i][0]
                  self.ss_7[1][i/5] = self.p7_6[i][1]
                  self.ss_7[2][i/5] = self.p7_6[i][2]
                  self.ss_7[3][i/5] = self.p7_6[i][3]
              elif j == 7:
                  self.ss_7[0][i/5] = self.p7_7[i][0]
                  self.ss_7[1][i/5] = self.p7_7[i][1]
                  self.ss_7[2][i/5] = self.p7_7[i][2]
                  self.ss_7[3][i/5] = self.p7_7[i][3]
              elif j == 8:
                  self.ss_7[0][i/5] = self.p7_8[i][0]
                  self.ss_7[1][i/5] = self.p7_8[i][1]
                  self.ss_7[2][i/5] = self.p7_8[i][2]
                  self.ss_7[3][i/5] = self.p7_8[i][3]
              elif j == 9:
                  self.ss_7[0][i/5] = self.p7_9[i][0]
                  self.ss_7[1][i/5] = self.p7_9[i][1]
                  self.ss_7[2][i/5] = self.p7_9[i][2]
                  self.ss_7[3][i/5] = self.p7_9[i][3]
              elif j == 10:
                  self.ss_7[0][i/5] = self.p7_10[i][0]
                  self.ss_7[1][i/5] = self.p7_10[i][1]
                  self.ss_7[2][i/5] = self.p7_10[i][2]
                  self.ss_7[3][i/5] = self.p7_10[i][3]


              if j == 11:
                  self.ss_7[0][i/5] = self.p7_11[i][0]
                  self.ss_7[1][i/5] = self.p7_11[i][1]
                  self.ss_7[2][i/5] = self.p7_11[i][2]
                  self.ss_7[3][i/5] = self.p7_11[i][3]
              elif j == 12:
                  self.ss_7[0][i/5] = self.p7_12[i][0]
                  self.ss_7[1][i/5] = self.p7_12[i][1]
                  self.ss_7[2][i/5] = self.p7_12[i][2]
                  self.ss_7[3][i/5] = self.p7_12[i][3]
              elif j == 13:
                  self.ss_7[0][i/5] = self.p7_13[i][0]
                  self.ss_7[1][i/5] = self.p7_13[i][1]
                  self.ss_7[2][i/5] = self.p7_13[i][2]
                  self.ss_7[3][i/5] = self.p7_13[i][3]
              elif j == 14:
                  self.ss_7[0][i/5] = self.p7_14[i][0]
                  self.ss_7[1][i/5] = self.p7_14[i][1]
                  self.ss_7[2][i/5] = self.p7_14[i][2]
                  self.ss_7[3][i/5] = self.p7_14[i][3]
              elif j == 15:
                  self.ss_7[0][i/5] = self.p7_15[i][0]
                  self.ss_7[1][i/5] = self.p7_15[i][1]
                  self.ss_7[2][i/5] = self.p7_15[i][2]
                  self.ss_7[3][i/5] = self.p7_15[i][3]
              elif j == 16:
                  self.ss_7[0][i/5] = self.p7_16[i][0]
                  self.ss_7[1][i/5] = self.p7_16[i][1]
                  self.ss_7[2][i/5] = self.p7_16[i][2]
                  self.ss_7[3][i/5] = self.p7_16[i][3]
              elif j == 17:
                  self.ss_7[0][i/5] = self.p7_17[i][0]
                  self.ss_7[1][i/5] = self.p7_17[i][1]
                  self.ss_7[2][i/5] = self.p7_17[i][2]
                  self.ss_7[3][i/5] = self.p7_17[i][3]
              elif j == 18:
                  self.ss_7[0][i/5] = self.p7_18[i][0]
                  self.ss_7[1][i/5] = self.p7_18[i][1]
                  self.ss_7[2][i/5] = self.p7_18[i][2]
                  self.ss_7[3][i/5] = self.p7_18[i][3]
              elif j == 19:
                  self.ss_7[0][i/5] = self.p7_19[i][0]
                  self.ss_7[1][i/5] = self.p7_19[i][1]
                  self.ss_7[2][i/5] = self.p7_19[i][2]
                  self.ss_7[3][i/5] = self.p7_19[i][3]
              elif j == 20:
                  self.ss_7[0][i/5] = self.p7_20[i][0]
                  self.ss_7[1][i/5] = self.p7_20[i][1]
                  self.ss_7[2][i/5] = self.p7_20[i][2]
                  self.ss_7[3][i/5] = self.p7_20[i][3]
                  j = 0
              j = j + 1

        j = 1
        self.ss_8 = np.zeros((4,d8/5+1))
        print "Stage 8"
        for i in range(0,d8):
            if (i % 5) == 0:
              if j == 1:
                  self.ss_8[0][i/5] = self.p8_1[i][0]
                  self.ss_8[1][i/5] = self.p8_1[i][1]
                  self.ss_8[2][i/5] = self.p8_1[i][2]
                  self.ss_8[3][i/5] = self.p8_1[i][3]
              elif j == 2:
                  self.ss_8[0][i/5] = self.p8_2[i][0]
                  self.ss_8[1][i/5] = self.p8_2[i][1]
                  self.ss_8[2][i/5] = self.p8_2[i][2]
                  self.ss_8[3][i/5] = self.p8_2[i][3]
              elif j == 3:
                  self.ss_8[0][i/5] = self.p8_3[i][0]
                  self.ss_8[1][i/5] = self.p8_3[i][1]
                  self.ss_8[2][i/5] = self.p8_3[i][2]
                  self.ss_8[3][i/5] = self.p8_3[i][3]
              elif j == 4:
                  self.ss_8[0][i/5] = self.p8_4[i][0]
                  self.ss_8[1][i/5] = self.p8_4[i][1]
                  self.ss_8[2][i/5] = self.p8_4[i][2]
                  self.ss_8[3][i/5] = self.p8_4[i][3]
              elif j == 5:
                  self.ss_8[0][i/5] = self.p8_5[i][0]
                  self.ss_8[1][i/5] = self.p8_5[i][1]
                  self.ss_8[2][i/5] = self.p8_5[i][2]
                  self.ss_8[3][i/5] = self.p8_5[i][3]
              elif j == 6:
                  self.ss_8[0][i/5] = self.p8_6[i][0]
                  self.ss_8[1][i/5] = self.p8_6[i][1]
                  self.ss_8[2][i/5] = self.p8_6[i][2]
                  self.ss_8[3][i/5] = self.p8_6[i][3]
              elif j == 7:
                  self.ss_8[0][i/5] = self.p8_7[i][0]
                  self.ss_8[1][i/5] = self.p8_7[i][1]
                  self.ss_8[2][i/5] = self.p8_7[i][2]
                  self.ss_8[3][i/5] = self.p8_7[i][3]
              elif j == 8:
                  self.ss_8[0][i/5] = self.p8_8[i][0]
                  self.ss_8[1][i/5] = self.p8_8[i][1]
                  self.ss_8[2][i/5] = self.p8_8[i][2]
                  self.ss_8[3][i/5] = self.p8_8[i][3]
              elif j == 9:
                  self.ss_8[0][i/5] = self.p8_9[i][0]
                  self.ss_8[1][i/5] = self.p8_9[i][1]
                  self.ss_8[2][i/5] = self.p8_9[i][2]
                  self.ss_8[3][i/5] = self.p8_9[i][3]
              elif j == 10:
                  self.ss_8[0][i/5] = self.p8_10[i][0]
                  self.ss_8[1][i/5] = self.p8_10[i][1]
                  self.ss_8[2][i/5] = self.p8_10[i][2]
                  self.ss_8[3][i/5] = self.p8_10[i][3]

              if j == 11:
                  self.ss_8[0][i/5] = self.p8_11[i][0]
                  self.ss_8[1][i/5] = self.p8_11[i][1]
                  self.ss_8[2][i/5] = self.p8_11[i][2]
                  self.ss_8[3][i/5] = self.p8_11[i][3]
              elif j == 12:
                  self.ss_8[0][i/5] = self.p8_12[i][0]
                  self.ss_8[1][i/5] = self.p8_12[i][1]
                  self.ss_8[2][i/5] = self.p8_12[i][2]
                  self.ss_8[3][i/5] = self.p8_12[i][3]

              elif j == 13:
                  self.ss_8[0][i/5] = self.p8_13[i][0]
                  self.ss_8[1][i/5] = self.p8_13[i][1]
                  self.ss_8[2][i/5] = self.p8_13[i][2]
                  self.ss_8[3][i/5] = self.p8_13[i][3]
              elif j == 14:
                  self.ss_8[0][i/5] = self.p8_14[i][0]
                  self.ss_8[1][i/5] = self.p8_14[i][1]
                  self.ss_8[2][i/5] = self.p8_14[i][2]
                  self.ss_8[3][i/5] = self.p8_14[i][3]
              elif j == 15:
                  self.ss_8[0][i/5] = self.p8_15[i][0]
                  self.ss_8[1][i/5] = self.p8_15[i][1]
                  self.ss_8[2][i/5] = self.p8_15[i][2]
                  self.ss_8[3][i/5] = self.p8_15[i][3]
              elif j == 16:
                  self.ss_8[0][i/5] = self.p8_16[i][0]
                  self.ss_8[1][i/5] = self.p8_16[i][1]
                  self.ss_8[2][i/5] = self.p8_16[i][2]
                  self.ss_8[3][i/5] = self.p8_16[i][3]
              elif j == 17:
                  self.ss_8[0][i/5] = self.p8_17[i][0]
                  self.ss_8[1][i/5] = self.p8_17[i][1]
                  self.ss_8[2][i/5] = self.p8_17[i][2]
                  self.ss_8[3][i/5] = self.p8_17[i][3]
              elif j == 18:
                  self.ss_8[0][i/5] = self.p8_18[i][0]
                  self.ss_8[1][i/5] = self.p8_18[i][1]
                  self.ss_8[2][i/5] = self.p8_18[i][2]
                  self.ss_8[3][i/5] = self.p8_18[i][3]
              elif j == 19:
                  self.ss_8[0][i/5] = self.p8_19[i][0]
                  self.ss_8[1][i/5] = self.p8_19[i][1]
                  self.ss_8[2][i/5] = self.p8_19[i][2]
                  self.ss_8[3][i/5] = self.p8_19[i][3]
              elif j == 20:
                  self.ss_8[0][i/5] = self.p8_20[i][0]
                  self.ss_8[1][i/5] = self.p8_20[i][1]
                  self.ss_8[2][i/5] = self.p8_20[i][2]
                  self.ss_8[3][i/5] = self.p8_20[i][3]
                  j = 0
              j = j + 1

        j = 1
        self.ss_9 = np.zeros((4,d9/5+1))
        print "Stage 9"
        for i in range(0,d9):
            if (i % 5) == 0:
              if j == 1:
                  self.ss_9[0][i/5] = self.p9_1[i][0]
                  self.ss_9[1][i/5] = self.p9_1[i][1]
                  self.ss_9[2][i/5] = self.p9_1[i][2]
                  self.ss_9[3][i/5] = self.p9_1[i][3]
              elif j == 2:
                  self.ss_9[0][i/5] = self.p9_2[i][0]
                  self.ss_9[1][i/5] = self.p9_2[i][1]
                  self.ss_9[2][i/5] = self.p9_2[i][2]
                  self.ss_9[3][i/5] = self.p9_2[i][3]
              elif j == 3:
                  self.ss_9[0][i/5] = self.p9_3[i][0]
                  self.ss_9[1][i/5] = self.p9_3[i][1]
                  self.ss_9[2][i/5] = self.p9_3[i][2]
                  self.ss_9[3][i/5] = self.p9_3[i][3]
              elif j == 4:
                  self.ss_9[0][i/5] = self.p9_4[i][0]
                  self.ss_9[1][i/5] = self.p9_4[i][1]
                  self.ss_9[2][i/5] = self.p9_4[i][2]
                  self.ss_9[3][i/5] = self.p9_4[i][3]
              elif j == 5:
                  self.ss_9[0][i/5] = self.p9_5[i][0]
                  self.ss_9[1][i/5] = self.p9_5[i][1]
                  self.ss_9[2][i/5] = self.p9_5[i][2]
                  self.ss_9[3][i/5] = self.p9_5[i][3]
              elif j == 6:
                  self.ss_9[0][i/5] = self.p9_6[i][0]
                  self.ss_9[1][i/5] = self.p9_6[i][1]
                  self.ss_9[2][i/5] = self.p9_6[i][2]
                  self.ss_9[3][i/5] = self.p9_6[i][3]
              elif j == 7:
                  self.ss_9[0][i/5] = self.p9_7[i][0]
                  self.ss_9[1][i/5] = self.p9_7[i][1]
                  self.ss_9[2][i/5] = self.p9_7[i][2]
                  self.ss_9[3][i/5] = self.p9_7[i][3]
              elif j == 8:
                  self.ss_9[0][i/5] = self.p9_8[i][0]
                  self.ss_9[1][i/5] = self.p9_8[i][1]
                  self.ss_9[2][i/5] = self.p9_8[i][2]
                  self.ss_9[3][i/5] = self.p9_8[i][3]
              elif j == 9:
                  self.ss_9[0][i/5] = self.p9_9[i][0]
                  self.ss_9[1][i/5] = self.p9_9[i][1]
                  self.ss_9[2][i/5] = self.p9_9[i][2]
                  self.ss_9[3][i/5] = self.p9_9[i][3]
              elif j == 10:
                  self.ss_9[0][i/5] = self.p9_10[i][0]
                  self.ss_9[1][i/5] = self.p9_10[i][1]
                  self.ss_9[2][i/5] = self.p9_10[i][2]
                  self.ss_9[3][i/5] = self.p9_10[i][3]

              if j == 11:
                  self.ss_9[0][i/5] = self.p9_11[i][0]
                  self.ss_9[1][i/5] = self.p9_11[i][1]
                  self.ss_9[2][i/5] = self.p9_11[i][2]
                  self.ss_9[3][i/5] = self.p9_11[i][3]
              elif j == 12:
                  self.ss_9[0][i/5] = self.p9_12[i][0]
                  self.ss_9[1][i/5] = self.p9_12[i][1]
                  self.ss_9[2][i/5] = self.p9_12[i][2]
                  self.ss_9[3][i/5] = self.p9_12[i][3]
              elif j == 13:
                  self.ss_9[0][i/5] = self.p9_13[i][0]
                  self.ss_9[1][i/5] = self.p9_13[i][1]
                  self.ss_9[2][i/5] = self.p9_13[i][2]
                  self.ss_9[3][i/5] = self.p9_13[i][3]
              elif j == 14:
                  self.ss_9[0][i/5] = self.p9_14[i][0]
                  self.ss_9[1][i/5] = self.p9_14[i][1]
                  self.ss_9[2][i/5] = self.p9_14[i][2]
                  self.ss_9[3][i/5] = self.p9_14[i][3]
              elif j == 15:
                  self.ss_9[0][i/5] = self.p9_15[i][0]
                  self.ss_9[1][i/5] = self.p9_15[i][1]
                  self.ss_9[2][i/5] = self.p9_15[i][2]
                  self.ss_9[3][i/5] = self.p9_15[i][3]
              elif j == 16:
                  self.ss_9[0][i/5] = self.p9_16[i][0]
                  self.ss_9[1][i/5] = self.p9_16[i][1]
                  self.ss_9[2][i/5] = self.p9_16[i][2]
                  self.ss_9[3][i/5] = self.p9_16[i][3]
              elif j == 17:
                  self.ss_9[0][i/5] = self.p9_17[i][0]
                  self.ss_9[1][i/5] = self.p9_17[i][1]
                  self.ss_9[2][i/5] = self.p9_17[i][2]
                  self.ss_9[3][i/5] = self.p9_17[i][3]
              elif j == 18:
                  self.ss_9[0][i/5] = self.p9_18[i][0]
                  self.ss_9[1][i/5] = self.p9_18[i][1]
                  self.ss_9[2][i/5] = self.p9_18[i][2]
                  self.ss_9[3][i/5] = self.p9_18[i][3]
              elif j == 19:
                  self.ss_9[0][i/5] = self.p9_19[i][0]
                  self.ss_9[1][i/5] = self.p9_19[i][1]
                  self.ss_9[2][i/5] = self.p9_19[i][2]
                  self.ss_9[3][i/5] = self.p9_19[i][3]
              elif j == 20:
                  self.ss_9[0][i/5] = self.p9_20[i][0]
                  self.ss_9[1][i/5] = self.p9_20[i][1]
                  self.ss_9[2][i/5] = self.p9_20[i][2]
                  self.ss_9[3][i/5] = self.p9_20[i][3]
                  j = 0
              j = j + 1

        j = 1
        self.ss_10 = np.zeros((4,d10/5+1))
        print "Stage 10"
        for i in range(0,d10):
            if (i % 5) == 0:
              if j == 1:
                  self.ss_10[0][i/5] = self.p10_1[i][0]
                  self.ss_10[1][i/5] = self.p10_1[i][1]
                  self.ss_10[2][i/5] = self.p10_1[i][2]
                  self.ss_10[3][i/5] = self.p10_1[i][3]
              elif j == 2:
                  self.ss_10[0][i/5] = self.p10_2[i][0]
                  self.ss_10[1][i/5] = self.p10_2[i][1]
                  self.ss_10[2][i/5] = self.p10_2[i][2]
                  self.ss_10[3][i/5] = self.p10_2[i][3]
              elif j == 3:
                  self.ss_10[0][i/5] = self.p10_3[i][0]
                  self.ss_10[1][i/5] = self.p10_3[i][1]
                  self.ss_10[2][i/5] = self.p10_3[i][2]
                  self.ss_10[3][i/5] = self.p10_3[i][3]
              elif j == 4:
                  self.ss_10[0][i/5] = self.p10_4[i][0]
                  self.ss_10[1][i/5] = self.p10_4[i][1]
                  self.ss_10[2][i/5] = self.p10_4[i][2]
                  self.ss_10[3][i/5] = self.p10_4[i][3]
              elif j == 5:
                  self.ss_10[0][i/5] = self.p10_5[i][0]
                  self.ss_10[1][i/5] = self.p10_5[i][1]
                  self.ss_10[2][i/5] = self.p10_5[i][2]
                  self.ss_10[3][i/5] = self.p10_5[i][3]
              elif j == 6:
                  self.ss_10[0][i/5] = self.p10_6[i][0]
                  self.ss_10[1][i/5] = self.p10_6[i][1]
                  self.ss_10[2][i/5] = self.p10_6[i][2]
                  self.ss_10[3][i/5] = self.p10_6[i][3]
              elif j == 7:
                  self.ss_10[0][i/5] = self.p10_7[i][0]
                  self.ss_10[1][i/5] = self.p10_7[i][1]
                  self.ss_10[2][i/5] = self.p10_7[i][2]
                  self.ss_10[3][i/5] = self.p10_7[i][3]
              elif j == 8:
                  self.ss_10[0][i/5] = self.p10_8[i][0]
                  self.ss_10[1][i/5] = self.p10_8[i][1]
                  self.ss_10[2][i/5] = self.p10_8[i][2]
                  self.ss_10[3][i/5] = self.p10_8[i][3]
              elif j == 9:
                  self.ss_10[0][i/5] = self.p10_9[i][0]
                  self.ss_10[1][i/5] = self.p10_9[i][1]
                  self.ss_10[2][i/5] = self.p10_9[i][2]
                  self.ss_10[3][i/5] = self.p10_9[i][3]
              elif j == 10:
                  self.ss_10[0][i/5] = self.p10_10[i][0]
                  self.ss_10[1][i/5] = self.p10_10[i][1]
                  self.ss_10[2][i/5] = self.p10_10[i][2]
                  self.ss_10[3][i/5] = self.p10_10[i][3]

              if j == 11:
                  self.ss_10[0][i/5] = self.p10_11[i][0]
                  self.ss_10[1][i/5] = self.p10_11[i][1]
                  self.ss_10[2][i/5] = self.p10_11[i][2]
                  self.ss_10[3][i/5] = self.p10_11[i][3]
              elif j == 12:
                  self.ss_10[0][i/5] = self.p10_12[i][0]
                  self.ss_10[1][i/5] = self.p10_12[i][1]
                  self.ss_10[2][i/5] = self.p10_12[i][2]
                  self.ss_10[3][i/5] = self.p10_12[i][3]
              elif j == 13:
                  self.ss_10[0][i/5] = self.p10_13[i][0]
                  self.ss_10[1][i/5] = self.p10_13[i][1]
                  self.ss_10[2][i/5] = self.p10_13[i][2]
                  self.ss_10[3][i/5] = self.p10_13[i][3]
              elif j == 14:
                  self.ss_10[0][i/5] = self.p10_14[i][0]
                  self.ss_10[1][i/5] = self.p10_14[i][1]
                  self.ss_10[2][i/5] = self.p10_14[i][2]
                  self.ss_10[3][i/5] = self.p10_14[i][3]
              elif j == 15:
                  self.ss_10[0][i/5] = self.p10_15[i][0]
                  self.ss_10[1][i/5] = self.p10_15[i][1]
                  self.ss_10[2][i/5] = self.p10_15[i][2]
                  self.ss_10[3][i/5] = self.p10_15[i][3]
              elif j == 16:
                  self.ss_10[0][i/5] = self.p10_16[i][0]
                  self.ss_10[1][i/5] = self.p10_16[i][1]
                  self.ss_10[2][i/5] = self.p10_16[i][2]
                  self.ss_10[3][i/5] = self.p10_16[i][3]
              elif j == 17:
                  self.ss_10[0][i/5] = self.p10_17[i][0]
                  self.ss_10[1][i/5] = self.p10_17[i][1]
                  self.ss_10[2][i/5] = self.p10_17[i][2]
                  self.ss_10[3][i/5] = self.p10_17[i][3]
              elif j == 18:
                  self.ss_10[0][i/5] = self.p10_18[i][0]
                  self.ss_10[1][i/5] = self.p10_18[i][1]
                  self.ss_10[2][i/5] = self.p10_18[i][2]
                  self.ss_10[3][i/5] = self.p10_18[i][3]
              elif j == 19:
                  self.ss_10[0][i/5] = self.p10_19[i][0]
                  self.ss_10[1][i/5] = self.p10_19[i][1]
                  self.ss_10[2][i/5] = self.p10_19[i][2]
                  self.ss_10[3][i/5] = self.p10_19[i][3]
              elif j == 20:
                  self.ss_10[0][i/5] = self.p10_20[i][0]
                  self.ss_10[1][i/5] = self.p10_20[i][1]
                  self.ss_10[2][i/5] = self.p10_20[i][2]
                  self.ss_10[3][i/5] = self.p10_20[i][3]
                  j = 0
              j = j + 1

        j = 1
        self.ss_11 = np.zeros((4,d11/5+1))
        print "Stage 11"
        for i in range(0,d11):
            if (i % 5) == 0:
              if j == 1:
                  self.ss_11[0][i/5] = self.p11_1[i][0]
                  self.ss_11[1][i/5] = self.p11_1[i][1]
                  self.ss_11[2][i/5] = self.p11_1[i][2]
                  self.ss_11[3][i/5] = self.p11_1[i][3]
              elif j == 2:
                  self.ss_11[0][i/5] = self.p11_2[i][0]
                  self.ss_11[1][i/5] = self.p11_2[i][1]
                  self.ss_11[2][i/5] = self.p11_2[i][2]
                  self.ss_11[3][i/5] = self.p11_2[i][3]
              elif j == 3:
                  self.ss_11[0][i/5] = self.p11_3[i][0]
                  self.ss_11[1][i/5] = self.p11_3[i][1]
                  self.ss_11[2][i/5] = self.p11_3[i][2]
                  self.ss_11[3][i/5] = self.p11_3[i][3]
              elif j == 4:
                  self.ss_11[0][i/5] = self.p11_4[i][0]
                  self.ss_11[1][i/5] = self.p11_4[i][1]
                  self.ss_11[2][i/5] = self.p11_4[i][2]
                  self.ss_11[3][i/5] = self.p11_4[i][3]
              elif j == 5:
                  self.ss_11[0][i/5] = self.p11_5[i][0]
                  self.ss_11[1][i/5] = self.p11_5[i][1]
                  self.ss_11[2][i/5] = self.p11_5[i][2]
                  self.ss_11[3][i/5] = self.p11_5[i][3]
              elif j == 6:
                  self.ss_11[0][i/5] = self.p11_6[i][0]
                  self.ss_11[1][i/5] = self.p11_6[i][1]
                  self.ss_11[2][i/5] = self.p11_6[i][2]
                  self.ss_11[3][i/5] = self.p11_6[i][3]
              elif j == 7:
                  self.ss_11[0][i/5] = self.p11_7[i][0]
                  self.ss_11[1][i/5] = self.p11_7[i][1]
                  self.ss_11[2][i/5] = self.p11_7[i][2]
                  self.ss_11[3][i/5] = self.p11_7[i][3]
              elif j == 8:
                  self.ss_11[0][i/5] = self.p11_8[i][0]
                  self.ss_11[1][i/5] = self.p11_8[i][1]
                  self.ss_11[2][i/5] = self.p11_8[i][2]
                  self.ss_11[3][i/5] = self.p11_8[i][3]
              elif j == 9:
                  self.ss_11[0][i/5] = self.p11_9[i][0]
                  self.ss_11[1][i/5] = self.p11_9[i][1]
                  self.ss_11[2][i/5] = self.p11_9[i][2]
                  self.ss_11[3][i/5] = self.p11_9[i][3]
              elif j == 10:
                  self.ss_11[0][i/5] = self.p11_10[i][0]
                  self.ss_11[1][i/5] = self.p11_10[i][1]
                  self.ss_11[2][i/5] = self.p11_10[i][2]
                  self.ss_11[3][i/5] = self.p11_10[i][3]

              if j == 11:
                  self.ss_11[0][i/5] = self.p11_11[i][0]
                  self.ss_11[1][i/5] = self.p11_11[i][1]
                  self.ss_11[2][i/5] = self.p11_11[i][2]
                  self.ss_11[3][i/5] = self.p11_11[i][3]
              elif j == 12:
                  self.ss_11[0][i/5] = self.p11_12[i][0]
                  self.ss_11[1][i/5] = self.p11_12[i][1]
                  self.ss_11[2][i/5] = self.p11_12[i][2]
                  self.ss_11[3][i/5] = self.p11_12[i][3]
              elif j == 13:
                  self.ss_11[0][i/5] = self.p11_13[i][0]
                  self.ss_11[1][i/5] = self.p11_13[i][1]
                  self.ss_11[2][i/5] = self.p11_13[i][2]
                  self.ss_11[3][i/5] = self.p11_13[i][3]
              elif j == 14:
                  self.ss_11[0][i/5] = self.p11_14[i][0]
                  self.ss_11[1][i/5] = self.p11_14[i][1]
                  self.ss_11[2][i/5] = self.p11_14[i][2]
                  self.ss_11[3][i/5] = self.p11_14[i][3]
              elif j == 15:
                  self.ss_11[0][i/5] = self.p11_15[i][0]
                  self.ss_11[1][i/5] = self.p11_15[i][1]
                  self.ss_11[2][i/5] = self.p11_15[i][2]
                  self.ss_11[3][i/5] = self.p11_15[i][3]
              elif j == 16:
                  self.ss_11[0][i/5] = self.p11_16[i][0]
                  self.ss_11[1][i/5] = self.p11_16[i][1]
                  self.ss_11[2][i/5] = self.p11_16[i][2]
                  self.ss_11[3][i/5] = self.p11_16[i][3]
              elif j == 17:
                  self.ss_11[0][i/5] = self.p11_17[i][0]
                  self.ss_11[1][i/5] = self.p11_17[i][1]
                  self.ss_11[2][i/5] = self.p11_17[i][2]
                  self.ss_11[3][i/5] = self.p11_17[i][3]
              elif j == 18:
                  self.ss_11[0][i/5] = self.p11_18[i][0]
                  self.ss_11[1][i/5] = self.p11_18[i][1]
                  self.ss_11[2][i/5] = self.p11_18[i][2]
                  self.ss_11[3][i/5] = self.p11_18[i][3]
              elif j == 19:
                  self.ss_11[0][i/5] = self.p11_19[i][0]
                  self.ss_11[1][i/5] = self.p11_19[i][1]
                  self.ss_11[2][i/5] = self.p11_19[i][2]
                  self.ss_11[3][i/5] = self.p11_19[i][3]
              elif j == 20:
                  self.ss_11[0][i/5] = self.p11_20[i][0]
                  self.ss_11[1][i/5] = self.p11_20[i][1]
                  self.ss_11[2][i/5] = self.p11_20[i][2]
                  self.ss_11[3][i/5] = self.p11_20[i][3]
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
        print "9-", np.shape(self.ss_9)
        print "10-", np.shape(self.ss_10)
        print "11-", np.shape(self.ss_11)

    def cross_validation(self): # Need to figure out transpose thingy
        print "Creating Valid Tests"
        d10_1  = len(self.p1_10)
        d10_2  = len(self.p2_10)
        d10_3  = len(self.p3_10)
        d10_4  = len(self.p4_10)
        d10_5  = len(self.p5_10)
        d10_6  = len(self.p6_10)
        d10_7  = len(self.p7_10)
        d10_8  = len(self.p8_10)
        d10_9  = len(self.p9_10)
        d10_10 = len(self.p10_10)
        d10_11 = len(self.p11_10)
        d10 = d10_1 + d10_2 + d10_3 + d10_4 + d10_5 + d10_6 + d10_7 + d10_8 + d10_9 + d10_10 + d10_11

        d20_1  = len(self.p1_20)
        d20_2  = len(self.p2_20)
        d20_3  = len(self.p3_20)
        d20_4  = len(self.p4_20)
        d20_5  = len(self.p5_20)
        d20_6  = len(self.p6_20)
        d20_7  = len(self.p7_20)
        d20_8  = len(self.p8_20)
        d20_9  = len(self.p9_20)
        d20_10 = len(self.p10_20)
        d20_11 = len(self.p11_20)
        d20 = d20_1 + d20_2 + d20_3 + d20_4 + d20_5 + d20_6 + d20_7 + d20_8 + d20_9 + d20_10 + d20_11
        self.cv_10 = np.zeros((4,d10))
        self.cv_20 = np.zeros((4,d20))
      

        for i in range(0,d10):
          if i < d10_1 :
            self.cv_10[0][i] = self.p1_10[i][0]
            self.cv_10[1][i] = self.p1_10[i][1]
            self.cv_10[2][i] = self.p1_10[i][2]
            self.cv_10[3][i] = self.p1_10[i][3]
          elif i < d10_1+d10_2 :
            self.cv_10[0][i] = self.p2_10[i-d10_1][0]
            self.cv_10[1][i] = self.p2_10[i-d10_1][1]
            self.cv_10[2][i] = self.p2_10[i-d10_1][2]
            self.cv_10[3][i] = self.p2_10[i-d10_1][3]
          elif i < d10_1+d10_2+d10_3 :
            self.cv_10[0][i] = self.p3_10[i-d10_1-d10_2][0]
            self.cv_10[1][i] = self.p3_10[i-d10_1-d10_2][1]
            self.cv_10[2][i] = self.p3_10[i-d10_1-d10_2][2]
            self.cv_10[3][i] = self.p3_10[i-d10_1-d10_2][3]
          elif i < d10_1+d10_2+d10_3+d10_4 :
            self.cv_10[0][i] = self.p4_10[i-d10_1-d10_2-d10_3][0]
            self.cv_10[1][i] = self.p4_10[i-d10_1-d10_2-d10_3][1]
            self.cv_10[2][i] = self.p4_10[i-d10_1-d10_2-d10_3][2]
            self.cv_10[3][i] = self.p4_10[i-d10_1-d10_2-d10_3][3]
          elif i < d10_1+d10_2+d10_3+d10_4+d10_5 :
            self.cv_10[0][i] = self.p5_10[i-d10_1-d10_2-d10_3-d10_4][0]
            self.cv_10[1][i] = self.p5_10[i-d10_1-d10_2-d10_3-d10_4][1]
            self.cv_10[2][i] = self.p5_10[i-d10_1-d10_2-d10_3-d10_4][2]
            self.cv_10[3][i] = self.p5_10[i-d10_1-d10_2-d10_3-d10_4][3]
          elif i < d10_1+d10_2+d10_3+d10_4+d10_5+d10_6 :
            self.cv_10[0][i] = self.p6_10[i-d10_1-d10_2-d10_3-d10_4-d10_5][0]
            self.cv_10[1][i] = self.p6_10[i-d10_1-d10_2-d10_3-d10_4-d10_5][1]
            self.cv_10[2][i] = self.p6_10[i-d10_1-d10_2-d10_3-d10_4-d10_5][2]
            self.cv_10[3][i] = self.p6_10[i-d10_1-d10_2-d10_3-d10_4-d10_5][3]
          elif i < d10_1+d10_2+d10_3+d10_4+d10_5+d10_6+d10_7 :
            self.cv_10[0][i] = self.p7_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6][0]
            self.cv_10[1][i] = self.p7_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6][1]
            self.cv_10[2][i] = self.p7_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6][2]
            self.cv_10[3][i] = self.p7_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6][3]
          elif i < d10_1+d10_2+d10_3+d10_4+d10_5+d10_6+d10_7 +d10_8 :
            self.cv_10[0][i] = self.p8_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7][0]
            self.cv_10[1][i] = self.p8_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7][1]
            self.cv_10[2][i] = self.p8_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7][2]
            self.cv_10[3][i] = self.p8_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7][3]
          elif i < d10_1+d10_2+d10_3+d10_4+d10_5+d10_6+d10_7 +d10_8 +d10_9:
            self.cv_10[0][i] = self.p9_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7-d10_8][0]
            self.cv_10[1][i] = self.p9_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7-d10_8][1]
            self.cv_10[2][i] = self.p9_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7-d10_8][2]
            self.cv_10[3][i] = self.p9_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7-d10_8][3]
          elif i < d10_1+d10_2+d10_3+d10_4+d10_5+d10_6+d10_7 +d10_8 +d10_9+d10_10:
            self.cv_10[0][i] = self.p10_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7-d10_8-d10_9][0]
            self.cv_10[1][i] = self.p10_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7-d10_8-d10_9][1]
            self.cv_10[2][i] = self.p10_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7-d10_8-d10_9][2]
            self.cv_10[3][i] = self.p10_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7-d10_8-d10_9][3]
          elif i < d10_1+d10_2+d10_3+d10_4+d10_5+d10_6+d10_7 +d10_8 +d10_9+d10_10+d10_11:
            self.cv_10[0][i] = self.p11_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7-d10_8-d10_9-d10_10][0]
            self.cv_10[1][i] = self.p11_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7-d10_8-d10_9-d10_10][1]
            self.cv_10[2][i] = self.p11_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7-d10_8-d10_9-d10_10][2]
            self.cv_10[3][i] = self.p11_10[i-d10_1-d10_2-d10_3-d10_4-d10_5-d10_6-d10_7-d10_8-d10_9-d10_10][3]

        for i in range(0,d20):
          if i < d20_1 :
            self.cv_20[0][i] = self.p1_20[i][0]
            self.cv_20[1][i] = self.p1_20[i][1]
            self.cv_20[2][i] = self.p1_20[i][2]
            self.cv_20[3][i] = self.p1_20[i][3]
          elif i < d20_1+d20_2 :
            self.cv_20[0][i] = self.p2_20[i-d20_1][0]
            self.cv_20[1][i] = self.p2_20[i-d20_1][1]
            self.cv_20[2][i] = self.p2_20[i-d20_1][2]
            self.cv_20[3][i] = self.p2_20[i-d20_1][3]
          elif i < d20_1+d20_2+d20_3 :
            self.cv_20[0][i] = self.p3_20[i-d20_1-d20_2][0]
            self.cv_20[1][i] = self.p3_20[i-d20_1-d20_2][1]
            self.cv_20[2][i] = self.p3_20[i-d20_1-d20_2][2]
            self.cv_20[3][i] = self.p3_20[i-d20_1-d20_2][3]
          elif i < d20_1+d20_2+d20_3+d20_4 :
            self.cv_20[0][i] = self.p4_20[i-d20_1-d20_2-d20_3][0]
            self.cv_20[1][i] = self.p4_20[i-d20_1-d20_2-d20_3][1]
            self.cv_20[2][i] = self.p4_20[i-d20_1-d20_2-d20_3][2]
            self.cv_20[3][i] = self.p4_20[i-d20_1-d20_2-d20_3][3]
          elif i < d20_1+d20_2+d20_3+d20_4+d20_5 :
            self.cv_20[0][i] = self.p5_20[i-d20_1-d20_2-d20_3-d20_4][0]
            self.cv_20[1][i] = self.p5_20[i-d20_1-d20_2-d20_3-d20_4][1]
            self.cv_20[2][i] = self.p5_20[i-d20_1-d20_2-d20_3-d20_4][2]
            self.cv_20[3][i] = self.p5_20[i-d20_1-d20_2-d20_3-d20_4][3]
          elif i < d20_1+d20_2+d20_3+d20_4+d20_5+d20_6 :
            self.cv_20[0][i] = self.p6_20[i-d20_1-d20_2-d20_3-d20_4-d20_5][0]
            self.cv_20[1][i] = self.p6_20[i-d20_1-d20_2-d20_3-d20_4-d20_5][1]
            self.cv_20[2][i] = self.p6_20[i-d20_1-d20_2-d20_3-d20_4-d20_5][2]
            self.cv_20[3][i] = self.p6_20[i-d20_1-d20_2-d20_3-d20_4-d20_5][3]
          elif i < d20_1+d20_2+d20_3+d20_4+d20_5+d20_6+d20_7 :
            self.cv_20[0][i] = self.p7_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6][0]
            self.cv_20[1][i] = self.p7_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6][1]
            self.cv_20[2][i] = self.p7_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6][2]
            self.cv_20[3][i] = self.p7_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6][3]
          elif i < d20_1+d20_2+d20_3+d20_4+d20_5+d20_6+d20_7 +d20_8 :
            self.cv_20[0][i] = self.p8_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7][0]
            self.cv_20[1][i] = self.p8_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7][1]
            self.cv_20[2][i] = self.p8_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7][2]
            self.cv_20[3][i] = self.p8_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7][3]
          elif i < d20_1+d20_2+d20_3+d20_4+d20_5+d20_6+d20_7 +d20_8 +d20_9:
            self.cv_20[0][i] = self.p9_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7-d20_8][0]
            self.cv_20[1][i] = self.p9_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7-d20_8][1]
            self.cv_20[2][i] = self.p9_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7-d20_8][2]
            self.cv_20[3][i] = self.p9_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7-d20_8][3]
          elif i < d20_1+d20_2+d20_3+d20_4+d20_5+d20_6+d20_7 +d20_8 +d20_9+d20_10:
            self.cv_20[0][i] = self.p10_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7-d20_8-d20_9][0]
            self.cv_20[1][i] = self.p10_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7-d20_8-d20_9][1]
            self.cv_20[2][i] = self.p10_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7-d20_8-d20_9][2]
            self.cv_20[3][i] = self.p10_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7-d20_8-d20_9][3]
          elif i < d20_1+d20_2+d20_3+d20_4+d20_5+d20_6+d20_7 +d20_8 +d20_9+d20_10+d20_11:
            self.cv_20[0][i] = self.p11_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7-d20_8-d20_9-d20_10][0]
            self.cv_20[1][i] = self.p11_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7-d20_8-d20_9-d20_10][1]
            self.cv_20[2][i] = self.p11_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7-d20_8-d20_9-d20_10][2]
            self.cv_20[3][i] = self.p11_20[i-d20_1-d20_2-d20_3-d20_4-d20_5-d20_6-d20_7-d20_8-d20_9-d20_10][3]

      

        # need to identify sections of task in which error occurs, and isolate it
        control_value = 0.15
        print "Creating Error Tests"

        bound1_1 = self.e1p_1[0][0]
        bound2_1 = self.e8p_2[0][0]
        bound3_1 = self.e3p_3[0][0]
        bound4_1 = self.e7p_4[0][0]
        bound5_1 = self.e3p_5[0][0]
        bound6_1 = self.e6p_6[0][0]
        bound7_1 = self.e9p_7[0][0]
        bound8_1 = self.e10p_8[0][0]
      
        bound1_2 = self.e1p_1[0][1]
        bound2_2 = self.e8p_2[0][1]
        bound3_2 = self.e3p_3[0][1]
        bound4_2 = self.e7p_4[0][1]
        bound5_2 = self.e3p_5[0][1]
        bound6_2 = self.e6p_6[0][1]
        bound7_2 = self.e9p_7[0][1]
        bound8_2 = self.e10p_8[0][1]

        bound1_3 = self.e1p_1[0][2]
        bound2_3 = self.e8p_2[0][2]
        bound3_3 = self.e3p_3[0][2]
        bound4_3 = self.e7p_4[0][2]
        bound5_3 = self.e3p_5[0][2]
        bound6_3 = self.e6p_6[0][2]
        bound7_3 = self.e9p_7[0][2]
        bound8_3 = self.e10p_8[0][2]  

        j = 0
        for i in range(0,len(self.e1p_1)):
            if (bound1_1 - self.e1p_1[i][0] > control_value*bound1_1) or (bound1_2 - self.e1p_1[i][1] > control_value*bound1_2) or (bound1_3 - self.e1p_1[i][2] > control_value*bound1_3):
                j = j + 1
        link_e1 = np.zeros([4,j])
        j = 0
        for i in range(0,len(self.e8p_2)):
            if (bound2_1 - self.e8p_2[i][0] > control_value*bound2_1) or (bound2_2 - self.e8p_2[i][1] > control_value*bound2_2) or (bound2_3 - self.e8p_2[i][2] > control_value*bound2_3):
                j = j + 1
        link_e2 = np.zeros([4,j])
        j = 0
        for i in range(0,len(self.e3p_3)):
            if (bound3_1 - self.e3p_3[i][0] > control_value*bound3_1) or (bound3_2 - self.e3p_3[i][1] > control_value*bound3_2) or (bound3_3 - self.e3p_3[i][2] > control_value*bound3_3):
                j = j + 1
        link_e3 = np.zeros([4,j])
        j = 0
        for i in range(0,len(self.e7p_4)):
            if (bound4_1 - self.e7p_4[i][0] > control_value*bound4_1) or (bound4_2 - self.e7p_4[i][1] > control_value*bound2_2) or (bound4_3 - self.e7p_4[i][2] > control_value*bound4_3):
                j = j + 1
        link_e4 = np.zeros([4,j])
        j = 0
        for i in range(0,len(self.e3p_5)):
            if (bound5_1 - self.e3p_5[i][0] > control_value*bound5_1) or (bound5_2 - self.e3p_5[i][1] > control_value*bound5_2) or (bound5_3 - self.e3p_5[i][2] > control_value*bound5_3):
                j = j + 1
        link_e5 = np.zeros([4,j])
        j = 0
        for i in range(0,len(self.e6p_6)):
            if (bound6_1 - self.e6p_6[i][0] > control_value*bound6_1) or (bound6_2 - self.e6p_6[i][1] > control_value*bound6_2) or (bound6_3 - self.e6p_6[i][2] > control_value*bound6_3):
                j = j + 1
        link_e6 = np.zeros([4,j])
        j = 0
        for i in range(0,len(self.e9p_7)):
            if (bound7_1 - self.e9p_7[i][0] > control_value*bound7_1) or (bound7_2 - self.e9p_7[i][1] > control_value*bound7_2) or (bound7_3 - self.e9p_7[i][2] > control_value*bound7_3):
                j = j + 1
        link_e7 = np.zeros([4,j])
        j = 0
        for i in range(0,len(self.e10p_8)):
            if (bound8_1 - self.e10p_8[i][0] > control_value*bound8_1) or (bound8_2 - self.e10p_8[i][1] > control_value*bound8_2) or (bound8_3 - self.e10p_8[i][2] > control_value*bound8_3):
                j = j + 1
        link_e8 = np.zeros([4,j])    
      
        j = 0
        for i in range(0,len(self.e1p_1)):
            if (bound1_1 - self.e1p_1[i][0] > control_value*bound1_1) or (bound1_2 - self.e1p_1[i][1] > control_value*bound1_2) or (bound1_3 - self.e1p_1[i][2] > control_value*bound1_3):
                j = j + 1
                link_e1[0][j-1]=self.e1p_1[i][0]
                link_e1[1][j-1]=self.e1p_1[i][1]
                link_e1[2][j-1]=self.e1p_1[i][2]
                link_e1[3][j-1]=self.e1p_1[i][3]
        j = 0

        for i in range(0,len(self.e8p_2)):
            if (bound2_1 - self.e8p_2[i][0] > control_value*bound2_1) or (bound2_2 - self.e8p_2[i][1] > control_value*bound2_2) or (bound2_3 - self.e8p_2[i][2] > control_value*bound2_3):
                j = j + 1
                link_e2[0][j-1]=self.e8p_2[i][0]
                link_e2[1][j-1]=self.e8p_2[i][1]
                link_e2[2][j-1]=self.e8p_2[i][2]
                link_e2[3][j-1]=self.e8p_2[i][3]
        j = 0

        for i in range(0,len(self.e3p_3)):
            if (bound3_1 - self.e3p_3[i][0] > control_value*bound3_1) or (bound3_2 - self.e3p_3[i][1] > control_value*bound3_2) or (bound3_3 - self.e3p_3[i][2] > control_value*bound3_3):
                j = j + 1
                link_e3[0][j-1]=self.e3p_3[i][0]
                link_e3[1][j-1]=self.e3p_3[i][1]
                link_e3[2][j-1]=self.e3p_3[i][2]
                link_e3[3][j-1]=self.e3p_3[i][3]
        j = 0

        for i in range(0,len(self.e7p_4)):
            if (bound4_1 - self.e7p_4[i][0] > control_value*bound4_1) or (bound4_2 - self.e7p_4[i][1] > control_value*bound2_2) or (bound4_3 - self.e7p_4[i][2] > control_value*bound4_3):
                j = j + 1
                link_e4[0][j-1]=self.e7p_4[i][0]
                link_e4[1][j-1]=self.e7p_4[i][1]
                link_e4[2][j-1]=self.e7p_4[i][2]
                link_e4[3][j-1]=self.e7p_4[i][3]
        j = 0

        for i in range(0,len(self.e3p_5)):
            if (bound5_1 - self.e3p_5[i][0] > control_value*bound5_1) or (bound5_2 - self.e3p_5[i][1] > control_value*bound5_2) or (bound5_3 - self.e3p_5[i][2] > control_value*bound5_3):
                j = j + 1
                link_e5[0][j-1]=self.e3p_5[i][0]
                link_e5[1][j-1]=self.e3p_5[i][1]
                link_e5[2][j-1]=self.e3p_5[i][2]
                link_e5[3][j-1]=self.e3p_5[i][3]
        j = 0

        for i in range(0,len(self.e6p_6)):
            if (bound6_1 - self.e6p_6[i][0] > control_value*bound6_1) or (bound6_2 - self.e6p_6[i][1] > control_value*bound6_2) or (bound6_3 - self.e6p_6[i][2] > control_value*bound6_3):
                j = j + 1
                link_e6[0][j-1]=self.e6p_6[i][0]
                link_e6[1][j-1]=self.e6p_6[i][1]
                link_e6[2][j-1]=self.e6p_6[i][2]
                link_e6[3][j-1]=self.e6p_6[i][3]
        j = 0

        for i in range(0,len(self.e9p_7)):
            if (bound7_1 - self.e9p_7[i][0] > control_value*bound7_1) or (bound7_2 - self.e9p_7[i][1] > control_value*bound7_2) or (bound7_3 - self.e9p_7[i][2] > control_value*bound7_3):
                j = j + 1
                link_e7[0][j-1]=self.e9p_7[i][0]
                link_e7[1][j-1]=self.e9p_7[i][1]
                link_e7[2][j-1]=self.e9p_7[i][2]
                link_e7[3][j-1]=self.e9p_7[i][3]
        j = 0

        for i in range(0,len(self.e10p_8)):
            if (bound8_1 - self.e10p_8[i][0] > control_value*bound8_1) or (bound8_2 - self.e10p_8[i][1] > control_value*bound8_2) or (bound8_3 - self.e10p_8[i][2] > control_value*bound8_3):
                j = j + 1
                link_e8[0][j-1]=self.e10p_8[i][0]
                link_e8[1][j-1]=self.e10p_8[i][1]
                link_e8[2][j-1]=self.e10p_8[i][2]
                link_e8[3][j-1]=self.e10p_8[i][3]

 #       link_e1 = self.e1p_1
 #       link_e2 = self.e8p_2
 #       link_e3 = self.e3p_3
 #       link_e4 = self.e7p_4
 #       link_e5 = self.e3p_5
 #       link_e6 = self.e6p_6
 #       link_e7 = self.e9p_7
 #       link_e8 = self.e10p_8

        self.e1 = link_e1
        self.e2 = link_e2
        self.e3 = link_e3
        self.e4 = link_e4
        self.e5 = link_e5
        self.e6 = link_e6
        self.e7 = link_e7
        self.e8 = link_e8
        

        self.tests = np.zeros((4,500))
        for i in range(0,500):
            if i < 250:
                k = rand.randint(0,10)
                if k == 0:
                    j = rand.randint(0,len(self.ss_11.transpose())-2)
                    self.tests[0][i] = self.ss_11[0][j]
                    self.tests[1][i] = self.ss_11[1][j]
                    self.tests[2][i] = self.ss_11[2][j]
                    self.tests[3][i] = self.ss_11[3][j]
                elif k == 1:
                    j = rand.randint(0,len(self.ss_1.transpose())-2)
                    self.tests[0][i] = self.ss_1[0][j]
                    self.tests[1][i] = self.ss_1[1][j]
                    self.tests[2][i] = self.ss_1[2][j]
                    self.tests[3][i] = self.ss_1[3][j]
                elif k == 2:
                    j = rand.randint(0,len(self.ss_2.transpose())-2)
                    self.tests[0][i] = self.ss_2[0][j]
                    self.tests[1][i] = self.ss_2[1][j]
                    self.tests[2][i] = self.ss_2[2][j]
                    self.tests[3][i] = self.ss_2[3][j]
                elif k == 3:
                    j = rand.randint(0,len(self.ss_3.transpose())-2)      
                    self.tests[0][i] = self.ss_3[0][j]
                    self.tests[1][i] = self.ss_3[1][j]
                    self.tests[2][i] = self.ss_3[2][j]
                    self.tests[3][i] = self.ss_3[3][j]
                elif k == 4:
                    j = rand.randint(0,len(self.ss_4.transpose())-2)
                    self.tests[0][i] = self.ss_4[0][j]
                    self.tests[1][i] = self.ss_4[1][j]
                    self.tests[2][i] = self.ss_4[2][j]
                    self.tests[3][i] = self.ss_4[3][j]
                elif k == 5:
                    j = rand.randint(0,len(self.ss_5.transpose())-2)
                    self.tests[0][i] = self.ss_5[0][j]
                    self.tests[1][i] = self.ss_5[1][j]
                    self.tests[2][i] = self.ss_5[2][j]
                    self.tests[3][i] = self.ss_5[3][j]
                elif k == 6:
                    j = rand.randint(0,len(self.ss_6.transpose())-2)
                    self.tests[0][i] = self.ss_6[0][j]
                    self.tests[1][i] = self.ss_6[1][j]
                    self.tests[2][i] = self.ss_6[2][j]
                    self.tests[3][i] = self.ss_6[3][j]
                elif k == 7:
                    j = rand.randint(0,len(self.ss_7.transpose())-2)
                    self.tests[0][i] = self.ss_7[0][j]
                    self.tests[1][i] = self.ss_7[1][j]
                    self.tests[2][i] = self.ss_7[2][j]
                    self.tests[3][i] = self.ss_7[3][j]
                elif k == 8:
                    j = rand.randint(0,len(self.ss_8.transpose())-2)
                    self.tests[0][i] = self.ss_8[0][j]
                    self.tests[1][i] = self.ss_8[1][j]
                    self.tests[2][i] = self.ss_8[2][j]
                    self.tests[3][i] = self.ss_8[3][j]
                elif k == 9:
                    j = rand.randint(0,len(self.ss_9.transpose())-2)
                    self.tests[0][i] = self.ss_9[0][j]
                    self.tests[1][i] = self.ss_9[1][j]
                    self.tests[2][i] = self.ss_9[2][j]
                    self.tests[3][i] = self.ss_9[3][j]
                elif k == 10:
                    j = rand.randint(0,len(self.ss_10.transpose())-2)
                    self.tests[0][i] = self.ss_10[0][j]
                    self.tests[1][i] = self.ss_10[1][j]
                    self.tests[2][i] = self.ss_10[2][j]
                    self.tests[3][i] = self.ss_10[3][j]
            else:
                k = rand.randint(0,7)
                if k == 0:
                    j = rand.randint(0,len(self.e8.transpose())-2)
                    self.tests[0][i] = self.e8[0][j]
                    self.tests[1][i] = self.e8[1][j]
                    self.tests[2][i] = self.e8[2][j]
                    self.tests[3][i] = self.e8[3][j]
                elif k == 1:
                    j = rand.randint(0,len(self.e1.transpose())-2)
                    self.tests[0][i] = self.e1[0][j]
                    self.tests[1][i] = self.e1[1][j]
                    self.tests[2][i] = self.e1[2][j]
                    self.tests[3][i] = self.e1[3][j]
                elif k == 2:
                    j = rand.randint(0,len(self.e2.transpose())-2)
                    self.tests[0][i] = self.e2[0][j]
                    self.tests[1][i] = self.e2[1][j]
                    self.tests[2][i] = self.e2[2][j]
                    self.tests[3][i] = self.e2[3][j]
                elif k == 3:
                    j = rand.randint(0,len(self.e3.transpose())-2)
                    self.tests[0][i] = self.e3[0][j]
                    self.tests[1][i] = self.e3[1][j]
                    self.tests[2][i] = self.e3[2][j]
                    self.tests[3][i] = self.e3[3][j]
                elif k == 4:
                    j = rand.randint(0,len(self.e4.transpose())-2)
                    self.tests[0][i] = self.e4[0][j]
                    self.tests[1][i] = self.e4[1][j]
                    self.tests[2][i] = self.e4[2][j]
                    self.tests[3][i] = self.e4[3][j]
                elif k == 5:
                    j = rand.randint(0,len(self.e5.transpose())-2)
                    self.tests[0][i] = self.e5[0][j]
                    self.tests[1][i] = self.e5[1][j]
                    self.tests[2][i] = self.e5[2][j]
                    self.tests[3][i] = self.e5[3][j]
                elif k == 6:
                    j = rand.randint(0,len(self.e6.transpose())-2)
                    self.tests[0][i] = self.e6[0][j]
                    self.tests[1][i] = self.e6[1][j]
                    self.tests[2][i] = self.e6[2][j]
                    self.tests[3][i] = self.e6[3][j]
                elif k == 7:
                    j = rand.randint(0,len(self.e7.transpose())-2)
                    self.tests[0][i] = self.e7[0][j]
                    self.tests[1][i] = self.e7[1][j]
                    self.tests[2][i] = self.e7[2][j]
                    self.tests[3][i] = self.e7[3][j]   
            #print "k = ", k, "i =", i, "#=", self.tests[0:,i]

class vs:
    def init(self, data): # might not need to be transposed
        self.ss_1 = data.ss_1.transpose()
        self.ss_2 = data.ss_2.transpose()
        self.ss_3 = data.ss_3.transpose()
        self.ss_4 = data.ss_4.transpose()
        self.ss_5 = data.ss_5.transpose()
        self.ss_6 = data.ss_6.transpose()
        self.ss_7 = data.ss_7.transpose()
        self.ss_8 = data.ss_8.transpose()
        self.ss_9 = data.ss_9.transpose()
        self.ss_10 = data.ss_10.transpose()
        self.ss_11 = data.ss_11.transpose()
      
        self.cv_10 = data.cv_10.transpose()
        self.cv_20 = data.cv_20.transpose()
        self.e1  = data.e1
        self.e2  = data.e2
        self.e3  = data.e3
        self.e4  = data.e4
        self.e5  = data.e5
        self.e6  = data.e6
        self.e7  = data.e7
        self.e8  = data.e8
      
        self.tests = data.tests

    def info(self):
        print "If you have any questions, don't hesitate to ask Caleb."
        print "This core contains formated data for use in the multimodal system"
        print "The following formated data sets exist:"
        print "self.pX_Y   <-> contains raw data for each step. X is the step, Y is the trial"
        print "self.ss_X   <-> contains formatted (compressed) data for each step. X is the part"
        print "self.cv_X   <-> contains test set of X for cross-validation (X = 10 or 20)"
        print "self.eX     <-> contains error data for trial X (1->8)"
        print "self.tests  <-> 500 element testing vector for testing purposes(first 250 good, second 250 error typed)"
        print "Please note: due to adaptability, some of these sets may have a null column at the end."
        print "Otherwise, formatted sets have the following shape (some may lack element [3])"
        print "[0] -> Force Magnitude"
        print "[1] -> Torque Magnitude"
        print "[2] -> Acceleration Magnitude"
        print "[3] -> Part tag"

if __name__ == "__main__":
    data = tacitus()
    data.init()
    data.single_stages()
    data.cross_validation()
    push_me = vs()
    push_me.init(data)
    print "Saving Core"
    f = open("DataCore","w")
    pickle.dump(push_me,f)
    f.close()
