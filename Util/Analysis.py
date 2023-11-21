import numpy as np
import pandas as pd
import os
from matplotlib import pyplot


# for Ubuntu Server 
# path_result = "/myweb/www/pythonrunnew/NewDE/unconstraintoptimization/result/"
# path_individual = "/myweb/www/pythonrunnew/NewDE/unconstraintoptimization/individual/"
# path_plot = "/myweb/www/pythonrunnew/NewDE/unconstraintoptimization/plot/"
# path_populationanalysis = "/myweb/www/pythonrunnew/NewDE/unconstraintoptimization/populationAnalysis/"


# for local PC
path_result = "C:/Users/patip/OneDrive/Documents/python/unconstraintoptimization/result/"
path_individual = "C:/Users/patip/OneDrive/Documents/python/unconstraintoptimization/individual/"
path_plot = "C:/Users/patip/OneDrive/Documents/python/unconstraintoptimization/plot/"
path_populationanalysis = "C:/Users/patip/OneDrive/Documents/python/unconstraintoptimization/populationAnalysis/"
class PopulationAnalysis:
    def __init__(self,functionname:str,algorithmname:str,diversityList:np.array,successRateList:np.array
                 ,problemtype:str="Small",functiontype:str="Unimodal",replace:int=30,round:int=1000):    
        self.functionname = functionname
        self.algorithmname = algorithmname
        self.problemtype = problemtype
        self.functiontype = functiontype
        self.diversityList = diversityList
        self.successRateList = successRateList
        self.replace = replace
        self.round = round
        
    
    def averageValue(self,dataValue:np.array)->np.array:
        avgData = np.zeros(self.round)
        # print(type(dataValue))
        for j in range(self.round):
            for i in range(self.replace):
                avgData[j] += dataValue[i][j]
        return (avgData/self.replace)
                
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
                 plotValue:np.array=None,problemtype:str="Small",functiontype:str="Unimodal")->None:
        self.functionname = functionname
        self.algorithmname = algorithmname
        self.data = data
        self.individual = individual
        self.problemtype = problemtype
        self.functiontype = functiontype
        self.plotValue = plotValue
    
    
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
        
        
            
    def fileWriteSolution(self)->None:
        path_file = path_result+self.problemtype+"/"+self.functiontype+"/"+self.functionname+"_"+self.algorithmname+"_solution.csv"
        self.data.to_csv(path_file,index=False)

    def fileWriteIndividual(self)->None:
        path_file = path_individual+self.functionname+"_"+self.algorithmname+"_individual.csv"
        self.data.to_csv(path_file,index=False)
        

    def analysis(self)->None:
        solution = self.data['solution']
        print("From function "+self.functionname+" with algorithmname "+self.algorithmname)
        print("Worst solution ",(max(solution)),flush=True)
        print("Best solution ",(min(solution)),flush=True)
        print("Mean solution ",(np.average(solution)),flush=True)
        print("Standart diviation ",np.std(solution),flush=True)


