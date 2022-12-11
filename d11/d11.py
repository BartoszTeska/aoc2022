from collections import deque
from math import prod
from typing import Callable, List
import re
import sys

sys.set_int_max_str_digits(4500)


class Monkey:
    def __init__(self, number: int, items: List[int], operation: Callable, treshold: int, testTrue: int, testFalse: int) -> None:
        self.number = number
        self.items = deque(items)
        self.operation = operation
        self.testTrue = testTrue
        self.testFalse = testFalse
        self.testTreshold = treshold
        self.inspections = 0
        self.worryDivide = 3

    def setMonkeys(self, monkeys):
        self.monkeys = monkeys

    def inspectItem(self):
        if len(self.items) <= 0:
            return

        while len(self.items) > 0:
            item = self.operation(self.items.popleft())//self.worryDivide
            throwTarget = self.testTrue if item % self.testTreshold == 0 else self.testFalse
            self.inspections += 1

            self.throwItem(item, throwTarget)

    def addItem(self, item: int):
        self.items.append(item)

    def throwItem(self, item: int, monkeyNumber: int):
        [x for x in self.monkeys if x.number == monkeyNumber][0].addItem(item)

    def setAllDiv(self, allDiv: int):
        self.allDiv = allDiv


class LongMonkey(Monkey):
    def __init__(self, number: int, items: List[int], operation: Callable, treshold: int, testTrue: int, testFalse: int) -> None:
        super().__init__(number, items, operation, treshold, testTrue, testFalse)

    def inspectItem(self):
        if len(self.items) <= 0:
            return

        while len(self.items) > 0:
            item = self.operation(self.items.popleft())
            throwTarget = self.testTrue if item % self.testTreshold == 0 else self.testFalse
            self.inspections += 1
            item = item % self.allDiv
            self.throwItem(item, throwTarget)


def mod(a, b):
    r = 0
    stra = str(a)
    for i in range(0, len(stra)):
        r = (r*10)+int(stra[i]) % b

    return r


def getData(test: bool = False):
    filename = 'inputTestD11.txt' if test else 'inputD11.txt'

    with open(filename, 'r') as file:
        return [x for x in file.read().split('\n\n')]


def parseMonkey(monkey: str, long: bool = False) -> Monkey:
    m = monkey.split('\n')
    monkeyNumber = getNumber(m[0])
    items = getMonkeyItems(m[1])
    operation = getOperation(m[2])
    testingValue = getNumber(m[3])
    true = getNumber(m[4])
    false = getNumber(m[5])

    return Monkey(monkeyNumber, items, operation, testingValue, true, false) if not long else LongMonkey(monkeyNumber, items, operation, testingValue, true, false)


def getMonkeyItems(items: str):
    pattern = r'\d+'
    itemsFound = re.findall(pattern, items)

    return list(map(int, itemsFound))


def getOperation(operation: str):
    pattern1 = r'(?:=).+'
    op = re.findall(pattern1, operation)[0][1:]
    return lambda old: eval(op)


def getNumber(line: str):
    pattern = r'\d+'
    return int(re.findall(pattern, line)[0])


def solution(arr: List[str]):
    monkeys = [parseMonkey(x) for x in arr]
    for monkey in monkeys:
        monkey.setMonkeys(monkeys)

    for _ in range(20):
        for monkey in monkeys:
            monkey.inspectItem()

    return prod(sorted([x.inspections for x in monkeys])[-2:])


def solution2(arr: List[str]):
    monkeys = [parseMonkey(x, True) for x in arr]
    allDiv = prod([x.testTreshold for x in monkeys])
    for monkey in monkeys:
        monkey.setMonkeys(monkeys)
        monkey.setAllDiv(allDiv)

    for _ in range(10_000):
        for monkey in monkeys:
            monkey.inspectItem()

    return prod(sorted([x.inspections for x in monkeys])[-2:])


if __name__ == "__main__":
    data = getData()
    print(solution(data))
    print(solution2(data))
