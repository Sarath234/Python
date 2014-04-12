import sys, math, random, numpy
import matplotlib.pyplot as plt


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

def getClusterLabels(data,centroids):
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
        print("Clusetr no " , i , "Centroid " , centroid)
    
    return cluster_list

def findCentroid(c):
    c.asArray()
    centroid = c.findMean()
    return centroid

def plotCluster(cList):
    i = 0
    colors = list("bgrcmyk")
    for cluster in cList:
        color = colors[i % len(colors)]
        print(cluster.getPoints())
        x,y = cluster.getPoints()[:,0],cluster.getPoints()[:,1]
        #plt.scatter(x,y,c=color)
        #print(cluster.getCentroid())
        #plt.scatter(cluster.getCentroid()[0],cluster.getCentroid()[1],s = 100,c = color,marker = '+')
        #plt.plot(mList[i][0],mList[i][1],color)
        #i += 1
    #plt.show()

def main():
    data = init_board(10) #initialize the data
    print(data.tolist())
    print("")
    no_of_clusters = 5 #no of clusters
    no_of_cores = 3 #no of cores
    splitData = list()
    x = split_list(data.tolist(),no_of_cores) #generator object containing the split
    
    for i in range(0,no_of_cores):
        dataOnCore = next(x)
        splitData.append(dataOnCore)
        print(dataOnCore)
        print("")

    newCentroidList = getRandomCentroids(no_of_clusters)

    print(newCentroidList)

    label_list = list()
    accumulated_data = list()
    
    for i, ind_data in enumerate(splitData):
        print("")
        print(ind_data)
        label = getClusterLabels(ind_data,newCentroidList)
        print("")
        print(label)

        label_list.extend(label.tolist())
        accumulated_data.extend(ind_data)

    print("")
    print(accumulated_data)
    print("")
    print(label_list)
    
    cluster_list = getCluster(accumulated_data,label_list,newCentroidList)

    oldCentroidList = newCentroidList
    newCentroidList = list()
    for i, c in enumerate(cluster_list):
        print(i)
        print("Cluster", i, c.getPoints())
        print("Centroid", c.getCentroid())
        print("")
        #print(c.getPoints())
        if c.getPoints():
            centroid = findCentroid(c).tolist()
        else:
            centroid = c.getCentroid()
            #print("Empty")
        #print("New Centroid",centroid)
        newCentroidList.append(centroid)

    newCentroidList = numpy.array(newCentroidList)
    oldCentroidList = numpy.array(oldCentroidList)
    #plotCluster(cluster_list)

        
            
        
        
    
main()
