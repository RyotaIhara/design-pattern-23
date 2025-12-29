# print.py
## Printの抽象クラスを定義している
from abc import ABC, abstractmethod


class Print(ABC):

    @abstractmethod
    def print_weak(self) -> str:
        pass

    @abstractmethod
    def print_strong(self) -> str:
        pass
