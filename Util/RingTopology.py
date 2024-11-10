from Util.CircularLinklist import CircularLinklist
import numpy as np

class RingTopology():
    def __init__(self,nodeSet:np.array) -> None:
        self.nodeSet = nodeSet
        self.nodeNum = len(nodeSet)
        self.ring = None
        self.createTopology()

    def createTopology(self) -> None:
        cirList = []
        for i in range(self.nodeNum):
            cir = CircularLinklist(self.nodeSet[i],i)
            cirList.append(cir)

        for i in range(self.nodeNum):
            if i == 0 or i+1 != self.nodeNum:
                cirList[i].setNeighborhood(cirList[i-1],cirList[i+1])
            else:
                cirList[i].setNeighborhood(cirList[i-1],cirList[0])

        self.ring = np.array(cirList)

    def getIndexNeighborhood(self,radius:int = 1, index:int = 0)->np.array:
        indexList = []
        i = 0
        nextNode = self.ring[index].getNext()
        prevNode = self.ring[index].getPrev()
        while i < radius:
            indexList.append(nextNode.getIndex())
            indexList.append(prevNode.getIndex())
            i += 1
            nextNode = nextNode.getNext()
            prevNode = prevNode.getPrev()
        return np.array(indexList)
    
    def getValueNeighborhood(self,radius:int = 1, index:int = 0)->np.array:
        indexList = []
        i = 0
        nextNode = self.ring[index].getNext()
        prevNode = self.ring[index].getPrev()
        while i < radius:
            indexList.append(nextNode.getValue())
            indexList.append(prevNode.getValue())
            i += 1
            nextNode = nextNode.getNext()
            prevNode = prevNode.getPrev()
        return np.array(indexList)

        
            

