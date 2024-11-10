# Hierarchical Learning Backtracking search algorithm
from Benchmark.ProtoConstraintOptimization import ProtoConstraintOptimization
from Utilpenalty.Analysis import FileAnalysis, PopulationAnalysis
from scipy.stats import truncnorm
from BSApenalty.BSA import BSA
import pandas as pd
import numpy as np
import math

'''
Created on Sep 6, 2024

Hello world

@author: patip
'''

class HLBSA(BSA):
    def __init__(self, constraintClass:ProtoConstraintOptimization, populationSize:int=100, dimensionSize:int=30, sf:float=3, replace:int=30, problemtype:str="Small", algorithmname:str="HLBSA", functionname:str="None", functiontype:str="Constraint")->None:
        BSA.__init__(self, constraintClass, populationSize=populationSize, dimensionSize=dimensionSize, sf=sf, replace=replace, problemtype=problemtype, algorithmname=algorithmname, functionname=functionname, functiontype=functiontype)
        
    
    def _dividingpopulation(self, population:np.array, fitnessValue:np.array):
        indexSort = np.argsort(fitnessValue)
        group = []
        start = 0
        finish = 0
        x = [0.15*self.populationSize, 0.15*self.populationSize, 0.70*self.populationSize]
        for i in range(len(x)):
            if i+1 != len(x):
                finish += int(x[i])
            else:
                finish += int(x[i])+1    # because we divide 3 group with population size = 50 or 100

            y = indexSort[start:finish]
            group.append(y)
            start = finish

        return group,population[indexSort]
    
    
    def _mutation2(self, oldp:np.array, p:np.array, x:np.array) -> np.array:
        return x + self.sf*truncnorm.rvs(0,1)*(p-oldp)
    
    def _mutation(self, oldpm:np.array, oldpn:np.array, xbest:np.array, x:np.array)->np.array:
        return x+self.sf*truncnorm.rvs(0,1)*(xbest-x)+self.sf*truncnorm.rvs(0,1)*(oldpm-oldpn)
    
    def _buildnextPopulation(self, oldpm:np.array, oldpn:np.array, xbest:np.array, x:np.array)->np.array:
        mutantVec = self._mutation(oldpm=oldpm, oldpn=oldpn, xbest=xbest, x=x)
        trialVec = self.unconstraintObj.checking(self._crossover(mutantVec, x))
        return self._selectionII(trialVec, x)
    
    
    def _buildnextPopulation2(self, oldp:np.array, p:np.array, x:np.array) -> np.array:
        mutantVec = self._mutation2(oldp=oldp, p=p, x=x)
        trialVec = self.unconstraintObj.checking(self._crossover(mutantVec, x))
        return self._selectionII(trialVec=trialVec, x=x)
    
    def _meanpopgroup(self,population:np.array)->np.array:
        return np.sum(population, axis = 0)/len(population)
    
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
            secondsBest = np.zeros(self.dimensionSize)
            self.pr = np.zeros(self.dimensionSize)
            count = 0
            tick = 0
            groupindex = None
            it = 0
            while count < self.maxfes:
                for i in range(self.populationSize):
                    fitnessValue[i] = self.eveluate(population[i])
                    
                oldpopulation = self._selectionI(oldpopulation, population)
                indexSort = np.argsort(fitnessValue)
                oldpopulation = oldpopulation[indexSort]
                
                groupindex,_ = self._dividingpopulation(population=population, fitnessValue=fitnessValue)
                
                
                if minValue > min(fitnessValue) or count == 0:
                    minValue = min(fitnessValue)
                    minIndex = np.where(fitnessValue==minValue)[0]
                    indexSort = np.argsort(fitnessValue)
                    secondsBest = population[indexSort[1]]
                    bestPopulation = population[minIndex][0]
                    
                if count >= tick*self.nkeep or count == 0:
                    minRound[tick] = minValue
                    successrate[tick] = (self.successRateValue/self.populationSize)
                    popdiversity[tick] = self.calculatePopDiversity(population=population)
                    fitdiversity[tick] = self.calculationFitnessDiversity(fitnessValue=fitnessValue)
                    tick += 1
                
                
                dummyPopulation = []
                pbest = None
                
                for g in range(len(groupindex)):
                    for i in range(len(groupindex[g])):
                        if g == 0:
                            pbest = self._meanpopgroup(population[groupindex[0]])
                            dummyPopulation.append(self._buildnextPopulation2(oldp=oldpopulation[groupindex[g][i]], p=pbest, x=population[groupindex[g][i]]))
                        elif g == 1:
                            pbest = secondsBest
                            randVec = np.random.permutation(len(groupindex[g]))
                            vm = groupindex[g][randVec[0]]
                            vn = groupindex[g][randVec[0]]
                            oldpm = population[vm]
                            oldpn = population[vn]
                            dummyPopulation.append(self._buildnextPopulation(oldpm=oldpm, oldpn=oldpn, xbest=pbest, x=population[groupindex[g][i]]))
                        else:
                            pbest = bestPopulation
                            randVec = np.random.permutation(len(groupindex[g]))
                            vm = groupindex[g][randVec[0]]
                            vn = groupindex[g][randVec[0]]
                            oldpm = population[vm]
                            oldpn = population[vn]
                            dummyPopulation.append(self._buildnextPopulation(oldpm=oldpm, oldpn=oldpn, xbest=pbest, x=population[groupindex[g][i]]))
                count += self.populationSize
                it += 1        
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
        fa.analysis()

        pa = PopulationAnalysis(functionname=self.functionname,algorithmname=self.algorithmname,diversityList=roundPopdiversity,successRateList=roundSuccessRate,
                                fitdiversityList=roundFitnessdiversity,problemtype=self.problemtype,functiontype=self.functiontype,replace=self.replace)
        
        pa.fileWriteDiversity()
        pa.fileWriteFitness()
        pa.fileWriteSuccess()

        # population = self.unconstraintObj.generate()
        self.summary(xVec=bestIndividualAverage)
        return bestIndividualAverage