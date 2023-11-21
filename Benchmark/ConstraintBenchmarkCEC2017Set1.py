from Benchmark.Prototype import FunctionOptimization
import numpy as np
import math
'''
Created on Nov 20, 2023

@author: patip
'''



class C01(FunctionOptimization):
    # def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=100, lowerBound:np.double=-100)->None:
    #     FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound)
    
    def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=100, lowerBound:np.double=-100, filePath="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound, filePath=filePath,functionNumber="1")
        
    def fitnessValue(self, individual:np.array)->np.double:
        z = self.shiftVal(individual)
        fitnessValue = 0
        for i in range(len(individual)):
            valSq = 0
            for j in range(i):
                valSq += z[j]
            fitnessValue += math.pow(valSq, 2)
        
    def gConstraint1(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        gVal = 0
        for i in range(self.dimensionSize):
            gVal+= (math.pow(z[i], 2)-5000*math.cos(0.1*math.pi*z[i])-4000)
        return gVal
    
    def volidateConstraint(self, individual)->np.double:
        gVol = 0
        hVol = 0
        gVol += max(0,self.gConstraint1(individual))
        return gVol+hVol
    
    def eveluate(self, individual:np.array)->(np.double, np.double):
        return (self.fitnessValue(individual),self.volidateConstraint(individual))
    
    
class C02(FunctionOptimization):
    
    def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=100, lowerBound:np.double=-100, filePath="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound, functionNumber="2", filePath=filePath)
    
    def fitnessValue(self, individual:np.array)->np.double:
        z = self.shiftVal(individual)
        fitnessValue = 0
        for i in range(len(individual)):
            valSq = 0
            for j in range(i):
                valSq += z[j]
            fitnessValue += math.pow(valSq, 2)
    
    def gConstraint1(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        y = self.rotateValue(z)
        gVal = 0
        for i in range(self.dimensionSize):
            gVal+= (math.pow(y[i], 2)-5000*math.cos(0.1*math.pi*y[i])-4000)
        return gVal
    
    def volidateConstraint(self, individual)->np.double:
        gVol = 0
        hVol = 0
        gVol += max(0,self.gConstraint1(individual))
        return gVol+hVol
    
    def eveluate(self, individual:np.array)->(np.double, np.double):
        return (self.fitnessValue(individual),self.volidateConstraint(individual))
    
    
class C03(FunctionOptimization):
    def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=100, lowerBound:np.double=-100, filePath="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound, functionNumber="3", filePath=filePath)
        
    def fitnessValue(self, individual:np.array)->np.double:
        z = self.shiftVal(individual)
        fitnessValue = 0
        for i in range(len(individual)):
            valSq = 0
            for j in range(i):
                valSq += z[j]
            fitnessValue += math.pow(valSq, 2)
            
    
    def gConstraint1(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        gVal = 0
        for i in range(self.dimensionSize):
            gVal+= (math.pow(z[i], 2)-5000*math.cos(0.1*math.pi*z[i])-4000)
        return gVal
    
    def hConstraint1(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize):
            hVal += z[i]*math.sin(0.1*math.pi*z[i])
        return -1*hVal
    
    
    def volidateConstraint(self, individual)->np.double:
        gVol = 0
        hVol = 0
        gVol += max(0,self.gConstraint1(individual))
        hVol += max(0,abs(self.hConstraint1(individual))-self.epsVal)
        return gVol+hVol
    
    
    
    def eveluate(self, individual:np.array)->(np.double, np.double):
        return (self.fitnessValue(individual),self.volidateConstraint(individual))
    
    
class C04(FunctionOptimization):
    
    def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=10, lowerBound:np.double=-10, filePath="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound, functionNumber="4", filePath=filePath)
        
        
    def fitnessValue(self, individual:np.array)->np.double:
        z  = self.shiftVal(individual)
        fitnessValue = 0
        for i in range(self.dimensionSize):
            fitnessValue += (math.pow(z[i], 2)-10*math.cos(2*math.pi*z[i])+10)
        return fitnessValue
    
    def gConstraint1(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        gVal = 0
        for i in range(self.dimensionSize):
            gVal += z[i]*math.sin(2*z[i])
        return -1*gVal
    
    def gConstraint2(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        gVal = 0
        for i in range(self.dimensionSize):
            gVal += z[i]*math.sin(z[i])
        return gVal
    
    def volidateConstraint(self, individual)->np.double:
        gVol = 0
        hVol = 0
        gVol += max(0,self.gConstraint1(individual))
        gVol += max(0,self.gConstraint2(individual))

        return gVol+hVol
    
    def eveluate(self, individual:np.array)->(np.double, np.double):
        return (self.fitnessValue(individual),self.volidateConstraint(individual))
    
class C05(FunctionOptimization):
    def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=10, lowerBound:np.double=-10, filePath="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound, functionNumber="5", filePath=filePath)
        
    def fitnessValue(self, individual:np.array)->np.double:
        z = self.shiftVal(individual)
        fitnessValue = 0
        for i in range(self.dimensionSize-1):
            fitnessValue += (100*math.pow(math.pow(z[i], 2)-z[i+1], 2)+math.pow(z[i]-1, 2))
        return fitnessValue
    
    
    def rotateValue(self, shiftValue:np.array, rotateNumber:str ="1")->np.array:
        rotateName = "M"+rotateNumber+"_"+str(self.functionNumber)+"_D"+str(self.dimensionSize)+".txt"
        rotateData = np.load(self.filePath+"/"+rotateName)
        return np.matmul(rotateData,shiftValue)
    
    
    def gConstraint1(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        y = self.rotateValue(z, "1")
        gVal = 0
        for i in range(self.dimensionSize):
            gVal += (math.pow(y[i], 2)-50*math.cos(2*math.pi*y[i])-40)
        return gVal
        
    def gConstraint2(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        w = self.rotateValue(z, "1")
        gVal = 0
        for i in range(self.dimensionSize):
            gVal += (math.pow(w[i], 2)-50*math.cos(2*math.pi*w[i])-40)
        return gVal
        
        
    def volidateConstraint(self, individual:np.array)->np.double:
        gVol = 0
        hVol = 0
        gVol += max(0,self.gConstraint1(individual))
        gVol += max(0,self.gConstraint2(individual))
        return gVol+hVol
    
    
    def eveluate(self, individual:np.array)->(np.double, np.double):
        return (self.fitnessValue(individual),self.volidateConstraint(individual))
    
    
class C06(FunctionOptimization):
    def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=20, lowerBound:np.double=-20, filePath="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound, functionNumber="6", filePath=filePath)
        
    def fitnessValue(self, individual:np.array)->np.double:
        z = self.shiftVal(individual)
        fitnessValue = 0
        for i in range(self.dimensionSize):
            fitnessValue += ((z[i]-10*math.cos(2*math.pi*z[i])+10))
        return fitnessValue
    
    def hConstraint1(self,individual:np.array)->np.double:
        z  = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize):
            hVal += z[i]*math.sin(z[i])
        return -1*hVal
    
    
    def hConstraint2(self,individual:np.array)->np.double:
        z  = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize):
            hVal += z[i]*math.sin(z[i])
        return hVal
    
    def hConstraint3(self,individual:np.array)->np.double:
        z  = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize):
            hVal += z[i]*math.cos(z[i])
        return -1*hVal
    
    def hConstraint4(self,individual:np.array)->np.double:
        z  = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize):
            hVal += z[i]*math.cos(math.pi*z[i])
        return hVal
    
    def hConstraint5(self,individual:np.array)->np.double:
        z  = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize):
            hVal += z[i]*math.sin(2*math.sqrt(abs(z[i])))
        return hVal
    
    def hConstraint6(self,individual:np.array)->np.double:
        z  = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize):
            hVal += z[i]*math.sin(2*math.sqrt(abs(z[i])))
        return -1*hVal
    
    def volidateConstraint(self, individual:np.array)->np.double:
        gVol =0
        hVol = 0
        
        hVol += max(0,abs(self.hConstraint1(individual))-self.epsVal)
        hVol += max(0,abs(self.hConstraint2(individual))-self.epsVal)
        hVol += max(0,abs(self.hConstraint3(individual))-self.epsVal)
        hVol += max(0,abs(self.hConstraint4(individual))-self.epsVal)
        hVol += max(0,abs(self.hConstraint5(individual))-self.epsVal)
        hVol += max(0,abs(self.hConstraint6(individual))-self.epsVal)

        return gVol+hVol
    
    def eveluate(self, individual:np.array)->(np.double, np.double):
        return (self.fitnessValue(individual),self.volidateConstraint(individual))
    
    
    
class C07(FunctionOptimization):
    
    def __init__(self, populationSize:int=100, dimensionSize:int=30, upperBound:np.double=50, lowerBound:np.double=-50, filePath="C:/Users/patip/OneDrive/Documents/eclipseworkspace/constraintOpt/inputdata")->None:
        FunctionOptimization.__init__(self, populationSize=populationSize, dimensionSize=dimensionSize, upperBound=upperBound, lowerBound=lowerBound, functionNumber="7", filePath=filePath)
        
        
    def fitnessValue(self, individual:np.array)->np.double:
        z = self.shiftVal(individual)
        fitnessValue = 0
        for i in range(self.dimensionSize):
            fitnessValue += (z[i]*math.sin(z[i]))
        return fitnessValue
    
    def hConstraint1(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize):
            hVal += (z[i]-100*math.cos(0.5*z[i])+100)
        return hVal
    
    def hConstraint2(self,individual:np.array)->np.double:
        z = self.shiftVal(individual)
        hVal = 0
        for i in range(self.dimensionSize):
            hVal += (z[i]-100*math.cos(0.5*z[i])+100)
        return -1*hVal
    
    
    def volidateConstraint(self, individual:np.array)->np.double:
        gVol = 0
        hVol = 0
        
        hVol += max(0,abs(self.hConstraint1(individual))-self.epsVal)
        hVol += max(0,abs(self.hConstraint2(individual))-self.epsVal)
        
        return gVol+hVol
    
    def eveluate(self, individual:np.array)->(np.double, np.double):
        return (self.fitnessValue(individual),self.volidateConstraint(individual))
    
    

    
    
        