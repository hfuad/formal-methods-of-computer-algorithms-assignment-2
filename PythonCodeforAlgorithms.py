prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 10

#######################################
#1- Brute Force Rod Cutting Algorithm:#
#######################################

def RodCuttingBruteForce(n, prices):
    maxPrice = 0
    for i in range(0, n):
        price = prices[i] + RodCuttingBruteForce(n-i-1, prices)
        maxPrice = max(maxPrice, price)
    return maxPrice

print("Rod Cutting Brute-Force Max. Profit is: ", RodCuttingBruteForce(n, prices))


###########################################################################################

######################################
#2- Top Bottom Rod Cutting Algorithm:#
######################################

def RodCuttingTopBottom(n, prices):
    arr = [-1000] * n
    arr[0] = 0
    maxProfit = MaxProfit(n, prices, arr)
    return maxProfit

def MaxProfit(n, prices, arr):
    if(n ==0):
        maxx = 0
    else:
        maxx = -1000
    for i in range(0, n):
        maxx = max(maxx, prices[i] + MaxProfit(n-i-1, prices, arr))
    arr[n-1] = maxx
    return arr[n-1]

print("Rod Cutting Top-Bottom Max. Profit is: ", RodCuttingTopBottom(n, prices))


###########################################################################################

#####################################
#3- Bottom Up Rod Cutting Algorithm:#
#####################################

def RodCuttingBottomUp(n, prices):
    arr = [0] * (n+1)
    arr[0] = 0
    for i in range(1, n+1):
        maxx = -1000
        for j in range(i):
            maxx = max(maxx, prices[j] + arr[i-j-1])
        arr[i] = maxx
    return arr[n]

print("Rod Cutting Bottom-Up Max. Profit is: ", RodCuttingBottomUp(n, prices))


###########################################################################################

###############################
#Order of Growth of Algorithms#
###############################

from datetime import datetime

dataSizes = [10, 100, 1000, 100000]
m = len(dataSizes)
n = len(dataSizes)
timeBruteForce = [0] * len(dataSizes)
timeTopBottom = [0] * len(dataSizes)
timeBottomUp = [0] * len(dataSizes)

def AnalyzeBruteForceAlgorithm(dataSizes, prices):
    for i in range(0, m):
        print(i)
        time1 = datetime.now()
        RodCuttingBruteForce(dataSizes[i], prices*dataSizes[i])
        time2 = datetime.now()
        timeBruteForce[i] = time2 - time1
        print(time2-time1)
    print("Data Sizes Brute-Force: ", dataSizes)
    print("Times Brute-Force: ", timeBruteForce)

def AnalyzeTopBottomAlgorithm(dataSizes, prices):
    for i in range(0, m):
        print(i)
        time1 = datetime.now()
        RodCuttingTopBottom(dataSizes[i], prices*dataSizes[i])
        time2 = datetime.now()
        timeTopBottom[i] = time2-time1
        print(time2-time1)
    print("Data Sizes Top-Bottom: ", dataSizes)
    print("Times Top-Bottom: ", timeTopBottom)

def AnalyzeBottomUpAlgorithm(dataSizes, prices):
    for i in range(0, m):
        print(i)
        time1 = datetime.now()
        RodCuttingBottomUp(dataSizes[i], prices*dataSizes[i])
        time2 = datetime.now()
        timeBottomUp[i] = time2-time1
        print(time2-time1)
    print("Data Sizes Bottom-Up: ", dataSizes)
    print("Times Bottom-Up: ", timeBottomUp)


AnalyzeBruteForceAlgorithm(dataSizes, prices)

AnalyzeTopBottomAlgorithm(dataSizes, prices)

AnalyzeBottomUpAlgorithm(dataSizes, prices)

import numpy as np
import  matplotlib.pyplot as plt

numpyDataSizes = np.array(dataSizes)
numpyTimeBruteForce = np.array(timeBruteForce)
numpyTimeTopBottom = np.array(timeTopBottom)
numpyTimeBottomUp = np.array(timeBottomUp)

plt.scatter(numpyDataSizes, numpyTimeBruteForce)
plt.show()

plt.scatter(numpyDataSizes, numpyTimeTopBottom)
plt.show()

plt.scatter(numpyDataSizes, numpyTimeBottomUp)
plt.show()
