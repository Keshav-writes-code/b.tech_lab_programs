
in(monkey,room).
hang(banana,ceiling).
walk(monkey,floor).
strong(monkey).
push(monkey,box):-strong(monkey).
under(box,banana).
climb(monkey,box).
can_reach(monkey,banana):-grasp(monkey,banana).
can_get(monkey,banana).
