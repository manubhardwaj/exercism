-module(bob).

-export([response/1, test_version/0]).

is_question([]) -> false;
is_question([H|[]]) -> H =:= $?;
is_question([_|T]) -> is_question(T).

is_blank([]) -> true;
is_blank(String) -> false.

is_yell([]) -> false;
is_yell(String) -> false.


response(String) when (is_question(String)) -> "Sure.";
response(String) when (is_yell(String)) -> "Whoa, chill out!";
response(String) when (is_blank(String)) -> "Fine. Be that way!";
response(String) -> "Whatever.".

test_version() -> 2.
