#!/usr/bin/env python

# trans.py -> transformation service
# Caleb Little, HRL Summer 2014
# Please read all relavent information below before using


# Version 2: Ballistic Gel
# Changes:
# Added additional dimension reduction systems (LLE,PCA,Isomap)
# Known potential issues:
# Will need seperate services for each modality (different server messages)

import numpy as np
import rospy
from minisom import MiniSom
import os.path
import roslib; roslib.load_manifest('manifold_systems')
from manifold_systems.srv import *
from sklearn import manifold, datasets, decomposition, ensemble, lda, random_projection
import cPickle as pickle

# Operating Algorithm Control:
mode = 4 # 1 = SOM, 2 = LLE, 3 = PCA, 4 = Isomap
# Change the number of mode to select which algorithm to use

class Som:
    def init(self):
        self.core = MiniSom(50,50,6,sigma=.8,learning_rate=.5) # needs to match generating minisom command (specifically the load_map)
        self.core.load_map()
        self.callme = rospy.Service("mapping", Compute, self.callback)
	print "SOM setup complete"
    
    def callback(self, data):
        vector = np.array([data.fx, data.fy, data.fz, data.tx, data.ty, data.tz]) # format as needed
	print vector        
	w = self.core.winner(vector)
        return w[0],w[1]

class Lle:
    def init(self):
	f = open('LLE', 'r')
	self.core = pickle.load(f)
	f.close()
	self.callme = rospy.Service("mapping", Compute, self.callback)
	print "LLE setup complete"

    def callback(self,data):
	vector = np.array([data.fx, data.fy, data.fz, data.tx, data.ty, data.tz]) # format as needed
	print vector
	w = self.core.transform(vector)
	return w[0][0],w[0][1]

class Pca:
    def init(self):
	f = open('PCA', 'r')
	self.core = pickle.load(f)
	f.close()
	self.callme = rospy.Service("mapping", Compute, self.callback)
	print "PCA setup complete"

    def callback(self,data):
	vector = np.array([data.fx, data.fy, data.fz, data.tx, data.ty, data.tz]) # format as needed
	print vector
	w = self.core.transform(vector)
	return w[0][0],w[0][1]

class Isomap:
    def init(self):
	f = open('Isomap', 'r')
	self.core = pickle.load(f)
	f.close()
        print "loaded map"
	self.callme = rospy.Service("mapping", Compute, self.callback)
	print "Isomap setup complete"

    def callback(self,data):
	vector = np.array([data.fx, data.fy, data.fz, data.tx, data.ty, data.tz]) # format as needed
	print vector
	vector = np.array([vector]) # Impliment the double reference issue in isomap
	w = self.core.transform(vector)
	return w[0][0],w[0][1]

def boot():
    rospy.init_node('Remap_System')
    print "Node Established"

    if mode == 1:
	print "entering SOM mode"
    	if os.path.isfile('SOM') == False:
        	print "System cannot find SOM file. Did you run dr and then obtain the resultant SOM file?"
        	return -1
    	goal = Som()
    if mode == 2:
	print "entering LLE mode"
	if os.path.isfile('LLE') == False:
		print "System cannot find LLE file. Did you run dr and then obtain the resultant LLE file?"
		return -1
	goal = Lle()
    if mode == 3:
	print "entering PCA mode"
	if os.path.isfile('PCA') == False:
		print "System cannot find PCA file. Did you run dr and then obtain the resultant PCA file?"
		return -1
	goal = Pca()
    if mode == 4:
	print "entering Isomap mode"
	if os.path.isfile('Isomap') == False:
		print "System cannot find Isomap file. Did you run dr adn then obtain the resultant Isomap file?"
		return -1
        goal = Isomap()

    goal.init()
    rospy.spin()

if __name__ == '__main__':
    boot()
