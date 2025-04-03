
% Facts
parent(john, mary).
parent(mary, alice).
parent(alice, bob).

% Rules
ancestor(X, Y) :- parent(X, Y).   % Base case: A parent is an ancestor.
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y). % Recursive case: If X is parent of Z, and Z is ancestor of Y, then X is ancestor of Y.

% Query
?- ancestor(alice, bob).  % True
?- ancestor(john, bob).   % True
?- ancestor(mary, bob).   % True
