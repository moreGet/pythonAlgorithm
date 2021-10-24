from itertools import permutations

def solution(numbers):
    answer = 0
    dicNumbers=[]

    for i in range(1, len(numbers)+1):
        dicNumbers.append(list(map(''.join, permutations(numbers, i)))) # 모든 경우의 수 조합

    # 리스트 를 리스트 형식으로 더하는 것은 모든 요소를 하나의 1차원 리스트로 변환 시켜줌
    dicNumbers = sum(dicNumbers, [])
    dicNumbers = list(set(map(int, dicNumbers))) # 중복 값을 전부 제거한 순수한 list로 변환
    
    for number in dicNumbers:
        if number == 2: # 2면 소수
            answer += 1

        for i in range(2, number):
            if number % i == 0:
                break # 소수라면 다음 숫자로 넘어감
            if i == number-1: # 만약 자기 자신 까지 왔으면 소수
                answer += 1
    return answer

if __name__ == '__main__':
    p = "17"
    print(solution(p))