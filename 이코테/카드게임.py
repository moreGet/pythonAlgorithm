## N과 M을 공백으로 구분하여 받는다.
n, m = map(int, input().split())

result = 0 ## 결과 값을 담을 변수

for i in range(n): ## 행 만큼 돌린다.
    data = list(map(int, input().split())) ## 한줄 을 먼저 받는다.

    minValue = min(data) ## 현재 행 중 가장 낮은 숫자가 뭔지 고른다.
    
    result = max(result, minValue) ## 해당 행들의 가장 낮은 값들 중에 가장 높은 값을 고른다.

## 문제의 규칙이 주어진 N * M 만큼의 숫자 카드 중 가장 높은 카드를 고르는 게임 이지만
## 규칙중 하나가 고를 행에서 가장 낮은 카드를 고르고 각 행 중 가장 높은 카드(가장 낮은 카드중)를 고르는 것이다.
## 따라서 고를 카드의 행중 가장 낮은 카드들을 비교했을때 가장 높은 카드를 뽑아야 하는 게임 이다.
print(result)