#!/usr/bin/env python

# k-nn.py -> k Next Neighbors implimentation
# Caleb Little, HRL Summer 2014
# Please read all relavent information below before using 

# Version 3 : The Laws of this World
# Changes: 
# Autoadjusted distances for anomoly detection based on 
# data spread. Sensitivity can be adjusted below.
# Currently, an error requires an error of 5 times
# that of a warning.

import rospy
import os.path
from numpy import *
import scipy.spatial.distance as ssd
import matplotlib.pyplot as plt
import time
from geometry_msgs.msg import WrenchStamped, Wrench
from std_msgs.msg import Float64
import roslib; roslib.load_manifest('manifold_systems')
from manifold_systems.srv import *
import random as rand

# Sensitivity Control Section:
tol = 10 # 1 is normal operation. 
# Increasing the value of tol will cause the acceptable 
# distance between nodes to increase

class vs:
    def bacon():
        print "bacon"

class k_nn:
    def load_points(self):
        f = open('Original_Points','r')
        self.base = load(f)
        f.close()
        self.get_points = rospy.ServiceProxy('mapping',Compute)
        self.conclusion = rospy.Publisher('FT_Results', Float64)
        self.current_state = -1
        self.count = 11
        rospy.Subscriber('Current_State', Float64, self.status)

        
    def status(self,data):
        print "New State entered!"
        self.current_state = data.data
        self.current_state.astype(int)

    def calc_dist(self, e1,e2,mode=1):
        if mode == 1:
            return ssd.euclidean(e1,e2)
        elif mode == 2:
            return ssd.cityblock(e1,e2)
        elif mode == 3:
            return ssd.cosine(e1,e2)

    def plot_points(self, data, test_case = array([0,0])):
        for i in data:
            if i[-1] == 1:
                plt.plot(i[0],i[1], 'ro')
            elif i[-1] == 2:
                plt.plot(i[0],i[1], 'b*')
            elif i[-1] == 3:
                plt.plot(i[0],i[1], 'g^')
            elif i[-1] == 4:
                plt.plot(i[0],i[1], 'mx')
	    elif i[-1] == 5:
		plt.plot(i[0],i[1], 'mo')
	    elif i[-1] == 6:
		plt.plot(i[0],i[1], 'b^')
	    elif i[-1] == 7:
		plt.plot(i[0],i[1], 'g*')
	    elif i[-1] == 8:
		plt.plot(i[0],i[1], 'rx')
        plt.plot(test_case[0],test_case[1], 'yp')
        print "Red Circle -> 1"
        print "Blue Star -> 2"
        print "Green Triangle -> 3"
        print "Magenta X -> 4"
        print "Magenta Circle -> 5"
        print "Blue Triangle -> 6"
        print "Green Star -> 7"
        print "Red X -> 8"
        plt.show()

    def pass_me(self,i,loc,count):
        j = 1
        for a in loc:
            if a == i:
                j = 0
        return j

    def sort_min(self, data,k):
        loc = zeros(k)
        for count in range(k):
            min = 99999
            j = 0
            for i in data :
                if i < min and self.pass_me(j,loc,count) == 1:
                    min = i
                    loc[count] = j
                j = j + 1
        return loc.astype(int)

    def knn(self, pdata, test_case = array([0,0]), k = 3, options = 4):
        results = array([])
        storage = array([])
        counter = 0
        for i in pdata:
            results.resize((counter+1,1))
            storage.resize((counter+1,2))
            results[counter] = self.calc_dist(pdata[counter][:2],test_case)
            storage[counter][0] = results[counter]
            storage[counter][1] = pdata[counter][-1]
            counter = counter + 1    
        sai = self.sort_min(results,k)
        clearance = 0
        i = 0

	x_min = amin(pdata[:,0])
	x_max = amax(pdata[:,0])
        y_min = amin(pdata[:,1])
        y_max = amax(pdata[:,1])
        if x_max-x_min > y_max-y_min:
         scale = x_max-x_min
        else:
         scale = y_max-y_min
        #print "Calculated scale is: ", scale
        tier1_issue = scale/20*tol
        tier2_issue = scale/4*tol
        #print "tiers are: "
        #print "tier1 = ", tier1_issue
        #print "tier2 = ", tier2_issue

        while i < k:
            if storage[sai[i]][0] < tier1_issue:
                clearance = 1
            i = i + 1
        i = 0

        if clearance == 0:
            print "WARNING: This node is not close to any previously found nodes."
            while i < k:
                if storage[sai[i]][0] > tier2_issue:
                    clearance = clearance + 1
                i = i + 1
            if clearance == len(sai):
                print "ERROR: This node is far too distant from any previously observed nodes."
                return zeros(options-1)
   
        terms = array([])
        terms.resize((k,1))
        for i in range(k):
            terms[i] = storage[sai[i]][1]
        return self.stats(terms,k, options)

    def stats(self, nodes, total, options):
        t = zeros(options+1)
        for i in nodes:
            j = round(i)
            if j == 0:
                print "GOT ANOTHER ONE OF THESE THINGS..."
            else:
                t[j] = t[j] + 1
        t.astype(int)
        return t

    def main(self, data):
        #print "made it up to service point"
        rospy.wait_for_service('mapping')
        pdata = self.base
        test_case = zeros(2)
        #test_block = self.get_points(data.wrench.force.x,data.wrench.force.y,data.wrench.force.z,data.wrench.torque.x,data.wrench.torque.y,data.wrench.torque.z)
        test_block = self.get_points(data[0],data[1],data[2],data[3],data[4],data[5])
        test_case[0] = test_block.x
        test_case[1] = test_block.y
        #print "Current Point is:", test_case
        #self.plot_points(pdata,test_case) #Supressed for computational reasons ######################################
        #start = time.clock()       
        terms = self.knn(pdata,test_case,self.count,8) #First number is k, second is total distinct sets in the data
        #print "selected node is:"
        #print terms
        #print "time required:"
        #print time.clock()-start
        term = terms[self.current_state]/self.count*100
        print "Likely hood of current state:", term
        print "All states:", terms
        self.conclusion.publish(term)
        return term

