from collections import deque
from typing import Deque # 큐 구현을 위한 lib 참조

# BFS 정의
def bfs(graph, start, visited):
    queue = deque([start]) # 큐 구현
    visited[start] = True # 방문 완료

    while queue: # 큐 순회
        v = queue.popleft() # 노드 꺼내기
        print(v, end=' ') # 방문된 노드 출력

        for i in graph[v]:
            if not visited[i]: # 방문된 노드가 아니라면
                visited[i]=True # 방문처리 하고
                queue.append(i) # 방문된 노드 큐에 삽입

# 각 노드별 연결된 정보 리스트
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited) # bfs 수행