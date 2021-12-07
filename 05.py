# Generate Matrix 1000*1000
matrix = []
tmp = []
lines= []
for i in range(1000):
    tmp.append(0)
for i in range(1000):
    matrix.append(tmp)
# Process input
with open('05_input.txt') as txtInput:
    for line in txtInput:
        line = line.split(" ")
        tmpLine = [line[0].split(','), line[2].split(',')]
        tmpLine[0][0] = int(tmpLine[0][0])
        tmpLine[0][1] = int(tmpLine[0][1])
        tmpLine[1][0] = int(tmpLine[1][0])
        tmpLine[1][1] = int(tmpLine[1][1])
        # Consider only horizontal and vertical lines
        if tmpLine[0][0] == tmpLine[1][0] or tmpLine[0][1] == tmpLine[1][1]:
            lines.extend([tmpLine])
for line in lines:
    if line[0][0] == line[1][0]:  # vertical lines
        if line[0][1] < line[1][1]:  # if second value is higher
            for x in range(line[1][1] - line[0][1]):
                matrix[line[0][0]][line[0][1] + x] += 1
        else:  # if first value is higher
            for x in range(line[0][1] - line[1][1]):
                matrix[line[0][0]][line[1][1] + x] += 1
    else:  # horizontal lines
        if line[0][0] < line[1][0]:  # if second value is higher
            for x in range(line[1][0] - line[0][0]):
                matrix[line[0][0] + x][line[1][1]] += 1
        else:  # if first value is higher
            for x in range(line[0][0] - line[1][0]):
                matrix[line[1][0] + x][line[0][1]] += 1
counter = 0
for row in matrix:
    for x in range(1000):
        if x != 0 and x != 1:
            counter += row.count(x)
print(counter)