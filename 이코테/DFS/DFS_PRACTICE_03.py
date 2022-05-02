def dfs(graph, v, visited):
    visited[v] = True # 노드 방문 처리
    print(v, end=' ') # 방문 노드 출력

    for n in graph[v]:
        if visited[n] == False:
            dfs(graph, n, visited) # 재귀 반복

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

# 방문 여부 체크를 위한 1차원 LIST
visited = [False] * 9

# 정답 : 1 2 7 6 8 3 4 5 
# 깊이우선 탐색 수행
dfs(graph, 1, visited) # 연결된 노드, 시작 노드, 방문 정보