from stack import Stack


class ArrayStack(Stack):

    def __init__(self) -> None:
        self._item: list[str] = []

    def is_empty(self) -> bool:
        return len(self._item) == 0

    def push(self, item: str) -> None:
        self._item.append(item)

    def pop(self) -> str:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._item.pop()

    def delete(self) -> None:
        if self.is_empty():
            raise IndexError("delete form empty stack")
        self._item.pop()

    def peek(self) -> str:
        if self.is_empty():
            raise IndexError("peek form empty stack")
        return self._item[-1]

    def print_stack(self) -> None:
        print(f"stack array {' '.join(self._item)}")