import numpy as np
import math
'''
Created on Nov 19, 2023

@author: patip
'''

class FunctionOptimization:
    upperBound = 100
    lowerBound = -100
    populationSize = 100
    dimensionSize = 30
    filePath = ""
    functionNumber = ""
    epsVal = 1e-4
    
    def __init__(self,populationSize:int=100,dimensionSize:int=30,upperBound:np.double=100,lowerBound:np.double=-100,functionNumber:str = "1",filePath ="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        self.populationSize = populationSize
        self.dimensionSize = dimensionSize
        self.filePath = filePath
        self.functionNumber = functionNumber
        
    def generate(self)->np.array:
        return  np.random.uniform(self.lowerBound,self.upperBound,size=(self.populationSize,self.dimensionSize))

    
    def shiftVal(self,individual:np.array)->np.array:
        shiftName = "shift_data_"+str(self.functionNumber)+".txt"
        shiftData = np.loadtxt(self.filePath+"/"+shiftName)
        if self.dimensionSize == 100:
            return individual-shiftData
        return individual-shiftData[0:self.dimensionSize]
    
    def rotateValue(self,shiftValue:np.array)->np.array:
        rotateName = "M_"+str(self.functionNumber)+"_D"+str(self.dimensionSize)+".txt"
        rotateData = np.loadtxt(self.filePath+"/"+rotateName)
        return np.matmul(rotateData,shiftValue)
    
    def eveluate(self,individual:np.array)->(np.double,np.double):
        return 0
    
    
    def fitnessValue(self,individual:np.array)->np.double:
        return 0
    
    def volidateConstraint(self,individual)->np.double:
        return 0
    