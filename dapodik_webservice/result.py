from collections import UserList
from dataclasses import dataclass, InitVar
from typing import Generic, List, TypeVar, Union

T = TypeVar("T")


@dataclass
class Result(Generic[T], UserList):
    result: int
    id: str
    start: int
    limit: int
    rows: InitVar[Union[List[T], T]]

    def __post_init__(self, rows: Union[List[T], T] = None) -> None:
        if not rows:
            self.data = []
        if isinstance(rows, list):
            self.data = rows
        else:
            self.data = [rows]
