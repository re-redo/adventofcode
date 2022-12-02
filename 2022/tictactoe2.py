import requests
from sys import argv, exit
import re


# usage message
if len(argv) < 2:
    print("Usage: python3 tictactoe.py $SESSION_COOKIE")
    exit(1)

worth_matrix = {"A": 1, "B" : 2, "C" : 3, \
    "X" : "lose", "Y" : "draw", "Z" : "win", \
        "win" : 6, "draw" : 3, "lose" : 0}
win_matrix = {"win" : {1:2, 3:1, 2:3}, "lose" : {1:3, 2:1, 3:2}, "draw" : {1:1, 2:2, 3:3}}

# get data
input_url = "https://adventofcode.com/2022/day/2/input"
cookies = {"session": argv[1]}

data = requests.get(input_url, cookies=cookies).text

# split each input for both people on blank space
rounds = re.split(r'[\s]', data)
score = 0

for choice in range(0, len(rounds) - 1, 2):
    # Do I need to win, lose or draw
    outcome = worth_matrix.get(rounds[(choice + 1)])
    result = worth_matrix.get(outcome)

    # What did the other player pick and get it's number
    p1_choice = worth_matrix.get(rounds[choice])
    p2_choice = 0

    # Grab dictionary value that is a 2nd dictionary where the key value is the other players choice
    if outcome == "win":
        p2_choice = win_matrix["win"][p1_choice]
    elif outcome == "lose":
        p2_choice = win_matrix["lose"][p1_choice]
    else:
        p2_choice = win_matrix["draw"][p1_choice]
    score += (p2_choice + result)

print("I will score {} points".format(score))

