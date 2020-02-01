# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:39:38 2020

@author: AmperiaWang
"""

#question1: Answer: I = I0 * exp ( k * t )

import math
from matplotlib import pyplot as plt

peopleSum = 1e37 #S
infectedRate = 0.05 #k
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
    global peopleSum, infectedSum, infectedRate
    return infectedRate * infectedSum

def theoreticalInfectedModelForQuestion1(days):
    global initialInfected, infectedRate
    return initialInfected * math.exp(infectedRate * days)

if __name__ == "__main__":
    infected.append(initialInfected)
    theoreticalInfected.append(theoreticalInfectedModelForQuestion1(0))
    infectedSum = initialInfected
    for d in range(2,maxDays + 1):
        tempInfected = calculateNewlyInfected(d)
        infectedSum = infectedSum + tempInfected
        daysArr.append(d)
        infected.append(infectedSum)
        theoreticalInfected.append(theoreticalInfectedModelForQuestion1(d-1))
        
    plt.figure(figsize=(maxDays,12),dpi=80)
        
    plt.plot(daysArr,infected,label="感染总数",color="#0000FF")
    plt.plot(daysArr,theoreticalInfected,'--',label="感染总数",color="#00FFFF")
                 
    xlabels = [str(i) for i in daysArr]
    plt.xticks(daysArr,xlabels)
        
    plt.savefig('q1.png')
    plt.show()