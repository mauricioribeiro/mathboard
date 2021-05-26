from typing import Union


class Board:
    pass


class Number:
    value = 0

    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return str(self.value)


class Calculable(Number):
    __enable_history = True
    __history = []

    def __normalize(self, number):
        if not isinstance(number, self.__class__):
            number = Number(number)
        return number

    def __register(self, number: Number, operation: str):
        if self.__enable_history:
            self.__history.append(f'{self} {operation} {number}')

    def history(self):
        return self.__history

    def add(self, number: Union[Number, float, int]):
        number = self.__normalize(number)
        self.__register(number, '+')
        self.value += number.value
        return self

    def subtract(self, number: Union[Number, float, int]):
        number = self.__normalize(number)
        self.__register(number, '-')
        self.value -= number.value
        return self

    def __sub__(self, other):
        return self.subtract(other)

    def __add__(self, other):
        return self.add(other)


class Term(Calculable):
    name = None

    def __init__(self, name: str, value: float, enable_history: bool = True):
        self.name = name
        self.__enable_history = enable_history

        super().__init__(value)

    def __str__(self):
        return f'{self.name}: {self.value}'
