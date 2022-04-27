# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

def solution(numb):
    temp = list(map(sum, numb))
    i = 0

    for value in temp:
        print(f"Case #{i+1}: {numb[i][0]} + {numb[i][1]} = {value}")
        i+=1

t = int(input())

numb = []
for _ in range(t):
    numb.append(list(map(int, input().split())))

solution(numb)