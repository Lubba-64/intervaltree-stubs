from typing import NamedTuple, Generic, TypeVar, Literal
from numbers import Real

T = TypeVar("T")
N = TypeVar("N", int, float, Real)

class IntervalBase(NamedTuple, Generic[N, T]):
    begin: N
    end: N
    data: T | None

class Interval(IntervalBase[N, T], Generic[N, T]):
    def __new__(cls, begin: N, end: N, data: T | None = None) -> Interval[N, T]: ...
    def overlaps(self, begin: N | Interval[N, T], end: N | None = None) -> bool: ...
    def overlap_size(self, begin: N | Interval[N, T], end: N | None = None) -> N: ...
    def contains_point(self, p: N) -> bool: ...
    def range_matches(self, other: Interval[N, T]) -> bool: ...
    def contains_interval(self, other: Interval[N, T]) -> bool: ...
    def distance_to(self, other: Interval[N, T]) -> N: ...
    def is_null(self) -> bool: ...
    def length(self) -> N: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Interval[N, T]) -> bool: ...
    def __cmp__(self, other: Interval[N, T]) -> Literal[-1, 1, 0]: ...
    def __lt__(self, other: Interval[N, T]) -> bool: ...
    def __gt__(self, other: Interval[N, T]) -> bool: ...
    def _raise_if_null(self, other: Interval[N, T]) -> bool: ...
    def lt(self, other: Interval[N, T]) -> bool: ...
    def le(self, other: Interval[N, T]) -> bool: ...
    def gt(self, other: Interval[N, T]) -> bool: ...
    def ge(self, other: Interval[N, T]) -> bool: ...
    def _get_fields(self) -> tuple[N, N, T] | tuple[N, N]: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def copy(self) -> Interval[N, T]: ...
    def __reduce__(self) -> tuple[Interval[N, T], tuple[N, N, T] | tuple[N, N]]: ...