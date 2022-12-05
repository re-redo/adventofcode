import re

def compare(list1, list2):
    flag = False
    for item in list1:
        if item in list2:
            flag = True
    return flag

# read file input, split on each \n
with open('C:\\Users\\Max\\git\\adventofcode\\2022\\inputs\\day4.txt', "r") as f:    
    lines = f.readlines()

count = 0

for line in lines:
    input = re.split("[-,]", line.strip())
    one_test = compare(range(int(input[0]), int(input[1]) + 1), range(int(input[2]), int(input[3]) + 1))
    if (one_test):
        count += 1

print("There is double work for {} elves".format(count))