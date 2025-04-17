
% Predicate to start the game with initial state and the first move
start(X, Y) :-
    write('Initial State: '), write(X), write(' liters in the 5-liter jug, '),
    write(Y), write(' liters in the 3-liter jug'), nl,
    prompt_move(X, Y, 1).

% Predicate to prompt the user for the next move
prompt_move(X, Y, N) :-
    write('Move '), write(N), write(': Choose an action: '), nl,
    write('1. Fill the 5-liter jug'), nl,
    write('2. Fill the 3-liter jug'), nl,
    write('3. Empty the 5-liter jug'), nl,
    write('4. Empty the 3-liter jug'), nl,
    write('5. Pour from 5-liter jug to 3-liter jug'), nl,
    write('6. Pour from 3-liter jug to 5-liter jug'), nl,
    read(Move),
    contains_by_3(X, Y, Move, N).

% Predicate to apply a move and update the state
contains_by_3(X, Y, 1, N) :-
    NewX is 5, % Fill the 5-liter jug
    write('After Move '), write(N), write(': '), 
    write(NewX), write(' liters in the 5-liter jug, '),
    write(Y), write(' liters in the 3-liter jug'), nl,
    (NewX == 4 -> write('Congratulations! Goal state reached: 4 liters in the 5-liter jug.'), nl; prompt_move(NewX, Y, N+1)).

contains_by_3(X, Y, 2, N) :-
    NewY is 3, % Fill the 3-liter jug
    write('After Move '), write(N), write(': '), 
    write(X), write(' liters in the 5-liter jug, '),
    write(NewY), write(' liters in the 3-liter jug'), nl,
    prompt_move(X, NewY, N+1).

contains_by_3(X, Y, 3, N) :-
    NewX is 0, % Empty the 5-liter jug
    write('After Move '), write(N), write(': '), 
    write(NewX), write(' liters in the 5-liter jug, '),
    write(Y), write(' liters in the 3-liter jug'), nl,
    prompt_move(NewX, Y, N+1).

contains_by_3(X, Y, 4, N) :-
    NewY is 0, % Empty the 3-liter jug
    write('After Move '), write(N), write(': '), 
    write(X), write(' liters in the 5-liter jug, '),
    write(NewY), write(' liters in the 3-liter jug'), nl,
    prompt_move(X, NewY, N+1).

contains_by_3(X, Y, 5, N) :-
    Transfer is min(X, 3 - Y), % Pour from the 5-liter jug to the 3-liter jug
    NewX is X - Transfer,
    NewY is Y + Transfer,
    write('After Move '), write(N), write(': '), 
    write(NewX), write(' liters in the 5-liter jug, '),
    write(NewY), write(' liters in the 3-liter jug'), nl,
    prompt_move(NewX, NewY, N+1).

contains_by_3(X, Y, 6, N) :-
    Transfer is min(Y, 5 - X), % Pour from the 3-liter jug to the 5-liter jug
    NewX is X + Transfer,
    NewY is Y - Transfer,
    write('After Move '), write(N), write(': '), 
    write(NewX), write(' liters in the 5-liter jug, '),
    write(NewY), write(' liters in the 3-liter jug'), nl,
    prompt_move(NewX, NewY, N+1).
