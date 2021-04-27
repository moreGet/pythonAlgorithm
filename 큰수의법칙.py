# 주어진 N개의 배열요소를 M번만큼 더해 가장 큰 수를 만든다, 단, 같은 인덱스의 수는 K번 만큼만 더할수 있음
# N 개의 배열 요소, M번만큼 더하고, K번 만큼 같은 INDEX를 더할 수 있음

# N, M, K 를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수를 정렬하기
first = data[n-1] # 첫번째로 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0

while True:
    for i in range(k): # k번만큼 더하기
        if(m == 0): # m번만큼만 더한다
            break # Loop 탈출

        result += first # 제일 큰 수를 누계
        m -= 1 # m번만큼만 더해야 하기때문에 기회를 줄임
    
    if(m == 0): # 다 더해지면 반복문 종료
        break

    result += second # 첫번째로 큰 수를 k번만큼 더했으니 두번째로 큰 수를 더함
    m -= 1 # 이 역시 m번만큼만 더해야 하기 때문에 기회를 줄임
    
print(result)#

# 위 알고리즘은 M <= 10,000 이므로 시간 초과 문제가 발생하지 않는다 다만, 100억 이상 커진다면 시간초과 판정을 받는다
## 따라서 개선 해보자