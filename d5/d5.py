import re
from collections import deque
from string import digits
from typing import Deque, List, Tuple


def getData(test: bool = False):
    filename = 'inputD5.txt'
    if test:
        filename = 'testInput.txt'

    with open(filename, 'r') as file:
        crates, rawMoves = file.read().split('\n\n')
        return crates, rawMoves


def parseMoves(arr: str) -> List[Tuple[int, int, int]]:
    return [tuple(map(int, re.findall(r"\d+", move)))
            for move in arr.splitlines()]


def parseCrates(arr: str) -> List[Deque[str]]:
    maxBuckets = max([int(x) for x in arr[len(arr)-1] if x != " "])
    buckets = [deque() for _ in range(maxBuckets)]

    for line in arr.splitlines():
        for id, i in enumerate(range(1, len(line), 4)):
            if line[i] != " " and line[i] not in digits:
                buckets[id].append(line[i])

    return buckets


def makeMove(buckets: List[Deque[str]], move: Tuple[int, int, int]) -> None:
    howMany, origin, destination = move

    for _ in range(howMany):
        buckets[destination-1].appendleft(buckets[origin-1].popleft())


def makeMove2(buckets: List[Deque[str]], move: Tuple[int, int, int]) -> None:
    howMany, origin, destination = move
    temp = []
    for _ in range(howMany):
        temp.append(buckets[origin-1].popleft())
    for item in reversed(temp):
        buckets[destination-1].appendleft(item)


def solution(crates: str, moves: str) -> str:
    buckets = parseCrates(crates)
    parsedMoves = parseMoves(moves)
    for move in parsedMoves:
        makeMove(buckets, move)

    return "".join(x[0] for x in buckets)


def solution2(crates: str, moves: str) -> str:
    buckets = parseCrates(crates)
    parsedMoves = parseMoves(moves)
    for move in parsedMoves:
        makeMove2(buckets, move)

    return "".join(x[0] for x in buckets)


if __name__ == "__main__":
    crates, moves = getData()
    print(solution(crates, moves))
    print(solution2(crates, moves))
