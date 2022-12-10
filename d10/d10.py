from itertools import islice
from typing import Iterable, Iterator, List, Tuple
from functools import reduce
from operator import iconcat

ticks = [20, 60, 100, 140, 180, 220]


def getData(test: bool = False) -> List[List[str]]:
    filename = 'inputD10.txt'
    if test:
        filename = 'inputTestD10.txt'

    with open(filename, 'r') as file:
        return [x.strip().split(' ') for x in file.readlines()]


def execute(arr: List[List[str]]):
    state = [1]
    for instruction in arr:
        i = instruction[0]
        match i:
            case 'noop':
                state.append(state[-1])
            case 'addx':
                state.append(state[-1])
                state.append(state[-1]+int(instruction[1]))

    return state


def solution(arr: List[List[str]]) -> int:
    state = execute(arr)
    return sum([x * state[x-1] for x in ticks])


def solution2(arr: List[List[str]]) -> List[str]:
    screen = ['.']*240
    state = execute(arr)
    for id, value in enumerate(state):
        print(id, value)
        if id % 40 in [value-1, value, value+1]:
            screen[id] = '#'

    return screen


def chunk(arr: Iterable, size: int) -> Iterator[Tuple]:
    it = iter(arr)

    return iter(lambda: tuple(islice(it, size)), ())


def printScreen(screen: List[str]) -> None:
    screenLines = chunk(screen, 40)

    for line in screenLines:
        print(reduce(iconcat, line))


if __name__ == "__main__":
    data = getData()
    print(solution(data))
    printScreen(solution2(data))
