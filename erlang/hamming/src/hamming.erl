-module(hamming).

-export([distance/2, test_version/0]).


distance(Strand1, Strand2) -> distance(Strand1, Strand2, 0).

distance([],[],Distance) -> Distance;
distance(_,[],_) -> {error, "left and right strands must be of equal length"};
distance([],_,_) -> {error, "left and right strands must be of equal length"};
distance([H|T1],[H|T2],Distance) -> distance(T1, T2, Distance); 
distance([H1|T1],[H2|T2],Distance) -> distance(T1, T2, Distance + 1).


test_version() -> 2.
