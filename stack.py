from abc import ABC, abstractmethod


class Stack(ABC):

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def push(self, item: str) -> None:
        pass

    @abstractmethod
    def pop(self) -> str:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass

    @abstractmethod
    def peek(self) -> str:
        pass    