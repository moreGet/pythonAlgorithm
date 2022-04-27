# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

def solution(numb):
    numb = list(map(sum, numb))
    i = 0

    for value in numb:
        i+=1
        print(f"Case #{i}: {value}")

t = int(input())

numb = []
for _ in range(t):
    numb.append(list(map(int, input().split())))

solution(numb)