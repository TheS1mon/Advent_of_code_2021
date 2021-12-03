# Part A
counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
gamma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
epsilon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
gammaDec = ""
epsilonDec = ""
with open('03_input.txt') as txtInput:
    for line in txtInput:
        for i in range(12):
            if line[i] == "1":
                counter[i] += 1
for i in range(12):
    if counter[i] > 500:
        gamma[i] = 1
        epsilon[i] = 0
    else:
        gamma[i] = 0
        epsilon[i] = 1
print(counter)
print("Gamma: " + str(gamma) + "\nEpsilon: " + str(epsilon) + "\n\nIn Decimal:\n")
for item in gamma:
    gammaDec += str(item)
for item in epsilon:
    epsilonDec += str(item)
print("Gamma: " + str(int(gammaDec, 2)) + "\nEpsilon: " + str(int(epsilonDec, 2)))
print(str(int(gammaDec, 2) * int(epsilonDec, 2)) + "\n\n\n\n")



# Part B
counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
oxyRating = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
scrubRating = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
oxyDec = ""
scrubDec = ""
one = False
with open('03_input.txt') as txtInput:
    lines = txtInput.read().splitlines()
    linesTwo = lines.copy()
    for x in range(12):
        for line in lines:
            if line[x] == '1':
                counter[x] += 1
        if counter[x] >= int(len(lines) / 2):
            one = True
        for i in range(100):
            for line in lines:
                if one:
                    if line[x] == '0':
                        lines.remove(line)
                else:
                    if line[x] == '1':
                        lines.remove(line)
        print(lines)
    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    one = True
    for x in range(12):
        for line in linesTwo:
            if line[x] == '1':
                counter[x] += 1
        if counter[x] >= int(len(linesTwo) / 2):
            one = False
        for i in range(100):
            for line in linesTwo:
                if one:
                    if line[x] == '0':
                        linesTwo.remove(line)
                else:
                    if line[x] == '1':
                        linesTwo.remove(line)
        print(linesTwo)
#print("Gamma: " + str(gamma) + "\nEpsilon: " + str(epsilon) + "\n\nIn Decimal:\n")
#for item in gamma:
#    gammaDec += str(item)
#for item in epsilon:
#    epsilonDec += str(item)
#print("Gamma: " + str(int(gammaDec, 2)) + "\nEpsilon: " + str(int(epsilonDec, 2)))
#print(str(int(gammaDec, 2) * int(epsilonDec, 2)))