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