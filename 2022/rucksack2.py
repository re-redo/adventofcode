# imports


# read file input, split on each \n
with open('C:\\Users\\Max\\git\\adventofcode\\2022\\inputs\\day3.txt', "r") as f:    
    packs = f.readlines()

total = 0

# look at 3 lines 
for i in range(0, len(packs), 3):
    # find the upper or lowercase letter common between the pieces
    common = ""
    for letter in packs[i]:
        if letter in packs[i + 1] and letter in packs[i + 2]:
            common = letter
            break

    # a-z numbers 1-26, A-Z are 27-52
    # a -z == ord(letter) - 96
    # A-Z == ord(letter) - 38
    if ord(common) < 91:
        value = ord(common) - 38
    else:
        value = ord(common) - 96

# # sum the value of the shared letter in each line 
    total += value

print("Priority sum = {}".format(total))