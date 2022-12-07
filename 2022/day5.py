import re

# read file input, split on each \n
with open('.\\inputs\\day5.txt', "r") as f:    
    lines = f.readlines()

crates = []
instructions = []
columns = 0

# Split input between instruction set, get count for crate width
for line in lines:
    if "move" in line:
        instructions.append(line.strip())
    elif (line.startswith(' 1')):
        columns = int(line[-3])
    # input to align boxes and ignore empty line
    elif "[" in line:
        crates.insert(0,line)
    else:
        pass

boxes = []
holder = 0

# order the crates from the initial input. Looping by position index first
for x in range(0, columns):
    box = []
    # loop for each line of crate isntruction. The first line is the top
    for c in crates:
        # each crate is 3 characters + 1 space between them
        holder = (x * 4) + 1

        # what letter, [, ], or " " is in this 2-D location
        val = c[holder]
        if val.isalnum():
            box.append(val)
    
    # add a list entry for position n 
    boxes.append(box)

for inst in instructions:
    # input "move 1 from 2 to 3"  becomes [1,2,3] which is shorthand for
    # take 1 crate from top (end) of stack 2 and add to top (end) of 3 one at a time
    cmd = inst.split()

    # x.append(y.pop()) one at a time to reverse order 
    for i in range(0, int(cmd[1])):
        boxes[int(cmd[5]) - 1].append(boxes[int(cmd[3]) - 1].pop())

# Outputs the top boxes in position order
for x in range (0, columns):
    print(boxes[x][-1], end="")

