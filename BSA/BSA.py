from Benchmark.ProtoConstraintOptimization import ProtoConstraintOptimization
from Util.Analysis import FileAnalysis, PopulationAnalysis
from scipy.stats import truncnorm
import pandas as pd
import numpy as np
import random
import math


# this BSA original is use as BSA-FCe


class BSA():
    def __init__(self,constraintClass:ProtoConstraintOptimization, populationSize:int=50, dimensionSize:int=30, sf:float=3, replace:int=25, problemtype:str="Small", algorithmname:str="BSA",functionname:str="None",functiontype:str="Constraint") -> None:
        self.constraintClassObj = constraintClass(populationSize,dimensionSize)
        self.populationSize = populationSize
        self.dimensionSize = dimensionSize
        self.sf = sf
        self.cp = 5.0
        self.e0 = 0
        self.et = 0
        self.mixrate = 1

        self.maxfes = 20000*self.dimensionSize
        self.nkeep = 100

        self.upperBound = self.constraintClassObj.getUpperbound()
        self.lowerBound = self.constraintClassObj.getLowerbound()

        self.replace = replace
        self.problemtype = problemtype
        self.algorithmname = algorithmname
        self.functionname = functionname
        self.functiontype = functiontype
        self.successRateValue = 0
        self.Tc = int(0.5*(self.maxfes/self.populationSize))


    def setFesMax(self,maxfes:int)->None:
        self.maxfes = maxfes

    def setNkeep(self,nkeep:int)->None:
        self.nkeep = nkeep

    def printInfo(self):
        print(self.algorithmname," with function: ",self.functionname," in ",self.dimensionSize,flush=True)

    
    def _checkingBound(self,x:np.array)->np.array:
        for j in range(self.dimensionSize):
            if x[j] > self.upperBound[j] or x[j] < self.lowerBound[j]:
                x[j] = random.uniform(0,1)*(self.upperBound[j]-self.lowerBound[j])+self.lowerBound[j]
        return x
        
        
    def _eveluate(self, x:np.array)->(np.double, np.double): # type: ignore
        return self.constraintClassObj.eveluate(x)


    def _generate(self)->np.array:
        return self.constraintClassObj.generate()



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


    def _selectionII(self, trialVec:np.array, targetVec:np.array)->np.array:
        trialFit, trialVol = self._eveluate(x=trialVec)
        targetFit, targetVol = self._eveluate(x=targetVec)

        if (trialVol <= self.et and targetVol <= self.et) or (trialVol == targetVol):
            if trialFit < targetFit:
                self.successRateValue += 1
                return trialVec
        elif trialVol < targetVol:
            self.successRateValue += 1
            return trialVec

        return targetVec

    def _selectionbest(self, trialVec:np.array, targetVec:np.array)->np.array:
        trialFit, trialVol = self._eveluate(x=trialVec)
        targetFit, targetVol = self._eveluate(x=targetVec)

        if (trialVol <= self.et and targetVol <= self.et) or (trialVol == targetVol):
            if trialFit < targetFit:
                
                return trialVec
        elif trialVol < targetVol:
            
            return trialVec

        return targetVec


    def _mutation(self,oldp:np.array,x:np.array)->np.array:
        return x + self.sf*truncnorm.rvs(0,1)*(oldp-x)

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
        
        return self._checkingBound(x=trialVec)


    def _buildnextPopulation(self,oldp:np.array,x:np.array)->np.array:
        mutantVec = self._mutation(oldp, x)
        trialVec = self._crossover(mutantVec, x)
        return self._selectionII(trialVec, x)

    
    def _calculatePopDiversity(self,population:np.array)->np.double:
        meanVec = np.mean(population,axis=0)
        sum = 0
        for i in range(len(population)):
            sum += math.pow(np.linalg.norm(population[i]-meanVec),2)

        sum = math.sqrt(sum)/len(population)
        return sum
    
    def _calculationFitnessDiversity(self,fitnessValue:np.array)->np.double:
        meanFit = np.mean(fitnessValue)
        sum = 0
        for i in range(len(fitnessValue)):
            sum += math.pow(fitnessValue[i]-meanFit,2)

        sum = math.sqrt(sum)/len(fitnessValue)
        return sum

    def _caletVal(self,t:int)->None:
        if t in range(0,self.Tc):
            self.et = self.e0*math.pow(1-(t/self.Tc),self.cp)
        else:
            self.et = 0

    
    def _individualAvg(self,individualList:np.array)->np.array:
        averageIndividual = []
        for i in range(self.dimensionSize):
            diVal = 0
            for j in range(self.replace):
                diVal += individualList[j][i]
            diVal /= self.replace
            averageIndividual.append(diVal)
        return np.array(averageIndividual)


    def _summary(self,xVec:np.array)->None:
        print("=================================================Summary===============================================",flush=True)
        print("Object function of ",self.functionname," slove by ",self.algorithmname," optimizer value is: ",self.eveluate(xVec),flush=True)
        print("With population size = ",self.populationSize,"  and dimension size = ",self.dimensionSize," round ",self.round," independent run ",self.replace,flush=True)
        print("Value of variable as following: ",flush=True)
        for i in range(self.dimensionSize):
            print("X",(i+1),"=",xVec[i],flush=True)
        
        print("=================================================End===================================================",flush=True)

    def optimized(self)->np.array:
        self.printInfo()
        bestIndividualList = []
        bestFitness = []
        bestVolidate = []
        roundValueplot = []
        roundVolidateplot = []
        roundPopdiversity = []
        roundSuccessRate = []
        roundFitnessdiversity = []


        for k in range(self.replace):
            population = self._generate()
            oldpopulation = self._generate()
            self.successRateValue = 0
            minValue = 9e+9
            minVolidate = 9e+9
            minIndex = 0
            minRound = np.zeros(int(self.maxfes/self.nkeep))
            minVoli = np.zeros(int(self.maxfes/self.nkeep))
            popdiversity = np.ones(int(self.maxfes/self.nkeep))*-1
            fitdiversity = np.ones(int(self.maxfes/self.nkeep))*-1
            successrate  = np.ones(int(self.maxfes/self.nkeep))*-1

            fitnessValue = np.zeros(self.populationSize)
            volidateValue = np.zeros(self.populationSize)
            bestPopulation = np.zeros(self.dimensionSize)

            count = 0
            tick = 0
            self.e0 = 0
            self.et = 0
            t = 0
            while count < self.maxfes:
                for i in range(self.populationSize):
                    fitnessValue[i],volidateValue[i] = self._eveluate(population[i])

                oldpopulation = self._selectionI(oldpopulation=oldpopulation, population=population)

                if count == 0:
                    self.e0 = max(volidateValue)
                self._caletVal(t=t)

                lowvloi = min(volidateValue)
                minIndex = np.where(volidateValue == lowvloi)[0][0]
                if count == 0:
                    bestPopulation = population[minIndex]
                    minValue = fitnessValue[minIndex]
                    minVolidate = volidateValue[minIndex]
                
                else:
                    bestPopulation = self._selectionbest(trialVec=population[minIndex],targetVec=bestPopulation)
                    minValue,minVolidate = self._eveluate(bestPopulation)

                if count >= tick*self.nkeep or count == 0:
                    minRound[tick] = minValue
                    minVoli[tick] - minVolidate
                    successrate[tick] = (self.successRateValue/self.populationSize)
                    popdiversity[tick] = self._calculatePopDiversity(population=population)
                    fitdiversity[tick] = self._calculationFitnessDiversity(fitnessValue=fitnessValue)
                    tick += 1

                self.successRateValue = 0
                dummyPopulation = []
                for i in range(self.populationSize):
                    dummyPopulation.append(self._buildnextPopulation(oldp=oldpopulation[i],x=population[i]))
                    count += 1

                t += 1
                dummyPopulation = np.array(dummyPopulation)
                population = np.copy(dummyPopulation)

            bestIndividualList.append(bestPopulation)
            bestFitness.append(minValue)
            bestVolidate.append(minVolidate)
            roundValueplot.append(minRound)
            roundVolidateplot.append(minVoli)
            roundPopdiversity.append(popdiversity)
            roundFitnessdiversity.append(fitdiversity)
            roundSuccessRate.append(successrate)
        


        roundPopdiversity = np.array(roundPopdiversity)
        roundFitnessdiversity = np.array(roundFitnessdiversity)
        roundSuccessRate = np.array(roundSuccessRate)

        bestFitness = np.array(bestFitness)
        bestVolidate = np.array(bestVolidate)
        bestIndividualList = np.array(bestIndividualList)
        roundValueplot = np.array(roundValueplot)
        roundVolidateplot = np.array(roundVolidateplot)
        bestIndividualAverage = self._individualAvg(bestIndividualList)
        fitnessDf = {'solution':bestFitness,'volidate':bestVolidate}
        individualDf = {}
        for i in range(self.replace):
            key = "individual"+str(i+1)
            individualDf[key] = bestIndividualList[i,:]
        
        individualDf = pd.DataFrame(data=individualDf)
        
        fitnessDf = pd.DataFrame(data=fitnessDf)
        fa = FileAnalysis(functionname=self.functionname, algorithmname=self.algorithmname, data=fitnessDf, individual=individualDf, problemtype=self.problemtype, functiontype=self.functiontype,plotValue=roundValueplot,plotVolidate=roundVolidateplot)
        fa.fileWriteSolution()
        fa.plotAnalysis2()
        fa.fileWriteIndividual()
        fa.analysis()

        pa = PopulationAnalysis(functionname=self.functionname,algorithmname=self.algorithmname,diversityList=roundPopdiversity,successRateList=roundSuccessRate,
                                fitdiversityList=roundFitnessdiversity,problemtype=self.problemtype,functiontype=self.functiontype,replace=self.replace)
        
        pa.fileWriteDiversity()
        pa.fileWriteFitness()
        pa.fileWriteSuccess()

        # population = self.unconstraintObj.generate()
        # self._summary(individual=bestIndividualAverage)
        return bestIndividualAverage



    
            

                


                




