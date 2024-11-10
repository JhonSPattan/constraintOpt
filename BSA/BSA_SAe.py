from numpy.core.multiarray import array as array
from Benchmark.ProtoConstraintOptimization import ProtoConstraintOptimization
from Util.Analysis import FileAnalysis, PopulationAnalysis
from BSA.BSA import BSA
import pandas as pd
import numpy as np
import math

class BSA_SAe(BSA):
    def __init__(self, constraintClass: ProtoConstraintOptimization, populationSize: int = 50, dimensionSize: int = 30, sf: float = 3, replace: int = 25, problemtype: str = "Small", algorithmname: str = "BSA_SAe", functionname: str = "None", functiontype: str = "Constraint") -> None:
        super().__init__(constraintClass, populationSize, dimensionSize, sf, replace, problemtype, algorithmname, functionname, functiontype)
        self.Tc = int(0.2*(self.maxfes/self.populationSize))
        self.seta = 0.2*self.populationSize
        self.Th1 = 100
        self.Th2 = 2
        self.e1 = 0
        self.e2 = 0
        self.e1h = 0


    

    def _caletVal(self,t:int)->None:
        if t in range(0,self.Tc):
            self.et = self.e1*math.pow(1-(t/self.Tc),self.cp)
        else:
            self.et = 0

    def optimized(self) -> np.array:
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
            self.e1 = 0
            self.e2
            t = 0
            while count < self.maxfes:
                for i in range(self.populationSize):
                    fitnessValue[i],volidateValue[i] = self._eveluate(population[i])

                oldpopulation = self._selectionI(oldpopulation=oldpopulation, population=population)

                if (count == 0):
                    self.e0 = max(volidateValue)
                    self.e1 = self.e0
                    self.e1h = self.e0
                else:
                    if (self.e0 > self.Th1):
                        self.e2 = max(np.flip(np.sort(volidateValue))[0:int(self.seta)])
                    else:
                        self.e2 = self.e0

                    if (self.e2 > self.Th2 and self.e2 < self.e1h):
                        self.e1 = self.e2
                        self.e1h = self.e1
                    else:
                        self.e1 = self.e1h

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

