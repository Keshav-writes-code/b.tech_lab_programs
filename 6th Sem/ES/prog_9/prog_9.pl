% solve(+CapA, +CapB, +GoalA)
solve(CapA, CapB, GoalA) :-
    path(state(0, 0), [state(0, 0)], Path, CapA, CapB, GoalA),
    maplist(write_state, Path), nl.

% Moves
move(state(_, B), state(CapA, B), CapA, _) :- true.              % Fill A
move(state(A, _), state(A, CapB), _, CapB) :- true.              % Fill B
move(state(_, B), state(0, B), _, _) :- true.                    % Empty A
move(state(A, _), state(A, 0), _, _) :- true.                    % Empty B

move(state(A, B), state(NA, NB), CapA, CapB) :-                  % Pour A -> B
    T is min(A, CapB - B), T > 0,
    NA is A - T, NB is B + T.

move(state(A, B), state(NA, NB), CapA, CapB) :-                  % Pour B -> A
    T is min(B, CapA - A), T > 0,
    NB is B - T, NA is A + T.

% Pathfinding
path(S, _, [S], _, _, Goal) :- S = state(Goal, _).
path(S, Visited, [S|Path], CapA, CapB, Goal) :-
    move(S, Next, CapA, CapB),
    \+ member(Next, Visited),
    path(Next, [Next|Visited], Path, CapA, CapB, Goal).

write_state(state(A, B)) :- format("(~w,~w) ", [A, B]).
