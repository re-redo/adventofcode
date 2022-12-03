import requests
from sys import argv, exit
import re


# usage message
if len(argv) < 2:
    print("Usage python3 tictactoe.py $SESSION_COOKIE")
    exit(1)

worth_matrix = {"A": 1, "B" : 2, "C" : 3, "X" : 1, "Y" : 2, "Z" : 3, "win" : 6, "draw" : 3, "lose" : 0}

# get data
input_url = "https://adventofcode.com/2022/day/2/input"
cookies = {"session": argv[1]}
data = requests.get(input_url, cookies=cookies).text

# split each input for both people on blank space
rounds = re.split(r'[\s]', data)
score = 0

for choice in range(0, len(rounds) - 1, 2):
        result = 0
        p1_choice = worth_matrix.get(rounds[choice])
        p2_choice = worth_matrix.get(rounds[(choice + 1)])
        if p2_choice == p1_choice:
                result = worth_matrix.get("draw")
        elif (p2_choice == 1 and p1_choice == 3) or (p2_choice == 2 and p1_choice == 1) or (p2_choice == 3 and p1_choice == 2):
                result = worth_matrix.get("win")
        else:
                result = worth_matrix.get("lose")
        total = p2_choice + result
        score += total

print("I will score {} points".format(score))

