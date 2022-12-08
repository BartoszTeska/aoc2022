from math import prod
from typing import Any, List
from functools import reduce
from operator import iconcat


def getData(test: bool = False) -> List[List[int]]:
    if test:
        return [[3, 0, 3, 7, 3],
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5, 3, 9, 0]]

    with open('inputD8.txt', 'r') as file:
        return [list(map(int, x.strip())) for x in file.readlines()]


def isTreeVisible(x: int, y: int, forest: List[List[int]]) -> bool:
    row = forest[x]
    col = [row[y] for row in forest]
    tree = forest[x][y]

    if x in [0, len(row)-1] or y in [0, len(col)-1]:
        return True

    rowLeft = row[:y]
    rowRight = row[y+1:]
    colUp = col[:x]
    colDown = col[x+1:]

    return all(map(lambda other: other < tree, rowRight)) or all(map(lambda other: other < tree, rowLeft)) or all(map(lambda other: other < tree, colUp)) or all(map(lambda other: other < tree, colDown))


def getScore(tree: int, way: List[int]) -> int:
    result = []
    for treeInWay in way:
        if treeInWay < tree:
            result.append(treeInWay)
        if treeInWay >= tree:
            result.append(treeInWay)
            break
    return len(result)


def getScenicScore(x: int, y: int, forest: List[List[int]]) -> int:
    row = forest[x]
    col = [row[y] for row in forest]
    tree = forest[x][y]
    rowLeft = row[:y]
    rowRight = row[y+1:]
    colUp = col[:x]
    colDown = col[x+1:]
    ways = [rowLeft[::-1], rowRight, colUp[::-1], colDown]
    return prod([x if x > 0 else 0 for x in [getScore(tree, way) for way in ways]])


def flatten(arr: List[List[Any]]) -> List[Any]:
    return reduce(iconcat, arr, [])


def solution(arr: List[List[int]]) -> int:
    result = []
    for i in range(len(arr)):
        resultRow = []
        for j in range(len(arr[i])):
            resultRow.append(isTreeVisible(i, j, arr))
        result.append(resultRow)

    return sum(flatten(result))


def solution2(arr: List[List[int]]) -> int:
    result = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            result.append(getScenicScore(i, j, arr))

    return max(result)


if __name__ == "__main__":
    data = getData()
    print(solution(data))
    print(solution2(data))
