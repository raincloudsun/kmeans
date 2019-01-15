import matplotlib.pyplot as plt 
import random
import numpy as np
 

dataSize    = 500
updLimits   = 100

plt.ion()
fig, ax = plt.subplots()

sc = []
retryFlag= [0] * kCount
kx = random.sample(range(dataSize), kCount)
ky = random.sample(range(dataSize), kCount)

def Euclidean(kCount,x,y):
    ss = []
    for i in range(kCount):
        s = []
        for j in range(dataSize):
            v = (kx[i]-x[j])**2 + (ky[i]-y[j])**2
            s.append(v)

        ss.append(s)

    return ss

def kSet(kCount,s):
    res = []
    for i in range(dataSize):
        tmp = []
        for j in range(kCount):
            tmp.append(s[j][i])
        m = min(tmp)
        res.append(tmp.index(m))

    return res


def kSetCentroid(kCount,k):
    colorSeed = 32
    cmap = plt.cm.get_cmap("nipy_spectral", 256)

    sumx = [0] * len(k)
    sumy = [0] * len(k)
    count= [0] * len(k)
    for i in range(len(k)):
        plt.scatter(x[i], y[i], label="circle", color=cmap(k[i]*colorSeed), marker= "o", s=10) 

        # kset sum
        sumx[k[i]] += x[i]
        sumy[k[i]] += y[i]
        count[k[i]]+= 1

    for i in range(kCount):
        #if len(sc) != kCount :
        res = ax.scatter(kx[i], ky[i], label="stars", color=cmap(i*colorSeed), marker="*", s=70)
        sc.append(res)

        # centroid campare
        avgx = sumx[i] / count[i]
        avgy = sumy[i] / count[i]
        if kx[i]==avgx and ky[i]==avgy:
            retryFlag[i] = 1
            print "ref %d" % i

        # next centroid
        kx[i] = avgx
        ky[i] = avgy


def kmeans(kCount,x,y):
    for i in range(updLimits):
        sv = Euclidean(kCount,x,y)
        kr = kSet(kCount,sv)
        kSetCentroid(kCount,kr)
        
        trueCount = 0
        for j in range(kCount):
            if retryFlag[j] == 1: 
                trueCount += 1

        plt.pause(0.1)

        if trueCount == kCount:
            print "kset centroid complete !"
            break
        else:
            print "retry kset-centroid...%d" % trueCount
            ax.clear()

        #reset centroid point
        #fig.canvas.draw_idle()
        #plt.draw() 

    plt.waitforbuttonpress()

if __name__ == "__main__":

    # cluster count
    k = 5

    # x, y coordinates
    x = random.sample(range(dataSize), dataSize)
    y = random.sample(range(dataSize), dataSize)

    # run k-means
    kmeans(k, x, y)
    

# End of File
