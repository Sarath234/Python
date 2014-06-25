import sys, math, random, numpy
import matplotlib.pyplot as plt
from mpi4py import MPI
from numpy import *
import time
comm=MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
no_of_cores=size-1
class Cluster:
    def __init__(self):
        self.points = []

    def addPoints(self, point):
        self.points.append(point)
        return self.points

    def getPoints(self):
        return self.points
    
    def printCluster(self):
        print(self.points)

    def asArray(self):
        #print(self.points)
        self.points = numpy.array(self.points)
        #print(self.pointsArray)

    def findMean(self):
        return numpy.mean(self.points,axis=0);

    def setCentroid(self,c):
        self.centroid = c
        #print("Centroid = ",self.centroid)

    def getCentroid(self):
        return self.centroid

def split_list(L, n):
    assert type(L) is list, "L is not a list"
    a = int(len(L)/n)
    for i in range(0,n-1):
        yield L[i*a:i*a+a]
    yield L[(n-1)*a:len(L)+1]

def init_board(N):
    X = numpy.array([(round(random.uniform(-10, 10),2), round(random.uniform(-10, 10),2)) for i in range(N)])
    return X

def getRandomCentroids(k):
    c = numpy.array([(random.uniform(-10, 10), random.uniform(-10, 10)) for i in range(k)])
    return c

def getClusterLabel(data,centroids):
    label = []
               
    for d in data:
        dist = []
        for i, c in enumerate(centroids):
            dist = numpy.append(dist,numpy.linalg.norm(d-c))
        #print (dist)
        #print(numpy.argmin(dist))
        ind = numpy.argmin(dist)
        label = numpy.append(label,ind)

    return label

def getCluster(data,label,newCentroidList):
    
    cluster_list = []
    for i, c in enumerate(newCentroidList):
        cluster_list.append(Cluster())
           
    #print (label)
    for i, l in enumerate(label):
        l = int(l)
        #print(l)
        #print(data[i])
        cluster_list[l].addPoints(data[i])
        
    for i, centroid in enumerate(newCentroidList):
        cluster_list[i].setCentroid(centroid)
        #print("Clusetr no " , i , "Centroid " , centroid)
    
    return cluster_list

def findCentroid(c):
    c.asArray()
    centroid = c.findMean()
    return centroid

def plotCluster(cList):
    i = 0
#    colors = list("bgrcmyk")
    colors = list("_x.+|")
    for cluster in cList:
	if (cluster.getPoints()==[]):
	    print("Null")
	else:       
	    color = colors[i % len(colors)]
        #print(cluster.getPoints())
            x,y = cluster.getPoints()[:,0],cluster.getPoints()[:,1]
            plt.figure(1)
            plt.scatter(x,y,marker=color)#c=color)
            
        #print(cluster.getCentroid())
        #plt.scatter(cluster.getCentroid()[0],cluster.getCentroid()[1],s = 100,c = color,marker = '+')
        #plt.plot(mList[i][0],mList[i][1],color)
            i += 1
    plt.show()
#    plt.draw()
#    time.sleep(5)
def main():

    if rank==0:
        data = init_board(50) #loadtxt('data.txt') #init_board(10) #initialize the data
        #print(data.tolist())
        #print("")
        no_of_clusters = 5 #no of clusters
        splitData = list()
        x = split_list(data.tolist(),no_of_cores) #generator object containing the split
 
        newCentroidList = getRandomCentroids(no_of_clusters)#loadtxt('centroid.txt') #getRandomCentroids(no_of_clusters)

        for i in range(0,no_of_cores):
            dataOnCore = next(x)
            splitData.append(dataOnCore)
            comm.send(dataOnCore,dest=i+1,tag=1)
            #print(dataOnCore)
            #print("")        
    else:
        ind_data=comm.recv(source=0,tag=1)

#        print(newCentroidList)

    for k in range(0,20):
        if rank==0:
            for i in range(0,no_of_cores):
                comm.send(newCentroidList,dest=i+1,tag=2)
        
        if rank!=0:
            newCentroidList=comm.recv(source=0,tag=2)
            label=getClusterLabel(ind_data,newCentroidList)
            comm.send(label,dest=0,tag=rank)
        if rank==0:
            label_list = list()
            accumulated_data = list()
            for j in range(0,no_of_cores):
                label=comm.recv(source=j+1,tag=j+1) 
                label_list.extend(label.tolist())
                
            accumulated_data = data 

    
            cluster_list = getCluster(accumulated_data,label_list,newCentroidList)
            
            oldCentroidList = newCentroidList
            newCentroidList = list()
            for i, c in enumerate(cluster_list):
                #print(i)
                #print("Cluster", i, c.getPoints())
                #print("Centroid", c.getCentroid())
                #print("")
                if c.getPoints():
                    centroid = findCentroid(c).tolist()
                else:
                    centroid = c.getCentroid()
       
                newCentroidList.append(centroid)

            newCentroidList = numpy.array(newCentroidList)
            oldCentroidList = numpy.array(oldCentroidList)
    	    plotCluster(cluster_list)
main()
