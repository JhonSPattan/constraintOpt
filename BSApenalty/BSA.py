from Benchmark.ProtoConstraintOptimization import ProtoConstraintOptimization
from Utilpenalty.Analysis import FileAnalysis, PopulationAnalysis
from scipy.stats import truncnorm
import pandas as pd
import numpy as np

import random
import math

class BSA:
    def __init__(self,constraintClass:ProtoConstraintOptimization, populationSize:int=100, dimensionSize:int=30, sf:float=3, replace:int=30, problemtype:str="Small", algorithmname:str="BSA",functionname:str="None",functiontype:str="Constraint") -> None:
        self.unconstraintObj = constraintClass(populationSize,dimensionSize)
        self.populationSize = populationSize
        self.dimensionSize = dimensionSize
        self.sf = sf
        self.mixrate = 1
        
        self.upperBound = self.unconstraintObj.getUpperbound()
        self.lowerBound = self.unconstraintObj.getLowerbound()
        
        
        
        if dimensionSize == 10 and "CEC2022" in functionname:
            self.maxfes = 200000
            self.nkeep = 1000
        elif (dimensionSize == 20) and ("CEC2022" in functionname):
            self.maxfes = 1000000
            self.nkeep = 1000
        elif "CEC2015ExpensiveProblems" in functionname:
            self.maxfes = 2000*self.dimensionSize
            self.nkeep = 100
        elif "CEC2017" in functionname:
            self.maxfes = 10000*self.dimensionSize
            self.nkeep = 1000
        elif "ReusableInventoryModel" in functionname:
            self.maxfes = 1000*self.dimensionSize
            self.nkeep = 100

        elif "CEC2017Constraint" in functionname:
            self.maxfes = 20000*self.dimensionSize
            self.nkeep = 1000
            
        
        self.replace = replace
        self.problemtype = problemtype
        self.algorithmname = algorithmname
        self.functionname = functionname
        self.functiontype = functiontype
        self.successRateValue = 0
        
    
    def _checkingBound(self,x:np.array)->np.array:
        for j in range(self.dimensionSize):
            if x[j] > self.upperBound[j] or x[j] < self.lowerBound[j]:
                x[j] = random.uniform(0,1)*(self.upperBound[j]-self.lowerBound[j])+self.lowerBound[j]
        return x
    
    
    
    def _selectionI(self,oldpopulation:np.array,population:np.array)->np.array:
        oldpList = []
        for i in range(self.populationSize):
            b = random.uniform(0,1)
            a = random.uniform(0,1)
            if a < b:
                oldpList.append(np.random.permutation(population[i]))
                continue        
            oldpList.append(np.random.permutation(oldpopulation[i]))
        
        return np.array(oldpList)
    
    
    def _selectionII(self,trialVec:np.array,x:np.array)->np.array:
        if self.eveluate(trialVec) < self.eveluate(x):
            self.successRateValue += 1
            return trialVec
        else:
            return x
    
    
    def _mutation(self,oldp:np.array,x:np.array)->np.array:
        return x+self.sf*truncnorm.rvs(0,1)*(oldp-x)
    
    
    def _crossover(self,mutantVec:np.array,x:np.array)->np.array:
        trialVec = mutantVec
        map = np.ones(self.dimensionSize)
        a = random.uniform(0,1)
        b = random.uniform(0,1)
        
        # strategy I
        if a < b:
            nd = int(math.ceil(self.mixrate*random.uniform(0,1)*self.dimensionSize))
            u = np.random.permutation(self.dimensionSize)
            for i in range(self.dimensionSize):
                if i in u[0:nd]:
                    map[i] = 0
        
        # strategy II
        else:
            for i in range(self.dimensionSize):
                k = random.randint(0,self.dimensionSize-1)
                map[k] = 0
                
        for i in range(self.dimensionSize):
            if(map[i]):
                trialVec[i] = x[i]
        
        return trialVec
    
    
    def _buildnextPopulation(self,oldp:np.array,x:np.array)->np.array:
        mutantVec = self._mutation(oldp, x)
        trialVec = self._checkingBound(self._crossover(mutantVec, x))
        return self._selectionII(trialVec, x)
        

    def eveluate(self,population:np.array)->np.double:
        return self.unconstraintObj.eveluate(population)
    
    
    def generate(self)->np.array:
        return self.unconstraintObj.generate()
    
    def setFesMax(self,maxfes:int)->None:
        self.maxfes = maxfes

    def setNkeep(self,nkeep:int)->None:
        self.nkeep = nkeep
    
    
    def printInfo(self):
        print(self.algorithmname," with function: ",self.functionname," in ",self.dimensionSize," replace ",self.replace,flush=True)
    
    def individualAvg(self,individualList:np.array)->np.array:
        averageIndividual = []
        for i in range(self.dimensionSize):
            diVal = 0
            for j in range(self.replace):
                diVal += individualList[j][i]
            diVal /= self.replace
            averageIndividual.append(diVal)
        return np.array(averageIndividual)
    
    def summary(self,xVec:np.array)->None:
        print("=================================================Summary===============================================",flush=True)
        print("Object function of ",self.functionname," slove by ",self.algorithmname," optimizer value is: ",self.eveluate(xVec),flush=True)
        print("With population size = ",self.populationSize,"  and dimension size = ",self.dimensionSize," independent run ",self.replace,flush=True)
        print("Value of variable as following: ",flush=True)
        for i in range(self.dimensionSize):
            print("X",(i+1),"=",xVec[i],flush=True)
        
        print("=================================================End===================================================",flush=True)
    
    
    def calculatePopDiversity(self,population:np.array)->np.double:
        meanVec = np.mean(population,axis=0)
        sum = 0
        for i in range(len(population)):
            sum += math.pow(np.linalg.norm(population[i]-meanVec),2)
            
        
        return math.sqrt(sum)/len(population)
    
    def calculationFitnessDiversity(self,fitnessValue:np.array)->np.double:
        meanFit = np.mean(fitnessValue)
        sum = 0
        for i in range(len(fitnessValue)):
            sum += math.pow(fitnessValue[i]-meanFit,2)

        return math.sqrt(sum)/len(fitnessValue)
    
    
    
    def optimized(self)->np.array:
        self.printInfo()
        bestIndividualList = []
        bestFitness = []
        roundValueplot = []
        roundPopdiversity = []
        roundSuccessRate = []
        roundFitnessdiversity = []
        
        
        for k in range(self.replace):
            self.successRateValue = 0
            population = self.generate()
            oldpopulation = self.generate()
            minValue = 9e+9
            minIndex = 0
            minRound = np.zeros(int(self.maxfes/self.nkeep))
            popdiversity = np.ones(int(self.maxfes/self.nkeep))*-1
            fitdiversity = np.ones(int(self.maxfes/self.nkeep))*-1
            successrate  = np.ones(int(self.maxfes/self.nkeep))*-1
            fitnessValue = np.zeros(self.populationSize)
            bestPopulation = np.zeros(self.dimensionSize)
            count = 0
            tick = 0
            while count < self.maxfes:
                
                for i in range(self.populationSize):
                    fitnessValue[i] = self.eveluate(population[i])
                    
                oldpopulation = self._selectionI(oldpopulation, population)
                
                
                if minValue > min(fitnessValue) or count == 0:
                    minValue = min(fitnessValue)
                    minIndex = np.where(fitnessValue==minValue)[0]
                    bestPopulation = population[minIndex][0]
                    
                if count >= tick*self.nkeep or count == 0:
                    minRound[tick] = minValue
                    successrate[tick] = (self.successRateValue/self.populationSize)
                    popdiversity[tick] = self.calculatePopDiversity(population=population)
                    fitdiversity[tick] = self.calculationFitnessDiversity(fitnessValue=fitnessValue)
                    tick += 1
                
                
                
                
                self.successRateValue = 0
                dummyPopulation = []
                for i in range(self.populationSize):
                    dummyPopulation.append(self._buildnextPopulation(oldp=oldpopulation[i], x=population[i]))
                    count += 1
                population = np.copy(np.array(dummyPopulation))
                
            bestIndividualList.append(bestPopulation)
            bestFitness.append(minValue)
            roundValueplot.append(minRound)
            roundPopdiversity.append(popdiversity)
            roundFitnessdiversity.append(fitdiversity)
            roundSuccessRate.append(successrate)
        


        roundPopdiversity = np.array(roundPopdiversity)
        roundFitnessdiversity = np.array(roundFitnessdiversity)
        roundSuccessRate = np.array(roundSuccessRate)

        bestFitness = np.array(bestFitness)
        bestIndividualList = np.array(bestIndividualList)
        roundValueplot = np.array(roundValueplot)
        bestIndividualAverage = self.individualAvg(bestIndividualList)
        fitnessDf = {'solution':bestFitness}
        individualDf = {}
        for i in range(self.replace):
            key = "individual"+str(i+1)
            individualDf[key] = bestIndividualList[i]
        
        individualDf = pd.DataFrame(data=individualDf)
        fitnessDf = pd.DataFrame(data=fitnessDf)
        fa = FileAnalysis(functionname=self.functionname, algorithmname=self.algorithmname, data=fitnessDf, individual=individualDf, problemtype=self.problemtype, functiontype=self.functiontype,plotValue=roundValueplot)
        fa.fileWriteSolution()
        fa.plotAnalysis()
        fa.fileWriteIndividual()
        fa.analysis()

        pa = PopulationAnalysis(functionname=self.functionname,algorithmname=self.algorithmname,diversityList=roundPopdiversity,successRateList=roundSuccessRate,
                                fitdiversityList=roundFitnessdiversity,problemtype=self.problemtype,functiontype=self.functiontype,replace=self.replace)
        
        pa.fileWriteDiversity()
        pa.fileWriteFitness()
        pa.fileWriteSuccess()

        # population = self.unconstraintObj.generate()
        # self.summary(individual=bestIndividualAverage)
        return bestIndividualAverage    
            
            
            
        
    
    
    
        
        
    


    