class Strength():
    def __init__(self, count):
        self.strength = count

    # strength cycle * x
    def strength_update(self, cycle, x):
        self.strength += (cycle * x)

def cycle_check(s, cycle, x):
    # if cycle 20, 60, 100, 140 do strength
    if cycle == 20 or (cycle + 20) % 40 == 0:
        s.strength_update(cycle, x)

# read file input, split on each \n
with open('.\\inputs\\day10.txt', "r") as f:    
    lines = f.read().splitlines()

# register x, starts at 1
x = 1
cycles = 0
s = Strength(0)

# read each line
for line in lines:
    l = line.split()
    # if no-op increase cycle count by 1
    if "noop" in l[0]:
        cycles += 1
        cycle_check(s, cycles, x)
    # else addx N
    else:
        # cycles up by 2
        for i in range(0, 2):
            cycles +=1
            cycle_check(s, cycles, x)
        # only then add N to X register 
        x += int(l[1])
print("After {} cycles the register is {} and the total strength is {}.".format(cycles, x, s.strength))



    
    