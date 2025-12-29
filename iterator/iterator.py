# iterator.py
## イテレーターの抽象クラスを定義している
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Iterator(ABC, Generic[T]):

    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> T:
        pass
