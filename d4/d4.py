from typing import Tuple, List
from dataclasses import dataclass


@dataclass
class Section():
    x: int
    y: int


def getData(test: bool = False) -> List[List[Tuple[int, int]]]:
    if test:
        return [[(2, 4), (6, 8)],
                [(2, 3), (4, 5)],
                [(5, 7), (7, 9)],
                [(2, 8), (3, 7)],
                [(6, 6), (4, 6)],
                [(2, 6), (4, 8)],
                ]

    with open('inputD4.txt', 'r') as file:
        return [[tuple(map(lambda z: int(z), y.strip().split('-'))) for y in x.strip().split(',')] for x in file.readlines()]


def isRangeContained(arr: List[Tuple[int, int]]) -> bool:
    elf1 = Section(arr[0][0], arr[0][1])
    elf2 = Section(arr[1][0], arr[1][1])

    return elf1.x <= elf2.x and elf1.y >= elf2.y or elf2.x <= elf1.x and elf2.y >= elf1.y


def isRangeOverlapping(arr: List[Tuple[int, int]]) -> bool:
    elf1 = Section(arr[0][0], arr[0][1])
    elf2 = Section(arr[1][0], arr[1][1])

    return max(elf2.y, elf1.y) - min(elf2.x, elf1.x) <= (elf1.y-elf1.x)+(elf2.y-elf2.x)


def solution(arr: List[List[Tuple[int, int]]]) -> int:
    return sum(map(lambda x: isRangeContained(x), arr))


def solution2(arr: List[List[Tuple[int, int]]]) -> int:
    return sum(map(lambda x: isRangeOverlapping(x), arr))


if __name__ == '__main__':
    data = getData()

    print(solution(data))
    print(solution2(data))
