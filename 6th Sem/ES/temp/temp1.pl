% Facts
parent(papa, me).
parent(dadu, papa).

% Rules
grandparent(X,Y) :- parent(X, Z), parent(Z, Y).
