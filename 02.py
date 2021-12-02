# Part A
hpos = 0
depth = 0
with open('02_input.txt') as txtInput:
    for line in txtInput:
        command = line.split(' ')
        if command[0] == "forward":
            hpos += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        else:
            depth -= int(command[1])
print("Part A:\nHorizontal position = " + str(hpos) + "\nDepth = " + str(depth) + "\n\nOutput = " + str(hpos * depth))

# Part B
hpos = 0
depth = 0
aim = 0
with open('02_input.txt') as txtInput:
    for line in txtInput:
        command = line.split(' ')
        if command[0] == "forward":
            hpos += int(command[1])
            depth += int(command[1]) * aim
        elif command[0] == "down":
            aim += int(command[1])
        else:
            aim -= int(command[1])
print("\n\n\n\nPart B:\nHorizontal position = " + str(hpos) + "\nDepth = " + str(depth) + "\n\nOutput = " + str(hpos * depth))