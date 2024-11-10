from Benchmark.ProtoConstraintOptimization import ProtoConstraintOptimization
from Util.Analysis import FileAnalysis, PopulationAnalysis
import pandas as pd
import numpy as np
import math

class DE():
    def __init__(self,constraintClass:ProtoConstraintOptimization,populationSize:int=100,dimensionSize:int=30,cr:float=0.8,sf:float=0.2,replace:int=30,problemtype:str="Small", algorithmname:str="DE",functionname:str="None",functiontype:str="Constraint"):
        self.constraintClassObj = constraintClass(populationSize,dimensionSize)
        self.populationSize = populationSize
        self.dimensionSize = dimensionSize
        self.cr = cr
        self.sf = sf
        self.cp = 0.5
        self.e0 = 0
        self.et = 0
        


        self.maxfes = 20000*self.dimensionSize
        self.nkeep = 1000

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

    
    def _eveluate(self, x:np.array)->(np.double, np.double): # type: ignore
        return self.constraintClassObj.eveluate(x)


    def _generate(self)->np.array:
        return self.constraintClassObj.generate()

    def _selection(self, trialVec:np.array, targetVec:np.array)->np.array:
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


        
    def _mutation(self, xr1Vec:np.array, xr2Vec:np.array, xr3Vec:np.array) -> np.array:
        return xr1Vec+self.sf*(xr2Vec-xr3Vec)

    def _crossover(self, mutantVec:np.array, xVec:np.array) -> np.array:
        trialVec = mutantVec
        randCross = np.random.uniform(0,1,self.dimensionSize)
        for j in range(self.dimensionSize):
            if randCross[j] > self.cr:
                trialVec[j] = xVec[j]
        return self.constraintClassObj.checking(trialVec)


    def _buildNextPopulation(self,xVec:np.array, xr1Vec:np.array, xr2Vec:np.array, xr3Vec:np.array) -> np.array:
        mutantVec = self._mutation(xr1Vec=xr1Vec, xr2Vec=xr2Vec, xr3Vec=xr3Vec)
        trialVec = self._crossover(mutantVec=mutantVec, xVec=xVec)
        return self._selection(trialVec=trialVec,targetVec=xVec)


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
    
    def _summary(self,individual:np.array)->None:
        print("=================================================Summary===============================================",flush=True)
        print("Object function of ",self.functionname," slove by ",self.algorithmname," optimizer value is: ",self.eveluate(individual),flush=True)
        print("With population size = ",self.populationSize,"  and dimension size = ",self.dimensionSize," maxfes ",self.maxfes," independent run ",self.replace,flush=True)
        print("Value of variable as following: ",flush=True)
        for i in range(self.dimensionSize):
            print("X",(i+1),"=",individual[i],flush=True)
        
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
                    # print(population[i])
                    fitnessValue[i],volidateValue[i] = self._eveluate(population[i])

                if count == 0:
                    self.e0 = max(volidateValue)
                self._caletVal(t=t)

                
                
                
                # if minVolidate > min(volidateValue) or count == 0:
                #     minVolidate = min(volidateValue)
                #     minindex = np.where(volidateValue == minVolidate)[0][0]
                #     minValue = fitnessValue[minindex]
                #     bestPopulation = population[minindex]

                lowvloi = min(volidateValue)
                minIndex = np.where(volidateValue == lowvloi)[0][0]
                if count == 0:
                    bestPopulation = population[minIndex]
                    minValue = fitnessValue[minIndex]
                    minVolidate = volidateValue[minIndex]
                else:
                    bestPopulation = self._selectionbest(trialVec=population[minIndex],targetVec=bestPopulation)
                    minValue,minVolidate = self._eveluate(bestPopulation)

                
                
                # if minValue > min(fitnessValue) or count == 0:
                #     minValue = min(fitnessValue)
                #     minIndex = np.where(fitnessValue==minValue)[0]
                #     bestPopulation = population[minIndex][0]

                if count >= tick*self.nkeep or count == 0:
                    minRound[tick] = minValue
                    minVoli[tick] = minVolidate
                    successrate[tick] = (self.successRateValue/self.populationSize)
                    popdiversity[tick] = self._calculatePopDiversity(population=population)
                    fitdiversity[tick] = self._calculationFitnessDiversity(fitnessValue=fitnessValue)
                    tick += 1

                self.successRateValue = 0
                dummyPopulation = []
                for i in range(self.populationSize):
                    randVec = np.random.permutation(self.populationSize)
                    delIndex = np.where(randVec == i)[0][0]
                    randVec = np.delete(randVec,delIndex,0)
                    dummyPopulation.append(self._buildNextPopulation(xVec=population[i],xr1Vec=population[randVec[0]],xr2Vec=population[randVec[1]],xr3Vec=population[randVec[2]]))
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

                



                

            









