class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[True] * columns] + [[True] + [False] * (columns - 2) + [True] for _ in range(rows - 2)] + [[True] * columns]


    def loop_side(self, direction, pos):
        r = []
        current_height = 0
        if direction == "LR":       # Left to Right
            current_height = lines[pos][0]
            r = range(0, self.columns, 1)
        else:      # Right to Left
            current_height = lines[pos][-1]
            r = range(self.columns - 1, -1, -1)
        for j in r:
            if not self.matrix[pos][j]: 
                if lines[pos][j] > current_height:
                    current_height = lines[pos][j]
                    self.matrix[pos][j] = True
            else:
                if lines[pos][j] > current_height:
                    current_height = lines[pos][j]

    def loop_vertical(self, direction, pos):
        r = []
        current_height = 0
        if direction == "D":       # Down
            current_height = lines[0][pos]
            r = range(0, self.columns, 1)
        else:      # Bottom to top
            current_height = lines[-1][pos]
            r = range(self.columns - 1, -1, -1)

        for i in r:
                #if matching matrix location is False (not already known as visible)
                if not self.matrix[i][pos]: 
                    if lines[i][pos] > current_height:
                        current_height = lines[i][pos]
                        self.matrix[i][pos] = True
                else:
                    if lines[i][pos] > current_height:
                        current_height = lines[i][pos]

# part 2 functions
def check_side(start, stop, jump, view):
    for r in range(start, stop, jump):
        if lines[current[0]][r] >= lines[current[0]][current[1]]:
            view = view * abs((r - current[1]))     
            break
        if r == abs(stop) - 1:
            view = view * abs((r - current[1]))
    return view

def check_vert(start, stop, jump, view):
    for r in range(start, stop, jump):
        if lines[r][current[1]] >= lines[current[0]][current[1]]:
            view = view * abs((r - current[0]))     
            break
        if r == abs(stop) - 1:
            view = view * abs((r - current[0]))
    return view


# read file input, split on each \n
with open('.\\inputs\\day8.txt', "r") as f:    
    lines = f.read().splitlines()

# lines is already a matrix lines[0][0] is the uppermost left
columns = len(lines[0])
rows = len(lines)

# for part 1, create a matching boolean matrix visible[0][0] = True. Everything on outside can be seen
visible = Matrix(rows, columns)

# loop from left to right, tracking the current highest value and marking the visible[][] True if less than or equal
for i in range(0, rows):
    visible.loop_side("LR", i)

# then loop right to left same as the first
for i in range(0, rows):
    visible.loop_side("RL", i)

# then loop by column top to bottom
for j in range(0, columns):
    visible.loop_vertical("D", j)

# then loop by column bottom to top
for j in range(0, columns):
    visible.loop_vertical("U", j)

# loop over matrix and count how many False's are left
count = 0
for x in visible.matrix:
    for y in x:
        if y:
            count += 1

print("The number of trees not visible are: {}".format(count))

## Part 2 
# best = index i, index j, score
best_yet = [0, 0, 0]
current = [0, 0]
view = 1
for i in range(1, rows - 1):
    for j in range(1, columns - 1):
        view = 1
        current = [i, j]
        # look right
        view = check_side(current[1] + 1, columns, 1, view)

        # look left
        view = check_side(current[1] - 1, -1, -1, view)

        # look down
        view = check_vert(current[0] + 1, rows, 1, view)

        # look up
        view = check_vert(current[0] - 1, -1, -1, view)

        if view > best_yet[2]:
            best_yet = current + [view]

print("The most trees {} is at table location {}, {}".format(best_yet[2], best_yet[0] + 1, best_yet[1] ))