% MYCIN-like diagnosis and treatment
symptom(john, fever).
symptom(john, chills).
symptom(john, high_white_cell_count).

diagnosis(P, bacterial_infection) :-
    symptom(P, fever), symptom(P, chills), symptom(P, high_white_cell_count).

treatment(bacterial_infection, penicillin).

recommend_treatment(P, T) :-
    diagnosis(P, D), treatment(D, T).

% SHRDLU-like blocks world
on(cube1, table). on(pyramid1, cube1). on(cube2, table).
color(cube1, red). color(pyramid1, blue). color(cube2, green).
shape(cube1, cube). shape(pyramid1, pyramid). shape(cube2, cube).

on_top_of(X, Y) :- on(X, Y).
movable(X) :- \+ on(_, X).
can_move(X, Y) :- movable(X), movable(Y), X \= Y.

describe(X) :-
    color(X, C), shape(X, S),
    format('~w is a ~w ~w.~n', [X, C, S]).
