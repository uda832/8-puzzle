# 8-puzzle
Author: Oyun-Undrakh Yeruultsengel
8-Puzzle
02/24/2018

## To run:
- Provide the input file (see section Sample Input for reference)
- Run using python3
```
python3 8puzzle.py
```


## Input Format
The first 3 lines should each contain 3 space separeted integers that represent the START state of the 8 puzzle game.
Separated by an empty line, another 3 lines should each contain 3 space separated integers that represent the GOAL state of the game.

## Sample Input:
```
3 6 4 
0 1 2 
8 7 5

1 2 3 
8 0 4
7 6 5
```


## Sample Output:
```
Start state:
[3, 6, 4]
[0, 1, 2]
[8, 7, 5]

Goal state:
[1, 2, 3]
[8, 0, 4]
[7, 6, 5]

Solution: The shortest path cost is: 43
```
