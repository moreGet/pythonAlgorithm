## 깊이우선 탐색 (재귀 버전)
def dfs(graph, v, visited):
    visited[v]=True # 방문 완료
    print(v, end=' ') # 방문 노드 출력

    for i in graph[v]: # 노드 깊이우선 탐색으로 방문
        if not visited[i]: # 현재 노드가 방문 지역이 아니면
            dfs(graph, i, visited) # 현재 노드와 방문 정보를 가지고 재탐색

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

# 깊이우선 탐색 수행
dfs(graph, 1, visited) # 연결된 노드, 시작 노드, 방문 정보