# Part A
counter = 0
lastLine = ""
with open('01_input.txt') as txtInput:
    for line in txtInput:
        if lastLine != "" and int(line) > int(lastLine):
            counter += 1
        lastLine = line
print("Number of increments in Part A: " + str(counter))

# Part B
counter = 0
mCounter = 0
mOne = 0
mTwo = 0
mNB = [0, 0, 0]
with open('01_input.txt') as txtInput:
    for line in txtInput:
        if mCounter < 3:
            mNB[mCounter] = int(line)
            mCounter += 1
            if mCounter == 3:
                mOne = mNB[0] + mNB[1] + mNB[2]
        else:
            mNB[0] = mNB[1]
            mNB[1] = mNB[2]
            mNB[2] = int(line)
            mTwo = mNB[0] + mNB[1] + mNB[2]
            if mTwo > mOne:
                counter += 1
            mOne = mTwo
print("Number of increments in Part B: " + str(counter))
