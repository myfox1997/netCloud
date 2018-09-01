from numpy import *
import numpy as np
import random


def loadData(fileName):
    file = open(fileName)
    dataMat = []
    category = [0]
    for line in file.readlines():
        curLine = line.strip().split('\t')
        curLine = list(map(float, curLine)) + category
        dataMat.append(curLine)
    data = np.array(dataMat)
    return data

def calEclud(vecA, vecB):
    return sqrt(pow(vecA[1] - vecB[1], 2) + pow(vecA[2] - vecB[2], 2))

def initCenter(data, K):
    maxX = max(data[:, 1])
    minX = min(data[:, 1])
    maxY = max(data[:, 2])
    minY = min(data[:, 2])
    center = np.zeros((K, 4))
    for i in range(0, K):
        center[i][0] = i
        center[i][1] = round(random.random() * (maxX - minX) + minX, 1)
        center[i][2] = round(random.random() * (maxY - minY) + minY, 1)
    # print(center)
    return center


def calNewCenter(data, K):
    tmpX = tmpY = count = 0
    center = np.zeros((K, 4))
    for i in range(0, K):
        center[i][0] = i
        for each in data:
            if each[3] == i:
                tmpX += each[1]
                tmpY += each[2]
                count += 1
        if count != 0:
            center[i][1] = tmpX / count  # (count+1)
            center[i][2] = tmpY / count  # (count+1)
        tmpX = tmpY = count = 0
    return center


def diff(CenterA, CenterB):
    return sqrt(sum(power(CenterA - CenterB, 2)))

def classify(eachData, center):
    minDis = 9999
    for i in range(0, len(center)):
        if(calEclud(eachData, center[i]) < minDis):
            minDis = calEclud(eachData, center[i])
            eachData[3] = i
    return eachData

def KMeans(data, K, Center, threshold):
    lastCenter = Center  # 0
    thisCenter = Center  # 0
    count = 1
    for i in range(0, len(data)):
        data[i] = classify(data[i], thisCenter)
    thisCenter = calNewCenter(data, K)  # calNewCenter
    while diff(lastCenter, thisCenter) >= threshold:
        count += 1
        lastCenter = thisCenter  # last2new    1
        for i in range(0, len(data)):
            data[i] = classify(data[i], thisCenter)
        thisCenter = calNewCenter(data, K)
    return data, thisCenter, count

if __name__ == '__main__':
    fileName = 'samples.txt'
    data = loadData(fileName)
    classification = 2
    print("here is the original data")
    print(data)
    center = initCenter(data, classification)
    print("here is the original center")
    print(center)
    data, center, count = KMeans(data, classification, center, 0.2)
    print("here is the final data")
    print(data)
    print("here is the final center")
    print(center)
    print("iteration")
    print(count)
