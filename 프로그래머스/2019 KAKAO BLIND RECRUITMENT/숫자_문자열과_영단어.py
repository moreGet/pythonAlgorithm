import re

def solution(s):
    numMap={
        'zero':'0',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    
    for key in numMap.keys():
        # s = s.replace(key, numMap[key])
        s = re.sub(key, numMap[key], s)

    return int(s)

if __name__ == '__main__':
    s='one4seveneight'
    # solution(s)
    print(solution(s))