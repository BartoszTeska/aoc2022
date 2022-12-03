from typing import List
from itertools import groupby


def getData(test: bool = False) -> List[List[int]]:
    if test:
        return [[1000, 2000, 3000], [4000],
                [5000, 6000], [7000, 8000, 9000], [10000]]

    with open('dataD1.txt', 'r') as file:
        return [list(map(lambda x: int(x.strip()), group)) for key, group in groupby(file, lambda x: x == '\n') if not key]


def solution(arr: List[List[int]]) -> int:
    return max(map(lambda x: sum(x), arr))


def solution2(arr: List[List[int]], n: int = 3) -> int:
    return sum(sorted(map(lambda x: sum(x), arr), reverse=True)[:n])


if __name__ == "__main__":
    data = getData()

    print(solution(data))
    print(solution2(data))
