import numpy as np

'''
Created on Apr 29, 2024

@author: patip
'''


class ClusterNode:
    def __init__(self,clusterCenter:np.array=None, index:int = -1)->None:
        self.clusterCenter = clusterCenter
        self.index = index
        self.memberCluster = []
        
    def addMember(self,member:np.array)->None:
        self.memberCluster.append(member)
        
        
    def getClusterCenter(self)->np.array:
        return self.clusterCenter
    
    def getClusterMember(self)->np.array:
        return np.array(self.memberCluster)
    
    
    def deleteCluster(self)->None:
        self.memberCluster = []
        
        
