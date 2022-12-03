from typing import List, Iterable, Tuple, Iterator
from string import ascii_letters
from itertools import islice


def getData(test: bool = False) -> List[str]:
    if test:
        return [
            'vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw',
        ]

    with open('inputD3.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]


def parseLine(line: str) -> str:
    middle = len(line)//2
    lineA = line[:middle]
    lineB = line[middle:]

    return set(lineA).intersection(set(lineB)).pop()


def getPriority(item: str) -> int:
    alphabet = list(ascii_letters)

    return alphabet.index(item)+1


def chunk(arr: Iterable, size: int) -> Iterator[Tuple]:
    it = iter(arr)
    return iter(lambda: tuple(islice(it, size)), ())


def parseGroup(arr: List[Tuple[str]]) -> str:
    char = set.intersection(*[set(x) for x in arr]).pop()

    return char


def solution(arr: List[str]) -> int:
    intersectedChars = list(map(lambda x: parseLine(x), arr))

    return sum(map(lambda x: getPriority(x), intersectedChars))


def solution2(arr: List[str]) -> int:
    groupedLines = list(chunk(arr, 3))
    intersectedChars = list(map(lambda x: parseGroup(x), groupedLines))

    return sum(map(lambda x: getPriority(x), intersectedChars))


if __name__ == "__main__":
    data = getData()

    print(solution(data))
    print(solution2(data))
