from collections import deque

# 솔루션 구현
def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v]) # 큐 생성

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]: # 방문 노드가 아니라면
                visited[i] = True # 노드 방문 확인
                queue.append(i) # 다음 노드 방문을 위해 방문한 노드 큐에 삽입


# 각 노드별 연결된 정보 리스트
graph = [
    [],
    [2, 3, 8], # 1번 노드
    [1, 7], # 2번 노드
    [1, 4, 5], # 3번 노드
    [3, 5], # 4번 노드
    [3, 4], # 5번 노드
    [7], # 6번 노드
    [2, 6, 8], # 7번 노드
    [1, 7] # 8번 노드
]

visited = [False] * 9

bfs(graph, 1, visited)