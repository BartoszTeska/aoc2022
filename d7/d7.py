from typing import List
from pathlib import Path


def getData(test: bool = False) -> List[str]:
    if test:
        return ["$ cd /",
                "$ ls",
                "dir a",
                "14848514 b.txt",
                "8504156 c.dat",
                "dir d",
                "$ cd a",
                "$ ls",
                "dir e",
                "29116 f",
                "2557 g",
                "62596 h.lst",
                "$ cd e",
                "$ ls",
                "584 i",
                "$ cd ..",
                "$ cd ..",
                "$ cd d",
                "$ ls",
                "4060174 j",
                "8033020 d.log",
                "5626152 d.ext",
                "7214296 k",]

    with open("inputD7.txt", 'r') as file:
        return [x.strip() for x in file.readlines()]


def parsePaths(arr: List[str]):
    path = Path("/")
    directories = {}
    for line in arr:
        command = line.split(" ")
        match command:
            case ["$", "cd", directoryName]:
                path = (path / directoryName).resolve()
            case [size, _]:
                if size.isdigit():
                    intSize = int(size)
                    for p in [path, *path.parents]:
                        if p not in directories.keys():
                            directories[p] = 0
                        directories[p] += intSize
    return directories


def solution(arr: List[str]) -> int:
    directories = parsePaths(arr)

    return sum([x for x in directories.values() if x <= 100_000])


def solution2(arr: List[str]) -> int:
    diskSize = 70_000_000
    required = 30_000_000
    directories = parsePaths(arr)
    return min([x for x in directories.values() if (directories[Path("/").resolve()] - x) <= diskSize-required])


if __name__ == "__main__":
    data = getData()
    print(solution(data))
    print(solution2(data))
