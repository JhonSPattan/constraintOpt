import numpy as np
import pandas as pd
import os
from matplotlib import pyplot


# for Ubuntu Server 
# path_result = "/myweb/www/pythonrunnew/Unconstraintoptimization/result/"
# path_individual = "/myweb/www/pythonrunnew/Unconstraintoptimization/individual/"
# path_plot = "/myweb/www/pythonrunnew/Unconstraintoptimization/plot/"
# path_populationanalysis = "/myweb/www/pythonrunnew/Unconstraintoptimization/populationAnalysis/"



# for work station PC
#path_result = "/home/patipan/Documents/unconstraintoptimization/result/"
#path_individual = "/home/patipan/Documents/unconstraintoptimization/individual/"
#path_plot = "/home/patipan/Documents/unconstraintoptimization/plot/"
#path_populationanalysis = "/home/patipan/Documents/unconstraintoptimization/populationAnalysis/"


# for local pc
path_result = "/home/patipan/Documents/ConstraintOptimization/result/"
path_individual = "/home/patipan/Documents/ConstraintOptimization/individual/"
path_plot = "/home/patipan/Documents/ConstraintOptimization/plot/"
path_populationanalysis = "/home/patipan/Documents/ConstraintOptimization/populationAnalysis/"



class PopulationAnalysis:
    def __init__(self,functionname:str,algorithmname:str,diversityList:np.array,successRateList:np.array,fitdiversityList:np.array
                 ,problemtype:str="Small",functiontype:str="Unimodal",replace:int=30):    
        self.functionname = functionname
        self.algorithmname = algorithmname
        self.problemtype = problemtype
        self.functiontype = functiontype
        self.diversityList = diversityList
        self.successRateList = successRateList
        self.fitdiversityList = fitdiversityList
        self.replace = replace
        # self.round = round
        
    
    def averageValue(self,dataValue:np.array)->np.array:
        averageData = []
        replace = len(dataValue)
        for i in range(len(dataValue[0])):
            averageValue = 0
            for j in range(len(dataValue)):
                averageValue += dataValue[j][i]
            averageData.append(averageValue/replace)
        return np.array(averageData)
    
    def fileWriteFitness(self):
        fitnessRate = {'fitnessdiversityrate':self.averageValue(self.fitdiversityList)}
        plotSuccess = pd.DataFrame(fitnessRate)
        path_file = path_populationanalysis+self.problemtype+"/"+self.functiontype+"/"+self.functionname+"_"+self.algorithmname+"_fitdiversity.csv"
        plotSuccess.to_csv(path_file,index=False)

                
    def fileWriteSuccess(self):
        successRate = {'successrate':self.averageValue(self.successRateList)}
        plotSuccess = pd.DataFrame(successRate)
        path_file = path_populationanalysis+self.problemtype+"/"+self.functiontype+"/"+self.functionname+"_"+self.algorithmname+"_success.csv"
        plotSuccess.to_csv(path_file,index=False)
        
        
    def fileWriteDiversity(self):
        diversityRate = {'diversityrate':self.averageValue(self.diversityList)}
        plotdiversity = pd.DataFrame(diversityRate)
        path_file = path_populationanalysis+self.problemtype+"/"+self.functiontype+"/"+self.functionname+"_"+self.algorithmname+"_diversity.csv"
        plotdiversity.to_csv(path_file,index=False)
        
        
    






