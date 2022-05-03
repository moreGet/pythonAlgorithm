from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # 큐 선언
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

# 각 노드별 연결된 정보 리스트
# 1 2 3 8 7 4 5 6
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