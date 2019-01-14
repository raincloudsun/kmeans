import matplotlib.pyplot as plt 
import random
 
dataSize= 100
kCount  = 2

# x-axis values 
x = random.sample(range(dataSize), dataSize)
#print x
# y-axis values 
y = random.sample(range(dataSize), dataSize)
#print y
# plotting points as a scatter plot 
#plt.scatter(x, y, label= "stars", color= "green", marker= "*", s=30) 

kx = random.sample(range(dataSize), kCount)
ky = random.sample(range(dataSize), kCount)
#plt.scatter(kx, ky, label= "stars", color= "black", marker= "x", s=50) 


def Euclidean(kx,ky,x,y):
    ss = []
    for i in range(kCount):
        s = []
        for j in range(dataSize):
            #print "%d - %d / %d - %d" % (kx[i],x[j],ky[i],y[j])
            v = (kx[i]-x[j])**2 + (ky[i]-y[j])**2
            s.append(v)

        ss.append(s)

    print ss
    return ss

#'''
def kSet(s):
    r = []
    for i in range(dataSize):
        tmp = []
        for j in range(kCount):
            tmp.append(s[j][i])
            #if s[i][j] > s[i+1][j]:
            #    r.append(i)
            #else
            #    r.append(i+1)
        m = min(tmp)
        r.append(tmp.index(m))

    print r
    return r
#'''

def kSetView(k):
    kColor = "black"
    plt.scatter(kx, ky, label= "stars", color=kColor, marker="o", s=50) 

    for i in range(len(k)):
        if k[i] == 0:
            kColor = "green"
        else:
            kColor = "blue"

        plt.scatter(x[i], y[i], label= "stars", color=kColor, marker= "*", s=30) 
        print i


if __name__ == "__main__":

    #kInit()
    
    sv = Euclidean(kx,ky,x,y)
    k = kSet(sv)
    kSetView(k)

#'''
    # x-axis label 
    plt.xlabel('x - axis') 
    # frequency label 
    plt.ylabel('y - axis') 
    # plot title 
    plt.title('My scatter plot!') 
    # showing legend 
    #plt.legend() 
    # function to show the plot 
    plt.show() 
#'''

# End of File
