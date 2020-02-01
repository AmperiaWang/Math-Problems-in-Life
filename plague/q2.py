# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 15:07:07 2020

@author: AmperiaWang
"""

#question2: Answer: I = T - ( T / ( P + 1 ) ),其中 P = ( I0 / ( T - I0 ) ) * exp ( k * T * t )

import math
from matplotlib import pyplot as plt

peopleSum = 10000 #T
infectedRate = 0.0001 #k
initialInfected = 5 #I0
maxDays = 30 #最多模拟30天

daysArr = [1]
infected = []
theoreticalInfected = []
dead = []
theoreticalDead = []
infectedSum = 0
deadSum = 0

def calculateNewlyInfected(days):
    global peopleSum,infectedRate,infectedSum
    return infectedRate * infectedSum * (peopleSum - infectedSum)

def theoreticalInfectedModelForQuestion2(days):
    global peopleSum, initialInfected, infectedRate
    P = (initialInfected/(peopleSum - initialInfected)) * (math.exp(infectedRate * peopleSum * days))
    return peopleSum - (peopleSum / (P + 1))

if __name__ == "__main__":
    infected.append(initialInfected)
    infectedSum = initialInfected
    theoreticalInfected.append(theoreticalInfectedModelForQuestion2(0))
    for d in range(1,maxDays + 1):
        tempInfected = calculateNewlyInfected(d)
        infectedSum = infectedSum + tempInfected
        daysArr.append(d)
        infected.append(infectedSum)
        theoreticalInfected.append(theoreticalInfectedModelForQuestion2(d-1))
        
    plt.figure(figsize=(maxDays,12),dpi=80)
        
    plt.plot(daysArr,infected,label="感染总数",color="#0000FF")
    plt.plot(daysArr,theoreticalInfected,'--',label="感染总数",color="#00FFFF")
                 
    xlabels = [str(i) for i in daysArr]
    plt.xticks(daysArr,xlabels)
        
    plt.savefig('q2.png')
    plt.show()