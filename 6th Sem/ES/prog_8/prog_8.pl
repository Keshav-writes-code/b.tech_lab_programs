dist(1,2,10). dist(2,1,10).
dist(1,3,15). dist(3,1,15).
dist(1,4,20). dist(4,1,20).
dist(2,3,35). dist(3,2,35).
dist(2,4,25). dist(4,2,25).
dist(3,4,30). dist(4,3,30).

route_cost([_],0).
route_cost([A,B|T],C) :- dist(A,B,D), route_cost([B|T],R), C is D + R.

tsp(BestRoute, BestCost) :-
    permutation([2,3,4], P),
    Route = [1|P], append(Route,[1], FullRoute),
    route_cost(FullRoute, Cost),
    findall(C-R, (permutation([2,3,4], X), Rr=[1|X], append(Rr,[1], FR), route_cost(FR,C)), L),
    sort(L, [BestCost-BestRoute|_]).
