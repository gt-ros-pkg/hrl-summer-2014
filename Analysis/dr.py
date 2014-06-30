# dr.py -> dimesion reduction system
# Caleb Little, HRL Summer 2014
# drmap = data map
import numpy as np
from minisom import MiniSom
from sklearn import manifold, datasets, decomposition, ensemble, lda, random_projection
import pylab as pl
import cPickle as pickle

window_control = 0.7 # Don't touch this unless you know what it does

mode = 4 #1 = SOM, 2 = LLE, 3 = PCA, 4 = Isomap
fresh_data = 1 # 1 = yes, 0 = load old data

# get data (uses sklearn atm)
digits = datasets.load_digits(n_class=4)
data = digits.data # matrix where each row is a vector that represent a digit.
num = digits.target # num[i] is the digit represented by data[i]
n_samples, n_features = data.shape
n_neighbors = 30

if mode == 1:
    print "Using SOM"
    drmap = MiniSom(20,20,64,sigma=.8,learning_rate=0.5) # Replace 64 with the dimensions of desired target
    if fresh_data == 1:
        print "Training..."
        drmap.train_random(data,1500) # random training
        print "\n...ready!"
    elif fresh_data == 0:
        print "Loading Data"
        drmap.load_map() # Use this to load a previously existing map

    # plotting the results
    from pylab import text,show,cm,axis,figure,subplot,imshow,zeros
    figure(1)
    im = 0
    result = np.array([])
    for x,t in zip(data,num): # scatterplot
     w = drmap.winner(x)
     result.resize((im+1,3))
     result[im][0]=w[0]
     result[im][1]=w[1]
     result[im][2]=num[im]
     text(w[0]+.5, w[1]+.5, str(t), color=cm.Dark2(t / 4.), fontdict={'weight': 'bold', 'size': 11})
     im = im + 1
     axis([0,drmap.weights.shape[0],0,drmap.weights.shape[1]])

    # Save SOM file
    drmap.save_map()

else:
    if mode == 2:
        print "Using LLE"
        construct = manifold.LocallyLinearEmbedding(n_neighbors, n_components=2, method='standard')
        if fresh_data == 1:
            print "Training..."
            drmap = construct.fit(data)
            print "\n...ready!"
            f = open('LLE','w')
            pickle.dump(drmap,f)
            f.close()
        else:
            print "Loading Data"
            f = open('LLE', 'r')
            drmap = pickle.load(f)
            f.close()
            
    elif mode == 3:
        print "Using PCA"
        construct = decomposition.TruncatedSVD(n_components=2)
        if fresh_data == 1:
            print "Training..."
            drmap = construct.fit(data)
            print "\n...ready!"
            f = open('PCA','w')
            pickle.dump(drmap,f)
            f.close()
        else:
            print "Loading Data"
            f = open('PCA','r')
            drmap = pickle.load(f)
            f.close()

    elif mode == 4:
        print "Using Isomap"
        construct = manifold.Isomap(n_neighbors, n_components=2)
        if fresh_data == 1:
            print "Training..."
            drmap = construct.fit(data)
            print "\n...ready!"
            f = open('Isomap','w')
            pickle.dump(drmap,f)
            f.close()
        else:
            print "Loading Data"
            f = open('Isomap','r')
            drmap = pickle.load(f)
            f.close()

    from pylab import text,show,cm,axis,figure,subplot,imshow,zeros
    figure(1)
    im = 0
    result = np.array([])
    for x,t in zip(data,num): # scatterplot
     if mode == 4:
         x = np.array([x])
     w = drmap.transform(x)
     result.resize((im+1,3))
     result[im][0]=w[0][0]
     result[im][1]=w[0][1]
     result[im][2]=num[im]
     text(w[0][0]+.5, w[0][1]+.5, str(t), color=cm.Dark2(t / 4.), fontdict={'weight': 'bold', 'size': 11})
     im = im + 1
    print result
    x_min = np.amin(result[:,0])
    x_max = np.amax(result[:,0])
    y_min = np.amin(result[:,1])
    y_max = np.amax(result[:,1])
    print x_min
    print x_max
    print y_min
    print y_max
    if mode != 2:
        axis([x_min,x_max,y_min,y_max])
    else :
        axis([0,x_max+window_control,0,y_max+window_control])

show()
f = open('Original_Points','w')
np.save(f,result)
f.close()