def ros_code():
    rospy.init_node('k_NN', anonymous=True)
    print "Node Established."
    if os.path.isfile('Original_Points') == False:
        print "System cannot find Original_Points. Did you run SOM and then obtain the resultant original points file, and is it located in the same folder as this execution?"
        return -1
    handler = k_nn()
    handler.load_points()
    #rospy.Subscriber("/ft/l_gripper_motor", WrenchStamped, handler.main)
    f = open("DataCore", 'r')
    current = load(f)
    f.close()
    value = 0
    test_point_v = [10,19,28,37,46,55,64,73,82,91,100] ###########################################################################################################################################################
    rand.seed(rospy.Time.now())
    j = 0
    TP = 0
    FP = 0
    test_values = array([])
    test_values.resize((250,2))

    for k in range(0,250):
        i = rand.randint(0,8)
        if i % 8 == 1:
            j = rand.randint(0,len(current.cv_21_1x)-1)
        elif i % 8 == 2:
            j = rand.randint(0,len(current.cv_21_2x)-1)
        elif i % 8 == 3:
            j = rand.randint(0,len(current.cv_21_3x)-1)
        elif i % 8 == 4:
            j = rand.randint(0,len(current.cv_21_4x)-1)
        elif i % 8 == 5:
            j = rand.randint(0,len(current.cv_21_5x)-1)
        elif i % 8 == 6:
            j = rand.randint(0,len(current.cv_21_6x)-1)
        elif i % 8 == 7:
            j = rand.randint(0,len(current.cv_21_7x)-1)
        elif i % 8 == 0:
            j = rand.randint(0,len(current.cv_21_8x)-1)
        for m in test_values[:,1]:
            if m == j:
                j == j + i % 5
        test_values[k][0] = i
        test_values[k][1] = j

    for test_point in test_point_v:
        TP = 0
        FP = 0
        for k in range(0,250):
            print "Current Trial: ", k
            #print i
            i = test_values[k][0]
            j = test_values[k][1]
            if i % 8 == 1:
                #print "Using data #: ", j, "Calling 1"
                handler.current_state = 1
                value = handler.main(current.cv_21_1x[j])
            elif i % 8 == 2:
                #print "Using data #: ", j, "Calling 2"
                handler.current_state = 2
                value = handler.main(current.cv_21_2x[j])
            elif i % 8 == 3:
                #print "Using data #: ", j, "Calling 3"
                handler.current_state = 3
                value = handler.main(current.cv_21_3x[j])
            elif i % 8 == 4:
                #print "Using data #: ", j, "Calling 4"
                handler.current_state = 4
                value = handler.main(current.cv_21_4x[j])
            elif i % 8 == 5:
                #print "Using data #: ", j, "Calling 5"
                handler.current_state = 5
                value = handler.main(current.cv_21_5x[j])
            elif i % 8 == 6:
                #print "Using data #: ", j, "Calling 6"
                handler.current_state = 6
                value = handler.main(current.cv_21_6x[j])
            elif i % 8 == 7:
                #print "Using data #: ", j, "Calling 7"
                handler.current_state = 7
                value = handler.main(current.cv_21_7x[j])
            elif i % 8 == 0:
                #print "Using data #: ", j, "Calling 8"
                handler.current_state = 8
                value = handler.main(current.cv_21_8x[j])
            if value < test_point: 
                FP = FP + 1

        for k in range(0,250):
            print "Current Trial: ", k
            if i % 8 == 1:
                #print "Using data #: ", j
                handler.current_state = 3
                value = handler.main(current.cv_21_1x[j])
            elif i % 8 == 2:
                #print "Using data #: ", j
                handler.current_state = 4
                value = handler.main(current.cv_21_2x[j])
            elif i % 8 == 3:
                #print "Using data #: ", j
                handler.current_state = 5
                value = handler.main(current.cv_21_3x[j])
            elif i % 8 == 4:
                #print "Using data #: ", j
                handler.current_state = 6
                value = handler.main(current.cv_21_4x[j])
            elif i % 8 == 5:
                #print "Using data #: ", j
                handler.current_state = 7
                value = handler.main(current.cv_21_5x[j])
            elif i % 8 == 6:
                #print "Using data #: ", j
                handler.current_state = 8
                value = handler.main(current.cv_21_6x[j])
            elif i % 8 == 7:
                #print "Using data #: ", j
                handler.current_state = 1
                value = handler.main(current.cv_21_7x[j])
            elif i % 8 == 0:
                #print "Using data #: ", j
                handler.current_state = 2
                value = handler.main(current.cv_21_8x[j])
            if value < test_point: 
                TP = TP + 1

        print "Test Value = ", test_point
        print "TP = ", TP
        print "FP = ", FP
        #rospy.spin()
    
if __name__ == '__main__':
    ros_code()
