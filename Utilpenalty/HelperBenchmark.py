import numpy as np
import math


'''
Created on Jan 1, 2024

@author: patipan
'''

def signX(x:np.array)->np.array:
    signx = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] < 0:
            signx[i] = -1
        elif x[i] == 0:
            signx[i] = 0
        else:
            signx[i] = 1
    return signx

def matrixA(alpha:float=0,dimensionSize:int=30)->np.array:
    matrixReturn = np.zeros((dimensionSize,dimensionSize))
    for i in range(dimensionSize):
        for j in range(dimensionSize):
            if i == j:
                matrixReturn[i][j] = math.pow(alpha, i/(2*(dimensionSize-1)))
    return matrixReturn

def tAsy(x:np.array,beta:float=0)->np.array:
    dumX = x
    for i in range(len(x)):
        if dumX[i] > 0:
            val = (beta*i*math.sqrt(len(x)))/(len(x)-1)
            val += 1
            dumX[i] = math.pow(dumX[i], val)
    return dumX

def c1(x:np.double)->np.double:
    if x > 0:
        return 10
    else:
        return 5.5
    
def c2(x:np.double)->np.double:
    if x > 0:
        return 7.9
    else:
        return 3.1

def tOsz(x:np.array)->np.array:
    signx = signX(x)
    xp = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] != 0:
            xp[i] = math.log10(abs(x[i]))
        else:
            xp[i] = 0
    for i in range(len(x)):
        sinC1 = math.sin(c1(x[i])*xp[i])
        sinC2 = math.sin(c2(x[i])*xp[i])
        x[i] = signx[i]*math.exp(xp[i]+0.049*(sinC1+sinC2))
    return x
