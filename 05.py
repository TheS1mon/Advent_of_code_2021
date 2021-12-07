# Generate Matrix 1000*1000
matrix = []
tmp = []
for i in range(1000):
    tmp.append('0')
    matrix.append([])
for i in range(1000):
    matrix[i].append(tmp)
# Process input
with open('05_input.txt') as txtInput:
    for line in txtInput:
        line = line.split(" ")
        print(line)