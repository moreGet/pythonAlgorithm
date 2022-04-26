def solution(graph):
    a = graph[0]
    b = graph[1]

    num = list(map(int, str(b)))

    graph = []
    for i in num:
        graph.append(a*i)

    graph.reverse()
    result = a*b

    for i in range(0, len(graph)):
        print(graph[i])

    print(result)

graph = []
for i in range(2):
    graph.append(int(input()))

solution(graph)