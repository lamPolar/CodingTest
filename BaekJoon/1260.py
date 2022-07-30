import sys

def DFS(graph, V, check):
    if (check[V] == 1):
        return
    graph[0].append(V)
    check[V] = 1
    for i in graph[V]:
        DFS(graph, i, check)


def BFS(graph, V, check):
    queue = []
    queue.append(V)
    while (len(queue)):
        node = queue.pop(0)
        if (check[node] == 0):
            while (len(graph[node])):
                i = graph[node].pop(0)
                if (check[i] == 0):
                    queue.append(i)
            check[node] = 1
            graph[0].append(node)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
check = [0 for _ in range(N + 1)]
for _ in range(M):
    elem1, elem2 = map(int, sys.stdin.readline().split())
    graph[elem1].append(elem2)
    graph[elem2].append(elem1)
for i in range(N + 1):
    graph[i].sort()
DFS(graph, V, check)
print(" ".join(map(str, graph[0])))
check = [0 for _ in range(N + 1)]
graph[0] = []
BFS(graph, V, check)
print(" ".join(map(str, graph[0])))