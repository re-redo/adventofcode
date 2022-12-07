from requests import get
from sys import argv, exit


# usage message
if len(argv) < 2:
    print("Usage:\t python3 elf_calories.py $SESSION_COOKIE")
    exit(1)

# get data
input_url = "https://adventofcode.com/2022/day/1/input"
cookies = {"session": argv[1]}
data = get(input_url, cookies=cookies).text

# split on blank lines as indicator between elves
elfs = data.split('\n\n')

# initialize count to track which elf has what
count = 0
calorie_list = []

# split on new line for calories per item and sum them
for elf in elfs:
   calories = elf.split('\n')
   calorie_total = 0
   for cal in calories:
      if len(cal) > 0:
         calorie_total += int(cal)
   calorie_list.append((count, calorie_total))
   count += 1

# sort by 2nd number in tuple (elf#, calories) 
calorie_list.sort(key=lambda a: a[1])

# chellange 1 - ID highest calorie count
print("Elf {} is carrying the most calories at {}".format(calorie_list[-1][0], calorie_list[-1][1]))
print("++++++++++++++++++++++++++++++++++++++++++++++")
# challenge 2 - What's the count of the top three
top_three = calorie_list[-2][1] + calorie_list[-3][1] + calorie_list[-1][1]
print("The highest three calories add up to: {}".format(top_three))