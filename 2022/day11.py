class Monkey:
    def __init__(self, items, test, tr, fa, op):
        self.items = items
        self.test = test
        self.tr = tr
        self.fa = fa
        self.op = op
        self.activity = 0

    def update_count(self):
        self.activity += 1

    def get_test(self):
        return self.test

    def get_items(self):
        return self.items

    def get_op(self):
        return str(self.op)

    def get_activity(self):
        return int(self.activity)

    def test_item(self, worry: int):
        w = worry // 3
        if w % self.test == 0:
            return self.tr, w
        else:
            return self.fa, w

    def add_item(self, item):
        self.items.append(item)

    def clear(self):
        self.items = []


def main():
    # read file input, split on each \n
    with open('.\\inputs\\day11.txt', "r") as f:    
        lines = f.read().splitlines()


    # holder current monkeys
    monkeys = []


    # read input
    for x in range(0, len(lines), 7):
        # create list of starting items/worries
        l1 = lines[x+1].split(":")[1]
        items = [int(i) for i in l1.split(",")]

        # put operation string (later eval()) in list
        l2 = lines[x+2].split("=")[1]
        if "*" in l2:
            l2_split = l2.split("*")
            op = "*"
        else:
            l2_split = l2.split("+")
            op = "+"
        op = l2_split[0].strip() + op + l2_split[1].strip()

        # create function to test where to throw for each
        div = int(lines[x+3].split("y")[1])
        
        monkeys.append(Monkey(items=items, op=op, test=div, \
            tr=int(lines[x+4][-1]), fa=int(lines[x+5][-1])))


    # for 20 rounds
    for round in range(0, 20):
        # for each monkey in order
        for n in range(0, len(monkeys)): 
            # for each item the monkey holds in order
            old_list = monkeys[n].get_items()
            start_len = len(old_list)
            for i in range(0, start_len):
                monkeys[n].update_count()
                op = monkeys[n].get_op()
                old = old_list[i]
                new = eval(op)
                next_monkey, new_worry = monkeys[n].test_item(new)
                monkeys[next_monkey].add_item(new_worry)
            monkeys[n].clear()

    highest = [m.get_activity() for m in monkeys]
    highest.sort()
    print(highest[-1] * highest[-2])

if __name__ == "__main__":
    main()
