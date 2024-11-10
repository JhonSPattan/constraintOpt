
from Benchmark.ConstraintOptimizationCEC2017set1 import C01, C02, C03, C04, C05, C06, C07
from Benchmark.ConstraintOptimizationCEC2017set2 import C08, C09, C10, C11, C12, C13, C14
from Benchmark.ConstraintOptimizationCEC2017set3 import C15, C16, C17, C18, C19, C20, C21
from Benchmark.ConstraintOptimizationCEC2017set4 import C22, C23, C24, C25, C26, C27, C28
from multiprocessing import Process
from BSA.BSA_SAe import BSA_SAe

populationSize = 50
dimensionSize = 30


def cec2017ConstraintSet1():
    deObj = BSA_SAe(constraintClass=C01,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C01",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C02,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C02",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C03,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C03",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C04,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C04",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C05,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C05",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C06,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C06",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C07,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C07",algorithmname="BSA_SAe_30di")
    deObj.optimized()

def cec2017ConstraintSet2():
    deObj = BSA_SAe(constraintClass=C08,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C08",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C09,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C09",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C10,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C10",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C11,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C11",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C12,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C12",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C13,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C13",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C14,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C14",algorithmname="BSA_SAe_30di")
    deObj.optimized()


def cec2017ConstraintSet3():
    deObj = BSA_SAe(constraintClass=C15,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C15",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C16,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C16",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C17,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C17",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C18,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C18",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C19,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C19",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C20,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C20",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C21,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C21",algorithmname="BSA_SAe_30di")
    deObj.optimized()


def cec2017ConstraintSet4():
    deObj = BSA_SAe(constraintClass=C22,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C22",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C23,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C23",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C24,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C24",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C25,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C25",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C26,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C26",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C27,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C27",algorithmname="BSA_SAe_30di")
    deObj.optimized()

    deObj = BSA_SAe(constraintClass=C28,populationSize=populationSize,dimensionSize=dimensionSize,replace=25,problemtype="Small",functionname="CEC2017Constraint-C28",algorithmname="BSA_SAe_30di")
    deObj.optimized()


def bsa_saeTest30diCEC2017Constraint():
    # p1 = Process(target=cec2017ConstraintSet1)
    # p2 = Process(target=cec2017ConstraintSet2)
    # p3 = Process(target=cec2017ConstraintSet3)
    p4 = Process(target=cec2017ConstraintSet4)

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # p3.start()
    p4.start()
    # p3.join()
    p4.join()

    print("All process in BSA_SAe with CEC2017 constraint 30 dimension is complete",flush=True)
