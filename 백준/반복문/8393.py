# 1 ~ n 까지의 합

def solution(n):
    result = 0

    for i in range(1, n+1):
        result += i

    return result

n = int(input())
print(solution(n))