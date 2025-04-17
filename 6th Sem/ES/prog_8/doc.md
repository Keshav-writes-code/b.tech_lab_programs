# Program 8
write a program in prolog to solve the water jug Problem

## 

- each rule corresponding to a predicate name contains by three which takes the current state of the jugs (x & y) representing the water levels in the 5 litre and 3 litre jug respectively and the move number, n as arguments
- the contains by 3 predicate terminates the new set of jugs after applying the selected move and call the start by to predicate with the new state

## Goal State
- Goal state is achieved when there is 4 litre water in the 5 litre jug
- start(_, 4)
- upon reaching the goal state, the program displays a congratulatory message

## Main predicate
- Made by 0 predicate initialize the game by displaying the initial state and prompting the user to enter a move
- it then pause contains by 3 predicate with the initial state and choosen move
