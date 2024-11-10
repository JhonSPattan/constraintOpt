import numpy as np

class CircularLinklist:
    '''
    this class recive and return value to index value
    '''
    def __init__(self,value:np.array = None,index:int = -1) -> None:
        self.prevnode = None
        self.nextnode = None
        self.value = value
        self.index = index

    def setNeighborhood(self,prevnode:object,nextnode:object)->None:
        self.nextnode = nextnode
        self.prevnode = prevnode
    
    def setNext(self,nextnode:object)->None:
        self.nextnode = nextnode

    def setPrev(self,prevnode:object)->None:
        self.prevnode = prevnode

    def getPrev(self)->object:
        return self.prevnode
    
    def getNext(self)->object:
        return self.nextnode
    
    def getValue(self):
        return self.value
    
    def getIndex(self):
        return self.index
    
    
# class RingTopology:
#     def __init__(self,nodeSet:np.array,nodeNum:int) -> None:
#         self.nodeSet = nodeSet
#         self.nodeNum = nodeNum


#     def getNextPopulation(self,index:int=0,n:int=1)->np.array:
#         negiborSet = []
#         for j in range(1,n+1):
#             # print(self.ring[index-j].getCurr()," ",index-j)
#             negiborSet.append(self.ring[index-j].getCurr())

#         for j in range(1,n+1):
#             # print(self.ring[index+j].getCurr()," ",index+j)
#             if index+j >= self.nodeNum:
#                 negiborSet.append(self.ring[self.nodeNum-(index-j)].getCurr())
#                 continue
#             negiborSet.append(self.ring[index+j].getCurr())
        
#         return np.array(negiborSet)

#     def getBestNegiborhood(self,fitness:np.array)->int:
#         minVal = np.where(np.min(fitness) == fitness)[0][0]
#         return minVal


#     def createdistanceMatrix(self)->None:
#         distance = np.zeros((self.nodeNum,self.nodeNum))
#         for i in range(self.nodeNum):
#             for j in range(self.nodeNum):
#                 if i == j:
#                     distance[i][j] = float('inf')
#                     continue
#                 distance[i][j] = np.linalg.norm(self.nodeSet[i]-self.nodeSet[j])
#         minIndex = np.argmin(distance)
#         jVal = int(minIndex%self.nodeNum)
#         tabuList = [jVal]
#         currRow = jVal
#         count = 0
#         while count < self.nodeNum:
#             minIndex = np.argsort(distance[currRow,:])
#             for i in minIndex:
#                 if i not in tabuList:
#                     tabuList.append(i)
#                     currRow = j
#                     break
#             count += 1
#         self.nodeSet = tabuList

#     def createCircularLinklist(self)->np.array:
#         ringtopology = []
#         for i in range(self.nodeNum):
#             if i == 0:
#                 obj = CircularLinklist(self.nodeNum-1,i,i+1)
#             elif i+1 == self.nodeNum:
#                 obj = CircularLinklist(i-1,i,0)
#             else:
#                 obj = CircularLinklist(i-1,i,i+1)
#             ringtopology.append(obj)
#         self.ring = np.array(ringtopology)
    
    