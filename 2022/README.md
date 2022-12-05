### Day 1
*Scenario:* The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line. See below. 
```
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
```
*Challenge 1:* Find which elf is carrying the most calories.


*Challenge 2:* What is the sum of the three greatest quantities. 

### Day 2
*Scenario:* Score rock-paper-scissors. Your opponent plays `A` rock, `B` scissors, or `C` paper and you play the same with `XYZ` respectively. The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)

Example input
```
A Y
B X
C Z
```
*Challenge 1:* What is the total number of points I would have? The example adds to 15.

*Scenario Revised:* The second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

*Challenge 2:* What is the total number of points I would have? The example evaluates to 12.

### Day 3
*Scenario:* There is a story but the plain of it is, find the letter shared between the two inputs. The inputs are the same length concatenated on the same line. The letters have numeric value -  Lowercase item types a through z have priorities 1 through 26. Uppercase item types A through Z have priorities 27 through 52.

Example input
```
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
```
*Challenge 1:* What is the sum of each of the shared letters. In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

*Scenario Revised:* Now each elf in a group of 3 (three lines) has one letter that's the same. 

*Challenge 2:* Sum the common letter in the groups of 3. Per this example In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, their badge item type must be Z.
Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

### Day 4
*Scenario:* On each new line two elves (separated by `,`), recieves an area they are responsible for cleaning.

Example input
```
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
```
*Challenge 1:* Find the number of lines where one of the cleaning sections is fully encompassed by their partner's section. The example results in answer of 2. 

*Challenge 2:* Find the number of lines where there is any overlap in sections.. The example results in answer of 4. 

### Day 5
*Scenario:* 

Example input
```

```
*Challenge 1:* 

*Scenario Revised:* 

*Challenge 2:* 