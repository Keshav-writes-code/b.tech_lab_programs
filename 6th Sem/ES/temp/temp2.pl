% Knowledge Base: Family relationships
parent(john, bob).
parent(john, lisa).
parent(mary, bob).
parent(mary, lisa).
parent(bob, ann).
parent(bob, james).
parent(lisa, carol).
parent(lisa, thomas).

male(john).
male(bob).
male(james).
male(thomas).
female(mary).
female(lisa).
female(ann).
female(carol).

% Rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
child(X, Y) :- parent(Y, X).
son(X, Y) :- child(X, Y), male(X).
daughter(X, Y) :- child(X, Y), female(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
grandfather(X, Z) :- grandparent(X, Z), male(X).
grandmother(X, Z) :- grandparent(X, Z), female(X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y) :- sibling(X, Y), female(X).

% Natural language query processor
answer(Question, Answer) :-
    process_question(Question, Relation, Person, Answer).

process_question(Question, Relation, Person, Answer) :-
    identify_relation(Question, Relation),
    identify_person(Question, Person),
    find_answer(Relation, Person, Answers),
    format_answer(Relation, Person, Answers, Answer).

% Extract relation from question
identify_relation(Question, father) :- 
    sub_string(Question, _, _, _, "father"), !.
identify_relation(Question, mother) :- 
    sub_string(Question, _, _, _, "mother"), !.
identify_relation(Question, son) :- 
    sub_string(Question, _, _, _, "son"), !.
identify_relation(Question, daughter) :- 
    sub_string(Question, _, _, _, "daughter"), !.
identify_relation(Question, children) :- 
    sub_string(Question, _, _, _, "children"), !.
identify_relation(Question, grandparent) :- 
    sub_string(Question, _, _, _, "grandparent"), !.
identify_relation(Question, grandfather) :- 
    sub_string(Question, _, _, _, "grandfather"), !.
identify_relation(Question, grandmother) :- 
    sub_string(Question, _, _, _, "grandmother"), !.
identify_relation(Question, sibling) :- 
    sub_string(Question, _, _, _, "sibling"), !.
identify_relation(Question, brother) :- 
    sub_string(Question, _, _, _, "brother"), !.
identify_relation(Question, sister) :- 
    sub_string(Question, _, _, _, "sister"), !.

% Extract person from question
identify_person(Question, Person) :-
    member(Person, [john, mary, bob, lisa, ann, james, carol, thomas]),
    sub_string(Question, _, _, _, Person).

% Find answers for the relation
find_answer(father, Person, Answers) :-
    findall(X, father(X, Person), Answers).
find_answer(mother, Person, Answers) :-
    findall(X, mother(X, Person), Answers).
find_answer(son, Person, Answers) :-
    findall(X, son(X, Person), Answers).
find_answer(daughter, Person, Answers) :-
    findall(X, daughter(X, Person), Answers).
find_answer(children, Person, Answers) :-
    findall(X, child(X, Person), Answers).
find_answer(grandparent, Person, Answers) :-
    findall(X, grandparent(X, Person), Answers).
find_answer(grandfather, Person, Answers) :-
    findall(X, grandfather(X, Person), Answers).
find_answer(grandmother, Person, Answers) :-
    findall(X, grandmother(X, Person), Answers).
find_answer(sibling, Person, Answers) :-
    findall(X, sibling(X, Person), Answers).
find_answer(brother, Person, Answers) :-
    findall(X, brother(X, Person), Answers).
find_answer(sister, Person, Answers) :-
    findall(X, sister(X, Person), Answers).

% Format the answer
format_answer(_, _, [], "I don't know.").
format_answer(Relation, Person, Answers, Answer) :-
    Answers \= [],
    list_to_string(Answers, AnswerStr),
    format(string(Answer), "The ~w of ~w is ~w.", [Relation, Person, AnswerStr]).

% Helper to convert list to string
list_to_string([X], X) :- !.
list_to_string([X,Y], Answer) :-
    format(string(Answer), "~w and ~w", [X, Y]), !.
list_to_string([H|T], Answer) :-
    list_to_string(T, TailStr),
    format(string(Answer), "~w, ~w", [H, TailStr]).

% Example queries
% ?- answer("Who is the father of bob?", A).
% ?- answer("Who are the children of lisa?", A).
% ?- answer("Who is the grandmother of carol?", A).
