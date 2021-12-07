def getInput(txtFile):
    with open(txtFile) as f:
        data = f.readlines()
    return data

def progressCounter(progress, progressStep):
    newProgress = progress
    newProgress += progressStep
    if round(progress) != round(newProgress):
        print(str(round(newProgress)) + "%")
    progress = newProgress
    return progress

def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def partA(data):
    _maxPos = 2000
    # Only Data[0] is relevant here
    crabs = list(map(int, data[0].split(',')))
    proxFuel = []
    progress = 0
    for x in range(_maxPos):
        moveCounter = []
        for crab in crabs:
            if crab > x + 1:
                moveCounter.append(crab - (x + 1))
            else:
                moveCounter.append((x + 1) - crab)
        progress = progressCounter(progress, 100 / _maxPos)
        proxFuel.append(0)  # Entry for the new value
        for counter in moveCounter:
            proxFuel[x] += counter
    print(proxFuel)
    sortedProxFuel = proxFuel.copy()
    sortedProxFuel = bubbleSort(sortedProxFuel)
    print(sortedProxFuel)
    print("Lowest fuel counter on: " + str(proxFuel.index(sortedProxFuel[0]) + 1) + " with " + str(sortedProxFuel[0]) + " Fuel consumed to get to this field.")


def partB(data):
    _maxPos = 2000
    # Only Data[0] is relevant here
    crabs = list(map(int, data[0].split(',')))
    proxFuel = []
    progress = 0
    for x in range(_maxPos):
        moveCounter = []
        for crab in crabs:
            counter = 0
            if crab > x + 1:
                for i in range(crab - (x + 1)):
                    counter += i + 1
            else:
                for i in range((x + 1) - crab):
                    counter += i + 1
            moveCounter.append(counter)
        progress = progressCounter(progress, 100 / _maxPos)
        proxFuel.append(0)  # Entry for the new value
        for counter in moveCounter:
            proxFuel[x] += counter
    print(proxFuel)
    sortedProxFuel = proxFuel.copy()
    sortedProxFuel = bubbleSort(sortedProxFuel)
    print(sortedProxFuel)
    print("Lowest fuel counter on: " + str(proxFuel.index(sortedProxFuel[0]) + 1) + " with " + str(sortedProxFuel[0]) + " Fuel consumed to get to this field.")


partB(getInput("07_input.txt"))
