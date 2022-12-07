import re

# read file input, split on each \n
with open('.\\inputs\\day5.txt', "r") as f:    
    lines = f.readlines()

crates = []
instructions = []
columns = 0

# Split input between instruction set, get count for crate width
# align boxes and ignore empty line
for line in lines:
    if "move" in line:
        instructions.append(line.strip())
    elif (line.startswith(' 1')):
        columns = int(line[-3])
    elif "[" in line:
        crates.insert(0,line)
    else:
        pass

# order the crates from the initial input
boxes = []
holder = 0

for x in range(0, columns):
    box = []
    for c in crates:
        holder = (x * 4) + 1
        val = c[holder]
        if val.isalnum():
            box.append(val)
    boxes.append(box)

for inst in instructions:
    cmd = inst.split()
    holding = []

    # x.append(y.pop()) take last of y and add as last of x
    for i in range(0, int(cmd[1])):
        holding.append(boxes[int(cmd[3]) - 1].pop()) 
    # reloop to reorder into the original order popped 
    for x in range(0, len(holding)):
        boxes[int(cmd[5]) - 1].append(holding.pop())

for x in range (0, columns):
    print(boxes[x][-1], end="")

