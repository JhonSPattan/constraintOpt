from BenchmarkPenalty.ConstraintOptimizationPenaltyCEC2017set1 import C01penalty, C02penalty, C03penalty, C04penalty, C05penalty, C06penalty, C07penalty
from BenchmarkPenalty.ConstraintOptimizationPenaltyCEC2017set2 import C08penalty, C09penalty, C10penalty, C11penalty, C12penalty, C13penalty, C14penalty
from BenchmarkPenalty.ConstraintOptimizationPenaltyCEC2017set3 import C15penalty, C16penalty, C17penalty, C18penalty, C19penalty, C20penalty, C21penalty
from BenchmarkPenalty.ConstraintOptimizationPenaltyCEC2017set4 import C22penalty, C23penalty, C24penalty, C25penalty, C26penalty, C27penalty, C28penalty


from multiprocessing import Process
from BSApenalty.HLBSA import HLBSA

populationSize = 100
dimensionSize = 10



def cec2017ConstraintSet1():
    deObj = HLBSA(constraintClass=C01penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C01",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C02penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C02",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C03penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C03",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C04penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C04",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C05penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C05",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C06penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C06",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C07penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C07",algorithmname="HLBSA_10di")
    deObj.optimized()

def cec2017ConstraintSet2():
    deObj = HLBSA(constraintClass=C08penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C08",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C09penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C09",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C10penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C10",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C11penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C11",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C12penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C12",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C13penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C13",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C14penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C14",algorithmname="HLBSA_10di")
    deObj.optimized()


def cec2017ConstraintSet3():
    deObj = HLBSA(constraintClass=C15penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C15",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C16penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C16",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C17penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C17",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C18penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C18",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C19penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C19",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C20penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C20",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C21penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C21",algorithmname="HLBSA_10di")
    deObj.optimized()


def cec2017ConstraintSet4():
    deObj = HLBSA(constraintClass=C22penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C22",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C23penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C23",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C24penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C24",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C25penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C25",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C26penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C26",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C27penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C27",algorithmname="HLBSA_10di")
    deObj.optimized()

    deObj = HLBSA(constraintClass=C28penalty,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C28",algorithmname="HLBSA_10di")
    deObj.optimized()



def hlbsaTest10diCEC2017ConstraintPenalty():
    p1 = Process(target=cec2017ConstraintSet1)
    p2 = Process(target=cec2017ConstraintSet2)
    p3 = Process(target=cec2017ConstraintSet3)
    p4 = Process(target=cec2017ConstraintSet4)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    p3.start()
    p4.start()
    p3.join()
    p4.join()

    print("All process in HLBSA with CEC2017 constraint 10 dimension is complete")