% The state is represented as (Jug1, Jug2) where Jug1 is the amount of water in the 3L jug, and Jug2 is the amount of water in the 5L jug.

% We will use the search strategy to find the sequence of actions to reach the goal.

% Base case: the goal state is reached.
solve(State, Goal, [State]) :-
    State = Goal.

% Recursive case 1: Fill Jug1 (3L jug).
solve((Jug1, Jug2), Goal, [(Jug1, Jug2) | Steps]) :-
    Jug1 < 3,
    NewJug1 is 3,
    solve((NewJug1, Jug2), Goal, Steps).

% Recursive case 2: Fill Jug2 (5L jug).
solve((Jug1, Jug2), Goal, [(Jug1, Jug2) | Steps]) :-
    Jug2 < 5,
    NewJug2 is 5,
    solve((Jug1, NewJug2), Goal, Steps).

% Recursive case 3: Empty Jug1 (3L jug).
solve((Jug1, Jug2), Goal, [(Jug1, Jug2) | Steps]) :-
    Jug1 > 0,
    NewJug1 is 0,
    solve((NewJug1, Jug2), Goal, Steps).

% Recursive case 4: Empty Jug2 (5L jug).
solve((Jug1, Jug2), Goal, [(Jug1, Jug2) | Steps]) :-
    Jug2 > 0,
    NewJug2 is 0,
    solve((Jug1, NewJug2), Goal, Steps).

% Recursive case 5: Pour water from Jug1 to Jug2.
solve((Jug1, Jug2), Goal, [(Jug1, Jug2) | Steps]) :-
    Jug1 > 0,
    Jug2 < 5,
    Transfer is min(Jug1, 5 - Jug2),
    NewJug1 is Jug1 - Transfer,
    NewJug2 is Jug2 + Transfer,
    solve((NewJug1, NewJug2), Goal, Steps).

% Recursive case 6: Pour water from Jug2 to Jug1.
solve((Jug1, Jug2), Goal, [(Jug1, Jug2) | Steps]) :-
    Jug2 > 0,
    Jug1 < 3,
    Transfer is min(Jug2, 3 - Jug1),
    NewJug1 is Jug1 + Transfer,
    NewJug2 is Jug2 - Transfer,
    solve((NewJug1, NewJug2), Goal, Steps).

% This predicate takes the initial state (0, 0) and tries to reach the Goal state.
find_solution(Goal, Steps) :-
    solve((0, 0), Goal, Steps).

