class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def up(self):
        self.y = self.y + 1

    def down(self):
        self.y = self.y - 1
    
    def left(self):
        self.x = self.x - 1

    def right(self):
        self.x = self.x + 1

    # Is node1 further than 1 space from another
    def check_too_far(self, other):
        if abs(self.x - other.x) > 1 or abs(self.y - other.y) > 1:
            return True
        else:
            return False

    # Move left or right depending on +- of difference
    def move_horizontal(self, distance):
        if distance[0] >= 1 :
            self.left()
        elif distance[0] <= -1:
            self.right()

    # Move up or down depending on +- of difference
    def move_vertical(self, distance):
        if distance[1] >= 1:
            self.down()
        elif distance[1] <= -1:
            self.up()

    # Handle logic to manage diagonal motion
    def move_closer(self, other):
        distance = (self.x - other.x, self.y - other.y)
        if (abs(distance[0]) >= 1 and abs(distance[1]) >= 2) or \
            (abs(distance[0]) >= 2 and abs(distance[1]) >= 1):
            self.move_horizontal(distance)
            self.move_vertical(distance)
        elif (abs(distance[0]) > 1):
            self.move_horizontal(distance)
        else:
            self.move_vertical(distance)
        return (self.x, self.y)

# pull out function to move node based on input
def action(knot, dir):
    if dir == "U":
        return knot.up
    elif dir == "D":
        return knot.down
    elif dir == "R":
        return knot.right
    else:           # Left
        return knot.left

# set init locations
head = Point(0,0)
tail = Point(0,0)
# rope[n] = [Point(0,0), Active Flag]
rope = [[head, True]] + [[Point(0,0), False] for _ in range(1, 9)] + [[tail, False]] 
tail_spots = {(0,0)}

# read file input, split on each \n
with open('.\\inputs\\day9.txt', "r") as f:    
    lines = f.read().splitlines()

# for each instruction line
for line in lines:
    input = line.split()

    # loop for each step
    for i in range(0, int(input[1])):   
        # move head
        action(head, input[0])()

        # act on each knot after moving head, don't move if thing before hasn't moved
        for n in range(1,10):
            if rope[n - 1][1]:          # if previous knot in motion move this one True, move
                if rope[n][0].check_too_far(rope[n-1][0]):      # check if too far from next node
                    new_spot = rope[n][0].move_closer(rope[n-1][0])
                    rope[n][1] = True

                    # add to tail_spots
                    if n == 9:
                        tail_spots.add(new_spot)


print(len(tail_spots))