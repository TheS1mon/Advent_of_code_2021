import numpy as np


def getInput(txtFile):
    with open(txtFile) as f:
        data = f.readlines()
    return data


def getMatrix(data):
    matrix = [[]]
    for i, line in enumerate(data):
        matrix.append([])
        for character in line:
            try:
                matrix[i].append(int(character))
            except:
                pass
    return matrix


def checkNeighbours(matrix):
    lowPoints = []
    for x, line in enumerate(matrix):
        for y, character in enumerate(line):
            isLowest = True
            try:
                if character >= matrix[x][y - 1]: isLowest = False
            except:
                pass
            try:
                if character >= matrix[x][y + 1]: isLowest = False
            except:
                pass
            try:
                if character >= matrix[x + 1][y]: isLowest = False
            except:
                pass
            try:
                if character >= matrix[x - 1][y]: isLowest = False
            except:
                pass
            if isLowest:
                lowPoint = {
                    "value" : character,
                    "x" : x,
                    "y" : y
                }
                lowPoints.append(lowPoint)
    return lowPoints


def calcRiskLevel(lowPoints):
    riskLevel = 0
    for lowPoint in lowPoints:
        riskLevel += lowPoint.get("value") + 1
    return riskLevel


def calcSumOfBasins(lowPoint, matrix):
    global accessMatrix
    sum = 1
    newPoint = {
        "value": "",
        "x": 0,
        "y": 0
    }
    accessMatrix[lowPoint.get("x")][lowPoint.get("y")] = 1
    try:
        newPoint["value"] = matrix[lowPoint.get("x")][lowPoint.get("y") - 1]
        newPoint["x"] = lowPoint.get("x")
        newPoint["y"] = lowPoint.get("y") - 1
        if lowPoint.get("value") < newPoint.get("value"):
            if matrix[newPoint.get("x")][newPoint.get("y")] != 9:
                if accessMatrix[newPoint.get("x")][newPoint.get("y")] == 0:
                    sum += calcSumOfBasins(newPoint, matrix)
    except:
        pass
    try:
        newPoint["value"] = matrix[lowPoint.get("x")][lowPoint.get("y") + 1]
        newPoint["x"] = lowPoint.get("x")
        newPoint["y"] = lowPoint.get("y") + 1
        if lowPoint.get("value") < newPoint.get("value"):
            if matrix[newPoint.get("x")][newPoint.get("y")] != 9:
                if accessMatrix[newPoint.get("x")][newPoint.get("y")] == 0:
                    sum += calcSumOfBasins(newPoint, matrix)
    except:
        pass
    try:
        newPoint["value"] = matrix[lowPoint.get("x") + 1][lowPoint.get("y")]
        newPoint["x"] = lowPoint.get("x") + 1
        newPoint["y"] = lowPoint.get("y")
        if lowPoint.get("value") < newPoint.get("value"):
            if matrix[newPoint.get("x")][newPoint.get("y")] != 9:
                if accessMatrix[newPoint.get("x")][newPoint.get("y")] == 0:
                    sum += calcSumOfBasins(newPoint, matrix)
    except:
        pass
    try:
        newPoint["value"] = matrix[lowPoint.get("x") - 1][lowPoint.get("y")]
        newPoint["x"] = lowPoint.get("x") - 1
        newPoint["y"] = lowPoint.get("y")
        if lowPoint.get("value") < newPoint.get("value"):
            if matrix[newPoint.get("x")][newPoint.get("y")] != 9:
                if accessMatrix[newPoint.get("x")][newPoint.get("y")] == 0:
                    sum += calcSumOfBasins(newPoint, matrix)
    except:
        pass
    return sum


input = getInput("09_input.txt")
matrix = getMatrix(input)
lowPoints = checkNeighbours(matrix)
print(calcRiskLevel(lowPoints))
basins = []

accessMatrix = []
for x in range(100):
    accessMatrix.append([])
    for y in range(100):
        accessMatrix[x].append(0)
print(accessMatrix)

for lowPoint in lowPoints:
    basins.append(calcSumOfBasins(lowPoint, matrix))

basins.sort()
print(basins)
print(basins[-3] * basins[-2] * basins[-1])