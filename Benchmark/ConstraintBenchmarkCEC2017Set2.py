from Benchmark.Prototype import FunctionOptimization
import numpy as np
import math
'''
Created on Nov 21, 2023

@author: patip
'''



class C08(FunctionOptimization):
    def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=100, lowerBound:np.double=-100, filePath="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound, functionNumber="8", filePath=filePath)
        
    def fitnessValue(self, individual:np.array)->np.double:
        z = self.shiftVal(individual)
        return max(z)
    
    def hConstraint1(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize/2):
            hValdump = 0
            for j in range(i):
                y = z[2*i]
                hValdump += y
            hVal += hValdump
        return hVal
    
    def hConstraint2(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize/2):
            hValdump = 0
            for j in range(i):
                y = z[2*i+1]
                hValdump += y
            hVal += hValdump
        return hVal
    
    def volidateConstraint(self, individual:np.array)->np.double:
        gVol = 0
        hVol = 0
        
        hVol += max(0,abs(self.hConstraint1(individual))-self.epsVal)
        hVol += max(0,abs(self.hConstraint2(individual))-self.epsVal)
        
        return gVol+hVol
    
    
    def eveluate(self, individual:np.array)->(np.double, np.double):
        return (self.fitnessValue(individual),self.volidateConstraint(individual))
    
    
class C09(FunctionOptimization):
    def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=10, lowerBound:np.double=-10, filePath="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound, functionNumber="9", filePath=filePath)
        
    def fitnessValue(self, individual:np.array)->np.double:
        z = self.shiftVal(individual)
        return max(z)
    
    def gConstraint1(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        gVal = 1
        for i in range(self.dimensionSize/2):
            gVal *= z[2*i+1]
            
          
        return gVal  
          
    def hConstraint1(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize/2-1):
            hVal += z[2*i]
        
        return hVal
            
    def volidateConstraint(self, individual)->np.double:
        gVol = 0
        hVol = 0
        
        gVol += max(0,self.gConstraint1(individual))
        hVol += max(0,abs(self.hConstraint1(individual))-self.epsVal)
        return gVol+hVol
    
    
    def eveluate(self, individual:np.array)->(np.double, np.double):
        return (self.fitnessValue(individual),self.volidateConstraint(individual))


class C10(FunctionOptimization):
    
    def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=100, lowerBound:np.double=-100, filePath="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound, functionNumber="10", filePath=filePath)
        
    def fitnessValue(self, individual:np.array)->np.double:
        z = self.shiftVal(individual)
        return max(z)
    
    def hConstraint1(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize):
            hdump = 0
            for j in range(i):
                hdump+= z[j]
            hVal += math.pow(hdump, 2)    
        return hVal
    
    def hConstraint2(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize-1):
            hVal += math.pow(z[i]-z[i+1], 2)
            
        return hVal
    
    def volidateConstraint(self, individual:np.array)->np.double:
        gVol = 0
        hVol = 0
        
        hVol += max(0,abs(self.hConstraint1(individual))-self.epsVal)
        hVol += max(0,abs(self.hConstraint2(individual))-self.epsVal)
        return gVol+hVol
    
    def eveluate(self, individual:np.array)->(np.double, np.double):
        return (self.fitnessValue(individual),self.volidateConstraint(individual))
        
class C11(FunctionOptimization):
    
    def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=100, lowerBound:np.double=-100, filePath="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound, functionNumber="11", filePath=filePath)
        
    def fitnessValue(self, individual:np.array)->np.double:
        z  = self.shiftVal(individual)
        fitnessValue = 0
        for i in range(self.dimensionSize):
            fitnessValue += z[i]
            
        return fitnessValue
    
    def gConstraint1(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        gVal = 1
        for i in range(self.dimensionSize):
            gVal *= z[i]
            
        return gVal
        
    def hConstraint1(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize-1):
            hVal += math.pow(z[i]-z[i+1], 2)
            
        return hVal
    
    def volidateConstraint(self, individual:np.array)->np.double:
        gVol = 0
        hVol = 0
                
        gVol += max(0,self.gConstraint1(individual))
        hVol += max(0,abs(self.hConstraint1(individual))-self.epsVal)
        
        return gVol+hVol
    
    def eveluate(self, individual:np.array)->(np.double, np.double):
        return (self.fitnessValue(individual),self.volidateConstraint(individual))
    
    
class C12(FunctionOptimization):
    
    def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=100, lowerBound:np.double=-100, filePath="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound, functionNumber="12", filePath=filePath)
        
    def fitnessValue(self, individual:np.array)->np.double:
        y = self.shiftVal(individual)
        fitnessValue = 0
        for i in range(self.dimensionSize):
            fitnessValue += math.pow(y[i], 2)-10*math.cos(2*math.pi*y[i])+10
        return fitnessValue 
    
    def gConstraint1(self,individual:np.array)->np.double:
        y = self.shiftVal(individual)
        gVal = 0
        for i in range(self.dimensionSize):
            gVal += abs(y[i])
        return 4-gVal
    
    def gConstraint2(self,indvidual:np.array)->np.double:
        y = self.shiftVal(indvidual)
        gVal = 0
        for i in range(self.dimensionSize):
            gVal += math.pow(y[i], 2)-4
        return gVal
    
    def volidateConstraint(self, individual:np.array)->np.double:
        gVol = 0
        hVol = 0
                
        gVol += max(0,self.gConstraint1(individual))
        gVol += max(0,self.gConstraint2(individual))
        
        return gVol+hVol
    
    def eveluate(self, individual:np.array)->(np.double, np.double):
        return (self.fitnessValue(individual),self.volidateConstraint(individual))
    
    
class C13(FunctionOptimization):
    def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=100, lowerBound:np.double=-100, filePath="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound, functionNumber="13", filePath=filePath)
        
    def fitnessValue(self, individual:np.array)->np.double:
        y = self.shiftVal(individual)
        fitnessValue = 0
        for i in range(self.dimensionSize-1):
            fitnessValue += 100*math.pow(math.pow(y[i],2)-y[i+1], 2)+math.pow(y[i]-1, 2)
        return fitnessValue
        
    def gConstraint1(self,individual:np.array)->np.double:
        y = self.shiftVal(individual)
        gVal = 0
        for i in range(self.dimensionSize):
            gVal += math.pow(y[i], 2)-10*math.cos(2*math.pi*y[i])+10
            
        return gVal - 100
    
    def gConstraint2(self,individual:np.array)->np.double:
        y = self.shiftVal(individual)
        gVal = 0
        for i in range(self.dimensionSize):
            gVal += y[i]-2*self.dimensionSize
        return  gVal
    
    def gConstraint3(self,individual:np.array)->np.double:
        y = self.shiftVal(individual)
        gVal = 0
        for i in range(self.dimensionSize):
            gVal += y[i]
        return 5-gVal
    
    def volidateConstraint(self, individual:np.array)->np.double:
        gVol = 0
        hVol = 0
                
        gVol += max(0,self.gConstraint1(individual))
        gVol += max(0,self.gConstraint2(individual))
        gVol += max(0,self.gConstraint3(individual))
        
        return gVol+hVol
    
    def eveluate(self, individual:np.array)->(np.double, np.double):
        return (self.fitnessValue(individual),self.volidateConstraint(individual))
    
class C14(FunctionOptimization):
    pass