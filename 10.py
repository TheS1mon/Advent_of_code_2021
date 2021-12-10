def getInput(txtFile):
    with open(txtFile) as f:
        data = f.readlines()
    return data


def isClosingClamp(clamp):
    if clamp == ")" or clamp == "]" or clamp == "}" or clamp == ">":
        return True
    return False


def getMatchingClamp(clamp):
    i = ")]}>".index(clamp)
    return ["(", "[", "{", "<"][i]


def getWrongLines(line):
    stack = []
    for pos in line:
        if not isClosingClamp(pos):
            stack.append(pos)
        else:
            bracket = stack.pop()
            if bracket != getMatchingClamp(pos):
                return pos


def countErrScore(errBrackets):
    score = 0
    for bracket in errBrackets:
        if bracket == ")":
            score += 3
        elif bracket == "]":
            score += 57
        elif bracket == "}":
            score += 1197
        elif bracket == ">":
            score += 25137
    return score


def correctMissingLines(line):
    err = False
    stack = []
    score = 0
    for pos in line:
        if not isClosingClamp(pos):
            stack.append(pos)
        else:
            bracket = stack.pop()
            if bracket != getMatchingClamp(pos):
                err = True

    if not err:
        stack.pop()
        for i in range(len(stack)):
                tmp = stack.pop()
                score *= 5
                j = "([{<".index(tmp)
                score += [1, 2, 3, 4][j]
        return score


input = getInput("10_input.txt")

# Part A
errBrackets = []
for line in input:
    tmp = getWrongLines(line)
    if tmp != None:
        errBrackets.append(tmp)
print(countErrScore(errBrackets))

# Part B
scores = []
for line in input:
    tmp = correctMissingLines(line)
    if tmp != None:
        scores.append(tmp)
scores.sort()
print(scores[int(len(scores) / 2)])

