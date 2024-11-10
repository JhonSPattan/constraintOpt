import numpy as np
import math
class FunctionOptimization:
    upperbound = 100
    lowerbound = -100
    populationSize = 100
    dimension = 30
    def __init__(self,populationSize:int=100,dimension:int=30)->None:
        self.populationSize = populationSize
        self.dimension = dimension
    
    def generate(self)->np.array:
        return np.random.uniform(self.lowerbound,self.upperbound,size=(self.populationSize,self.dimension))
    
    def eveluate(self,individual:np.array)->np.double:
        return np.sum(individual)
    
    def checking(self,individual:np.array)->np.array:
        for i in range(len(individual)):
            if individual[i] > self.upperbound:
                individual[i] = max(self.lowerbound,2*self.upperbound-individual[i])
            elif individual[i] < self.lowerbound:
                individual[i] = min(self.upperbound,2*self.lowerbound-individual[i])
        return individual
    

    def setDimension(self,dimension)->None:
        self.dimension = dimension
        
    def setPopulationSize(self,populationSize)->None:
        self.populationSize = populationSize
    
    def functionSummary(self,individual:np.array)->None:
        count = 1
        print("=========================Answer Function===========================")
        for i in individual:
            print("X: ",count," = ",i)
            count += 1
        print("Answer is: ",self.eveluate(individual))
        print("===================================================================")

    
    def getUpperbound(self)->np.array:
        return np.ones(self.dimension)*self.upperbound
    
    
    def getLowerbound(self)->np.array:
        return np.ones(self.dimension)*self.lowerbound
    
    # for constaint optimization
    def alphaFunction(self,fitnessValue:float=0,fitnessValueTransform:float=0,res:float=0,omega:float=0)->np.double:
        if fitnessValue > omega and res < abs(fitnessValueTransform)/3:
            return (abs(fitnessValueTransform)*((6*math.sqrt(3)-2)/(6*math.sqrt(3)))-res)/(abs(fitnessValueTransform)-res)
        elif fitnessValue > omega and  res >= (abs(fitnessValueTransform)/3) and res <= abs(fitnessValueTransform):
            return 1-(1/(2*math.sqrt(abs(fitnessValueTransform)/res)))
        elif fitnessValue > omega and res > fitnessValue:
            return 0.5*math.sqrt(abs(fitnessValueTransform)/res)
        else:
            return 0
        
    def penaltyFunction(self,fitnessValue:float,fitnessValueTransform:float,res:float,omega:float,alpha:float)->np.double:
        if fitnessValue > omega or res > 0:
            return alpha*abs(fitnessValueTransform)+(1-alpha)*res
        else:
            return fitnessValueTransform
        
    def residualFunction(self)->np.double:
        return 0.0
    
    def getOptimal(self)->np.double:
        return 0.0
    
    def summary(self,population:np.array)->None:
        for i in range(len(population)):
            print("X",(i+1),population[i])
        print("With value => ",self.eveluate(population))

