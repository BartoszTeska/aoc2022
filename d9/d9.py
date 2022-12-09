from typing import List, Tuple


class RopeHead():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def move(self, direction: str) -> None:
        match direction:
            case 'U':
                self.y += 1
            case 'D':
                self.y -= 1
            case 'R':
                self.x += 1
            case 'L':
                self.x -= 1
            case _:
                pass

    def position(self) -> Tuple[int, int]:
        return (self.x, self.y)


class RopeTail(RopeHead):
    moveSetVert = {
        1: 'U',
        -1: "D"
    }
    moveSetHor = {
        1: 'R',
        -1: "L"
    }

    def __init__(self) -> None:
        super().__init__()

    def chaseHead(self, headPosition: Tuple[int, int]) -> None:
        tailPosition = self.position()
        if (tailPosition[0] == headPosition[0] and tailPosition[1] == headPosition[1]) or (abs(headPosition[0]-tailPosition[0]) <= 1 and abs(headPosition[1]-tailPosition[1]) <= 1):
            return
        if tailPosition[0] == headPosition[0] and abs(headPosition[1]-tailPosition[1]) == 2:
            moveCode = 1 if headPosition[1]-tailPosition[1] > 0 else -1
            self.move(self.moveSetVert[moveCode])
            return
        if tailPosition[1] == headPosition[1] and abs(headPosition[0]-tailPosition[0]) == 2:
            moveCode = 1 if headPosition[0]-tailPosition[0] > 0 else -1
            self.move(self.moveSetHor[moveCode])
            return
        xDistance = 1 if headPosition[0]-tailPosition[0] > 0 else -1
        ydistance = 1 if headPosition[1]-tailPosition[1] > 0 else -1
        self.move(self.moveSetHor[xDistance])
        self.move(self.moveSetVert[ydistance])
        return


def getData(test: bool = False, testNo: int = 0) -> List[Tuple[str, int]]:
    if test and testNo == 0:
        return [
            ('R', 4),
            ('U', 4),
            ('L', 3),
            ('D', 1),
            ('R', 4),
            ('D', 1),
            ('L', 5),
            ('R', 2),
        ]

    if test and testNo == 1:
        return [
            ('R', 5),
            ('U', 8),
            ('L', 8),
            ('D', 3),
            ('R', 17),
            ('D', 10),
            ('L', 25),
            ('U', 20),
        ]

    def parseLine(line: str):
        direction, steps = line.strip().split(' ')

        return (direction, int(steps))

    with open('inputD9.txt', 'r') as file:
        return [parseLine(x) for x in file.readlines()]


def solution(moves: List[Tuple[str, int]]) -> int:
    tailMoves = set()
    head = RopeHead()
    tail = RopeTail()
    for move in moves:
        for _ in range(move[1]):
            head.move(move[0])
            tail.chaseHead(head.position())
            tailMoves.add(tail.position())
    return len(tailMoves)


def solution2(moves: List[Tuple[str, int]]) -> int:
    tailMoves = set()
    head = RopeHead()
    tails = [RopeTail() for x in range(9)]
    for move in moves:
        for _ in range(move[1]):
            head.move(move[0])
            tails[0].chaseHead(head.position())
            for i, tail in enumerate(tails[1:]):
                tail.chaseHead(tails[i].position())
            tailMoves.add(tails[-1].position())
    return len(tailMoves)


if __name__ == "__main__":
    data = getData()
    print(solution(data))
    print(solution2(data))
