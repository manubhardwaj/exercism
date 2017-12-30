-module(rna_transcription).

-export([to_rna/1, test_version/0]).

f(N) when (N == $G) -> $C;
f(N) when (N == $C) -> $G;
f(N) when (N == $T) -> $A;
f(N) when (N == $A) -> $U;
f(N) -> {error}.

to_rna([H|T]) -> [f(H) | to_rna(T)];
to_rna([]) -> [].

test_version() -> 2.
