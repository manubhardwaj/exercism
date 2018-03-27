-module(pangram).

-export([is_pangram/1, test_version/0]).

is_pangram([H | T]) when H =:= $  -> is_pangram(T);
is_pangram(Sentence) -> is_isogram(Sentence).

is_isogram(String) -> is_isogram(string:to_lower(String), sets:new()).

is_isogram([], _) -> true;
is_isogram([H | T], Set) when H =:= $- orelse H =:= $  -> is_isogram(T, Set);
is_isogram([H | T], Set) ->
  case sets:is_element(H, Set) of
    true -> false;
    _ -> is_isogram(T, sets:add_element(H, Set))
  end.



test_version() -> 1.
