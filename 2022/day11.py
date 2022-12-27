
# int(x/y) rounds down

# read file input, split on each \n
with open('.\\inputs\\day11.txt', "r") as f:    
    lines = f.read().splitlines()

# declare global 
monkeys_have = {}
monkeys_op = []
monkeys_test = []
activity = []

# read input
for x in range(0, len(lines), 7):
    l1 = lines[x]
    key = int(l1[-2])
    activity.append(0)

    # put starting items value in dict
    items = []
    l2 = lines[x+1].split(":")[1]
    for i in l2.split(","):
        items.append(int(i))
    monkeys_have[key] = items
    
    # put operation string (later eval()) in list
    l3 = lines[x+2].split("=")[1]
    if "*" in l3:
        l3_split = l3.split("*")
        op = "*"
    else:
        l3_split = l3.split("+")
        op = "+"
    monkeys_op.append(l3_split[0].strip() + op + l3_split[1].strip())


    # assign conditions
    l4 = lines[x+4]
    l5 = lines[x+5]

    # create function to test where to throw for each
    def f(worry = 0, x = x, l4=l4, l5=l5):
        y = int(worry / 3)
        # if true throw to monkey listed on line 4 otherwise line 5
        if y % int(lines[x+3].split("y")[1]) == 0:
            return int(l4[-1])
        else:
            return int(l5[-1])
    monkeys_test.append(f)

# print(monkeys_have)
# print(monkeys_op)
#print(monkeys_test[3](worry=105))

# for 20 rounds
for round in range(0, 20):
    # for each monkey in order
    for n in range(0, len(monkeys_have)): 
        # for each item the monkey holds in order
        start_len = len(monkeys_have[n])
        for i in range(0, start_len):
            activity[n] += 1
            old = monkeys_have[n][i]
            new = eval(monkeys_op[n])
            next_monkey = monkeys_test[n](worry = new)
            #print("{} becomes {} and goes to monkey {}".format(old, int(new/3), next_monkey))
            monkeys_have[next_monkey].append(int(new/3))
        monkeys_have[n] = []
    print(activity)
print(monkeys_have)

activity.sort()
print(activity[-1] * activity[-2])