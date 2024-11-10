from Benchmark.ConstraintOptimizationCEC2017set1 import C01, C02, C03, C04, C05, C06, C07
from NewDE.DE import DE

populationSize = 100
dimensionSize = 10


def cec2017ConstraintSet1():
    deObj = DE(constraintClass=C01,populationSize=populationSize,dimensionSize=dimensionSize,replace=3,problemtype="Small",functionname="CEC2017Constraint-C01",algorithmname="DE_10di")
    deObj.optimized()

    deObj = DE(constraintClass=C02,populationSize=populationSize,dimensionSize=dimensionSize,replace=3,problemtype="Small",functionname="CEC2017Constraint-C02",algorithmname="DE_10di")
    deObj.optimized()

    deObj = DE(constraintClass=C03,populationSize=populationSize,dimensionSize=dimensionSize,replace=3,problemtype="Small",functionname="CEC2017Constraint-C03",algorithmname="DE_10di")
    deObj.optimized()

    deObj = DE(constraintClass=C04,populationSize=populationSize,dimensionSize=dimensionSize,replace=3,problemtype="Small",functionname="CEC2017Constraint-C04",algorithmname="DE_10di")
    deObj.optimized()

    deObj = DE(constraintClass=C05,populationSize=populationSize,dimensionSize=dimensionSize,replace=3,problemtype="Small",functionname="CEC2017Constraint-C05",algorithmname="DE_10di")
    deObj.optimized()

    deObj = DE(constraintClass=C06,populationSize=populationSize,dimensionSize=dimensionSize,replace=3,problemtype="Small",functionname="CEC2017Constraint-C06",algorithmname="DE_10di")
    deObj.optimized()

    deObj = DE(constraintClass=C07,populationSize=populationSize,dimensionSize=dimensionSize,replace=3,problemtype="Small",functionname="CEC2017Constraint-C07",algorithmname="DE_10di")
    deObj.optimized()




def deTest10diCEC2017Constraint():
    cec2017ConstraintSet1()
