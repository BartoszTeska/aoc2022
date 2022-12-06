def getData(test:bool=False)->str:
    if test:
        return "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

    with open('inputD6.txt') as file:
        return file.read()


def solution(command:str, markerLen:int)->int|None:
    for i in range(len(command)-markerLen):
        if len(set(command[i:i+markerLen]))==markerLen:
            return i+markerLen

if __name__=="__main__":
    data = getData()
    print(solution(data,4))
    print(solution(data,14))