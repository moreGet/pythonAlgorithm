from collections import deque

# 너비 우선 탐색
def bfs(graph, v, visited):
    visited[v] = True # 첫 노드 방문
    queue = deque([v]) # 큐 생성

    while queue: # 큐 순회
        v = queue.popleft()
        print(v, end=' ') # 방문 노드 출력

        for i in graph[v]: # bfs 순회
            if not visited[i]: # 방문 노드가 아닐때만 큐에 적재
                visited[i] = True # 방문 완료
                queue.append(i) # 해당 노드로 이어진 노드 방문을 위해 입력

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

# 방문 노드 입력 list
visited = [False] * 9

# 수행
bfs(graph, 1, visited)