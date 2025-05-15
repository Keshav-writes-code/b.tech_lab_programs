queens(Solution) :-
    Solution = [Q1, Q2, Q3, Q4],
    permutation([1, 2, 3, 4], Solution),
    safe(Solution).

safe([]).
safe([Q|Others]) :-
    safe(Q, Others, 1),
    safe(Others).

safe(_, [], _).
safe(Q, [Q1|Others], D) :-
    Q =\= Q1,                % not in same column
    abs(Q - Q1) =\= D,       % not in same diagonal
    D1 is D + 1,
    safe(Q, Others, D1).

permutation([], []).
permutation(List, [H|Perm]) :-
    select(H, List, Rest),
    permutation(Rest, Perm).
