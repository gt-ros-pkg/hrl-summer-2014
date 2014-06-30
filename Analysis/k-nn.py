#!/usr/bin/env python

# Version 3 - CL - Laws of this World
# To DO:
# Test (obviously)
# In order to do above, I'll need test data and a script of the right size.
# Please Note: This version is designed for Force_Torque (modify for other modalities)
# everything else seems to be working at least for the most part(haven't made 
# it past the get current position call

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

class k_nn:
    
    def load_points(self):
        f = open('Original_Points','r')
        self.base = load(f)
        f.close()
        self.get_points = rospy.ServiceProxy('mapping',Compute)
        self.conclusion = rospy.Publisher('FT_Results', Float64)
        self.current_state = -1
        self.count = 7
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
            if i[-1] == 0:
                plt.plot(i[0],i[1], 'ro')
            elif i[-1] == 1:
                plt.plot(i[0],i[1], 'b*')
            elif i[-1] == 2:
                plt.plot(i[0],i[1], 'g^')
            elif i[-1] == 3:
                plt.plot(i[0],i[1], 'mx')
        plt.plot(test_case[0],test_case[1], 'kp')
        plt.show()

    def pass_me(self, i,loc,count):
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
        tier1_issue = scale/20
        tier2_issue = scale/4
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
                return -1
   
        terms = array([])
        terms.resize((k,1))
        for i in range(k):
            terms[i] = storage[sai[i]][1]
        return self.stats(terms,k, options)

    def stats(self, nodes, total, options):
        t = zeros(options)
        for i in nodes:
            j = round(i)
            t[j] = t[j] + 1
        t.astype(int)
        return t

    def main(self, data):
        print "made it up to service point"
        rospy.wait_for_service('mapping')
        pdata = self.base
        print pdata
        test_case = array(2)
        test_case[0],test_case[1] = self.get_points(data.wrench.force.x,data.wrench.force.y,data.wrench.force.z,data.wrench.torque.x,data.wrench.torque.y,data.wrench.torque.z) 
        print "Current Point is:", test_case
        self.plot_points(pdata,test_case)
        start = time.clock()       
        terms = self.knn(pdata,test_case,self.count,4) #First number is k, second is total distinct sets in the data
        print "selected node is:"
        print terms
        print "time required:"
        print time.clock()-start
        term = terms[self.current_state]/self.count*100
        print "Likely hood of current state:", term
        self.conclusion.publish(term)

def ros_code():
    rospy.init_node('k_NN', anonymous=True)
    print "Node Established."
    if os.path.isfile('Original_Points') == False:
        print "System cannot find Original_Points. Did you run SOM and then obtain the resultant original points file, and is it located in the same folder as this execution?"
        return -1
    handler = k_nn()
    handler.load_points()
    rospy.Subscriber("/ft/l_gripper_motor", WrenchStamped, handler.main)
    rospy.spin()
    
if __name__ == '__main__':
    ros_code()