class FileAnalysis:
    def __init__(self,functionname:str,algorithmname:str,data:pd.DataFrame,individual:pd.DataFrame,
                 plotValue:np.array=None,plotVolidate:np.array=None,problemtype:str="Small",functiontype:str="Unimodal")->None:
        self.functionname = functionname
        self.algorithmname = algorithmname
        self.data = data
        self.individual = individual
        self.problemtype = problemtype
        self.functiontype = functiontype
        self.plotValue = plotValue
        self.plotVolidate = plotVolidate
    
    
    def plotAnalysis(self)->None:
        plotAverage = []
        replace = len(self.plotValue)
        for i in range(len(self.plotValue[0])):
            averageValue = 0
            for j in range(len(self.plotValue)):
                averageValue += self.plotValue[j][i]
            plotAverage.append(averageValue/replace)
            
        plotAverage = np.array(plotAverage)
        plotDf = pd.DataFrame({'solutionround':plotAverage})
        path_file = path_plot+self.problemtype+"/"+self.functiontype+"/"+self.functionname+"_"+self.algorithmname+"_plot.csv"
        plotDf.to_csv(path_file,index=False)

    def plotAnalysis2(self)->None:
        plotAverage = []
        plotVoliAverage = []

        replace = len(self.plotValue)
        for i in range(len(self.plotValue[0])):
            averageValue = 0
            for j in range(len(self.plotValue)):
                averageValue += self.plotValue[j][i]
            plotAverage.append(averageValue/replace)

        replace = len(self.plotVolidate)
        for i in range(len(self.plotVolidate[0])):
            averageValue = 0
            for j in range(len(self.plotVolidate)):
                averageValue += self.plotVolidate[j][i]
            plotVoliAverage.append(averageValue/replace)

        plotAverage = np.array(plotAverage)
        plotVoliAverage = np.array(plotVoliAverage)

        plotDf = pd.DataFrame({'solutionround':plotAverage,'volidateround':plotVoliAverage})
        path_file = path_plot+self.problemtype+"/"+self.functiontype+"/"+self.functionname+"_"+self.algorithmname+"_plot.csv"
        plotDf.to_csv(path_file,index=False)
        
            
    def fileWriteSolution(self)->None:
        path_file = path_result+self.problemtype+"/"+self.functiontype+"/"+self.functionname+"_"+self.algorithmname+"_solution.csv"
        self.data.to_csv(path_file,index=False)

    def fileWriteIndividual(self)->None:
        path_file = path_individual+self.functionname+"_"+self.algorithmname+"_individual.csv"
        self.individual.to_csv(path_file,index=False)
        

    def analysis(self)->None:
        solution = self.data['solution']
        volidate = self.data['volidate']

        minIndex = np.where(solution == min(solution))[0][0]
        maxIndex = np.where(solution == max(solution))[0][0]

        volidatemin = volidate[minIndex]
        volidatemax = volidate[maxIndex]

        print("From function "+self.functionname+" with algorithmname "+self.algorithmname)
        print("Worst solution ",(max(solution))," with volidate ",volidatemax,flush=True)
        print("Best solution ",(min(solution))," with volidate ",volidatemin,flush=True)
        print("Mean solution ",(np.average(solution))," with volidate ",(np.average(volidate)),flush=True)
        print("Standart diviation ",np.std(solution),flush=True)
        
        
class FileAnalysis2(FileAnalysis):
    def __init__(self,functionname:str,algorithmname:str,data:pd.DataFrame,individual:pd.DataFrame,
                 plotValue:np.array=None,plotValuemin:np.array=None,plotValuemax:np.array=None
                 ,plotValuemean:np.array=None,plotValuestd:np.array=None,
                 problemtype:str="Small",functiontype:str="Unimodal")->None:
        self.functionname = functionname
        self.algorithmname = algorithmname
        self.data = data
        self.individual = individual
        self.problemtype = problemtype
        self.functiontype = functiontype
        self.plotValue = plotValue
        
        self.plotValuemin = plotValuemin
        self.plotValuemax = plotValuemax
        self.plotValuemean = plotValuemean
        self.plotValuestd = plotValuestd
        
    def plotAnalysis(self)->None:
        plotAverage = []
        plotAverageMin = []
        plotAverageMax = []
        plotAverageMean = []
        plotAverageStd = []
        
        replace = len(self.plotValue)
        for i in range(len(self.plotValue[0])):
            averageValue = 0
            for j in range(len(self.plotValue)):
                averageValue += self.plotValue[j][i]
            plotAverage.append(averageValue/replace)
            
            
        for i in range(len(self.plotValuemin[0])):
            averageValue = 0
            for j in range(len(self.plotValuemin)):
                averageValue += self.plotValuemin[j][i]
            plotAverageMin.append(averageValue/replace)
            
        for i in range(len(self.plotValuemax[0])):
            averageValue = 0
            for j in range(len(self.plotValuemax)):
                averageValue += self.plotValuemax[j][i]
            plotAverageMax.append(averageValue/replace)
            
        for i in range(len(self.plotValuemean[0])):
            averageValue = 0
            for j in range(len(self.plotValuemean)):
                averageValue += self.plotValuemean[j][i]
            plotAverageMean.append(averageValue/replace)
            
            
        for i in range(len(self.plotValuestd[0])):
            averageValue = 0
            for j in range(len(self.plotValuestd)):
                averageValue += self.plotValuestd[j][i]
            plotAverageStd.append(averageValue/replace)
            
        
            
        
        plotAverage = np.array(plotAverage)
        plotAverageMin = np.array(plotAverageMin)
        plotAverageMax = np.array(plotAverageMax)
        plotAverageMean = np.array(plotAverageMean)
        plotAverageStd = np.array(plotAverageStd)
        plotDf = pd.DataFrame({
            'solutionround':plotAverage,
            'solutionminround':plotAverageMin,
            'solutionmaxround':plotAverageMax,
            'solutionmeanround':plotAverageMean,
            'solutionstdround':plotAverageStd,
        })
        path_file = path_plot+self.problemtype+"/"+self.functionname+"_"+self.algorithmname+"_plot.csv"
        plotDf.to_csv(path_file,index=False)


