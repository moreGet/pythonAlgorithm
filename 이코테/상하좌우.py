# 지도 크기
mapSizeNM = int(input())
# 명령
orders = input().split()

# 기본 시작 좌표
x, y = 1, 1
# 이동 방향 x로 이동할때
dX = [0, 0, -1, 1]
# 이동 방향 y로 이동할때
dY = [-1, 1, 0, 0]
# 이동 명령 종류
moveTypes = ['L', 'R', 'U', 'D']

# 움직이기
for order in orders:
    for i in range(len(moveTypes)): # 배열을 전체 탐색
        if order == moveTypes[i]: # 명령과 동일한 요소 라면
            nX = x + dX[i] # X좌표 임시 가산
            nY = y + dY[i] # Y좌표 임시 가산

    if nX < 1 or nY < 1 or nX > mapSizeNM or nY > mapSizeNM: # 맵을 벗어나는 행위
        continue
    
    # 움직임
    x, y = nX, nY

print(x, y) # 정답 출력