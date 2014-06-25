#!/usr/bin/env python
from numpy import *
import scipy.spatial.distance as ssd
import matplotlib.pyplot as plt
import time

def load_points():
    f = open('Original_Points','r')
    a = load(f)
    f.close()
    return a

def calc_dist(e1,e2,mode=1):
    if mode == 1:
        return ssd.euclidean(e1,e2)
    elif mode == 2:
        return ssd.cityblock(e1,e2)
    elif mode == 3:
        return ssd.cosine(e1,e2)

def plot_points(data, test_case = array([0,0])):
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

def sort_max(data):
    max = 0
    j = 0
    hold = j
    for i in data:
        if i > max:
            max = i
            hold = j
        j = j + 1
    return hold

def pass_me(i,loc,count):
    j = 1
    for a in loc:
        if a == i:
            j = 0
    return j

def sort_min(data,k):
    loc = zeros(k)
    for count in range(k):
        min = 99999
        j = 0
        for i in data :
            if i < min and pass_me(j,loc,count) == 1:
                min = i
                loc[count] = j
            j = j + 1
    return loc.astype(int)

def knn(pdata, test_case = array([0,0]), k = 3, options = 4):
    results = array([])
    storage = array([])
    counter = 0
    for i in pdata:
        results.resize((counter+1,1))
        storage.resize((counter+1,2))
        results[counter] = calc_dist(pdata[counter][:2],test_case)
        storage[counter][0] = results[counter]
        storage[counter][1] = pdata[counter][-1]
        counter = counter + 1    
    sai = sort_min(results,k)
    clearance = 0
    i = 0
    while i < k:
        if storage[sai[i]][0] < 1:
            clearance = 1
        i = i + 1
    i = 0

    if clearance == 0:
        print "WARNING: This node is not close to any previously found nodes."
        while i < k:
            if storage[sai[i]][0] > 5:
                clearance = clearance + 1
            i = i + 1
        if clearance == len(sai):
            print "ERROR: This node is far too distant from any previously observed nodes."
            return -1
   
    terms = array([])
    terms.resize((k,1))
    for i in range(k):
        terms[i] = storage[sai[i]][1]
    return stats(terms,k, options)

def stats(nodes, total, options):
    t = zeros(options)
    for i in nodes:
        j = round(i)
        t[j] = t[j] + 1
    t.astype(int)
    s = sort_max(t)
    print "Confidence: ", float(t[s])/float(total)*100,"%"
    return s

def main() :
    pdata = load_points()
    test_case = array([3,5])
    print "Test Case is:", test_case
    plot_points(pdata,test_case)
    start = time.clock()       
    terms = knn(pdata,test_case,7,4)
    print "selected node is:"
    print terms
    print "time required:"
    print time.clock()-start
    
if __name__ == '__main__':
    main()
