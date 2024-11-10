from numpy.core.multiarray import array as array
from Benchmark.ProtoConstraintOptimization import ProtoConstraintOptimization
from Utilpenalty.Analysis import FileAnalysis, PopulationAnalysis
from scipy.stats import cauchy, norm, truncnorm
from BSApenalty.HLBSA import HLBSA
import pandas as pd
import numpy as np
import random
import math


class AHLBSA(HLBSA):
    def __init__(self, constraintClass: ProtoConstraintOptimization, populationSize: int = 100, dimensionSize: int = 30, sf: float = 3, replace: int = 30, problemtype: str = "Small", algorithmname: str = "AHLBSA", functionname: str = "None", functiontype: str = "Constraint") -> None:
        super().__init__(constraintClass, populationSize, dimensionSize, sf, replace, problemtype, algorithmname, functionname, functiontype)
        self.scalingFactorMu = 0.6
        self.mixRateMu = 0.8
        self.lr = 0.9
        self.scalingFactorList = []
        self.mixRateList = []


    def _selectionII(self, trialVec: np.array, x: np.array) -> np.array:
        if self.eveluate(trialVec) < self.eveluate(x):
            self.successRateValue += 1
            self.scalingFactorList.append(self.sf)
            self.mixRateList.append(self.mixrate)
            return trialVec
        else:
            return x
        

    def _crossover(self,mutantVec:np.array,x:np.array)->np.array:
        trialVec = mutantVec
        map = np.ones(self.dimensionSize)
        a = random.uniform(0,1)
        b = random.uniform(0,1)
        
        # strategy I
        if a < b:
            nd = int(math.ceil(self.mixrate*self.dimensionSize))
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
    
    def _mutation2(self, oldp:np.array, p:np.array, x:np.array) -> np.array:
        return x + self.sf*(p-oldp)
    
    def _mutation(self, oldpm:np.array, oldpn:np.array, xbest:np.array, x:np.array)->np.array:
        return x+self.sf*(xbest-x)+self.sf*(oldpm-oldpn)


    def _calculationMuValue(self)->None:
        if self.scalingFactorList != [] and self.mixRateList != []:
            self.mixRateList = self.lr*self.mixRateList+(1-self.lr)*np.mean(np.array(self.mixRateList))
            fList = np.array(self.scalingFactorList)
            meanL = ((np.sum(np.power(fList,2))))/(np.sum(fList))
            self.scalingFactorMu = self.lr*self.scalingFactorMu+(1-self.lr)*meanL

        self.scalingFactorList = []
        self.mixRateList = []


    def optimized(self) -> np.array:
        self.printInfo()
        bestIndividualList = []
        bestFitness = []
        roundValueplot = []
        roundPopdiversity = []
        roundSuccessRate = []
        roundFitnessdiversity = []


        for k in range(self.replace):
            self.successRateValue = 0
            self.scalingFactorList = []
            self.mixRateList = []
            self.mixRateMu = 0.8
            self.scalingFactorMu = 0.5

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


            while(count < self.maxfes):
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
                        self.mixrate = min(abs(norm.rvs(loc=self.mixRateMu,scale=0.1,size=1)[0]),1)
                        self.sf = min(abs(cauchy.rvs(loc = self.scalingFactorMu,scale=0.1,size=1)[0]),1)
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

                self._calculationMuValue()
            
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
        # self.summary(xVec=bestIndividualAverage)
        return bestIndividualAverage


    