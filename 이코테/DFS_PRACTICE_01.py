## 깊이우선 탐색 (재귀 버전)
def dfs(graph, v, visited):
    visited[v] = True # 방문 확인
    print(str(v), end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited) # 재귀

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

dfs(graph, 1, visited)