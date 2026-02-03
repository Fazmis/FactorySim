from typing import Any
class Queue:
    """
    Очередь FIFO, для механики инвентаря
    (есть встроенное решение Python для реализации FIFO, но для обучения был выбран кастомный вариант)
    """
    def __init__(self) -> None:
        self.queue = list()

    def add(self, obj: object) -> None:
        self.queue.append(obj)

    def pop(self, i:int= 0) -> Any:
        return self.queue.pop(i)