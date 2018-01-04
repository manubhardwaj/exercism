-module(space_age).

-export([ageOn/2, test_version/0]).

ageOn(Planet, Seconds) -> Seconds / year(Planet) / 31557600.

year(earth) -> 1.0;
year(mercury) -> 0.2408467;
year(venus) -> 0.61519726;
year(mars) -> 1.8808158;
year(jupiter) -> 11.862615;
year(saturn) -> 29.447498;
year(uranus) -> 84.016846;
year(neptune) -> 164.79132.

test_version() -> 1.
