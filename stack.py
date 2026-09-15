from abc import ABC, abstractmethod


class Stack(ABC):

    @abstractmethod
    def is_empty(self) -> bool:
        """스택 비었는지 여부 확인"""
        pass

    @abstractmethod
    def push(self, item:str) -> None:
        """스택 top에 원소 넣기"""
        pass

    @abstractmethod
    def pop(self) -> str:
        """스택 top에서 원소 빼고 데이터 리턴"""
        pass

    @abstractmethod
    def delete(self) -> None:
        pass

    @abstractmethod
    def peek(self) -> str:
        """스택 top에서 빼지않고 확인"""
        pass