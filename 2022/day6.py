
# part one stream is 4 chars
#initialization = 4
# start of message is 14 chars
initialization = 14

# read file input, split on each \n
with open('.\\inputs\\day6.txt', "r") as f:    
    line = f.readline()

for position in range(0, len(line)):
    code = set(line[position:position+initialization])
    if len(code) == initialization:
        print("The start is at character {}".format(position + len(code)))
        break

