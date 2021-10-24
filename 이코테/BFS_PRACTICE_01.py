from collections import deque

# BFS 정의
def bfs(graph, start, visited):
    queue = deque([start]) # 큐 구현을 위해 deque 라이브러리 사용
    visited[start] = True # 방문처리

    while queue: # 큐 순회
        v = queue.popleft() # 노드를 왼쪽에서 추출
        print(v, end=' ') # 방문 노드 출력

        for i in graph[v]: # graph 의 v번째 노드와 인접한 노드들을 출력
            if not visited[i]: # 해당 노드를 방문하지 않았다면
                visited[i] = True # 해당 노드 방문처리
                queue.append(i) # 방문 하지 않은 노드를 큐에 삽입
                
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
bfs(graph, 1, visited)