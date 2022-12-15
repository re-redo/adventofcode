
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

    def check_too_far(self, other):
        if abs(self.x - other.x) > 1 or abs(self.y - other.y) > 1:
            return True
        else:
            return False

    def move_horizontal(self, distance):
        if distance[0] >= 1 :
            self.left()
        elif distance[0] <= -1:
            self.right()

    def move_vertical(self, distance):
        if distance[1] >= 1:
            self.down()
        elif distance[1] <= -1:
            self.up()

    def move_closer(self, other):
        distance = (self.x - other.x, self.y - other.y)
        if (abs(distance[0]) == 1 and abs(distance[1]) == 2) or \
            (abs(distance[0]) == 2 and abs(distance[1]) == 1):
            self.move_horizontal(distance)
            self.move_vertical(distance)
        elif (abs(distance[0]) > 1):
            self.move_horizontal(distance)
        else:
            self.move_vertical(distance)
        return (self.x, self.y)


# set init locations
head = Point(0,0)
tail = Point(0,0)
tail_spots = {(0,0)}

# read file input, split on each \n
with open('.\\inputs\\day9.txt', "r") as f:    
    lines = f.read().splitlines()

for line in lines:
    input = line.split()
    action = head.up
    if input[0] == "U":
        action = head.up
    elif input[0] == "D":
        action = head.down
    elif input[0] == "R":
        action = head.right
    else:           # Left
        action = head.left

    for i in range(0, int(input[1])):
        action()
        if tail.check_too_far(head):
            tail_spots.add(tail.move_closer(head))

print(len(tail_spots))