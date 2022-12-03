from typing import List, Tuple
from enum import Enum

PlayerOptions = Enum('PlayerOptions', ['X', 'Y', 'Z'])
OpponentOptions = Enum('OpponentOptions', ['A', 'B', 'C'])

Weights = {
    ('A', 'X'): 0,
    ('B', 'Y'): -1,
    ('C', 'Z'): 1

}


def getData(test: bool = False) -> List[Tuple[str, str]]:
    if test:
        return [('A', 'Y'),
                ('B', 'X'),
                ('C', 'Z')]

    with open('inputD2.txt', 'r') as file:
        return [tuple(line.strip().split(' ')) for line in file.readlines()]


def getWeight(hand: 'str') -> int:
    return next(v for k, v in Weights.items() if hand in k)


def rockPaperScissors(opponent: str, you: str) -> int:
    opponentWeight = getWeight(opponent)
    yourWeight = getWeight(you)
    winningHand = 2

    if opponentWeight != yourWeight:
        if abs(opponentWeight) == abs(yourWeight):
            winningHand = max([opponentWeight, yourWeight])
        else:
            winningHand = min([opponentWeight, yourWeight])

    if winningHand == 2:
        return PlayerOptions[you].value+3

    if (winningHand == opponentWeight):
        return PlayerOptions[you].value

    return PlayerOptions[you].value+6


def getMove(opponent: str, outcome: str) -> Tuple[str, str]:
    match outcome:
        case 'X':
            for v, key in enumerate(PlayerOptions):
                if (OpponentOptions[opponent].value) % 3 != (v) and v != OpponentOptions[opponent].value-1:
                    return (opponent, key.name)
        case 'Y':
            for v, key in enumerate(PlayerOptions):
                if OpponentOptions[opponent].value-1 == v:
                    return (opponent, key.name)
        case 'Z':
            for v, key in enumerate(PlayerOptions):
                if (OpponentOptions[opponent].value) % 3 == (v):
                    return (opponent, key.name)
        case _:
            raise ValueError('wrong outcome')


def solution(arr: List[Tuple[str, str]]) -> int:
    return sum(map(lambda x: rockPaperScissors(x[0], x[1]), arr))


def solution2(arr: List[Tuple[str, str]]) -> int:
    moves = map(lambda x: getMove(x[0], x[1]), arr)
    return sum(map(lambda x: rockPaperScissors(x[0], x[1]), moves))


if __name__ == "__main__":
    data = getData()

    print(solution(data))
    print(solution2(data))
