import sys

def BFS(computer, queue, check):
    count = 0
    while (len(queue)):
        node = queue.pop(0)
        if (check[node] == 0):
            while (len(computer[node])):
                i = computer[node].pop(0)
                if (check[i] == 0):
                    queue.append(i)
            count += 1
            check[node] = 1
    return (count)

count = 0
def DFS(computer, V, check):
    global count

    if (check[V] == 1):
        return
    check[V] = 1
    count += 1
    for i in computer[V]:
        DFS(computer, i, check)

N = int(input())
V = int(input())
computer = [[] for _ in range(N + 1)]
for _ in range(V):
    node1, node2 = map(int, sys.stdin.readline().split())
    computer[node1].append(node2)
    computer[node2].append(node1)
for i in range(N + 1):
    computer[i].sort()
check = [0 for _ in range(N + 1)]
# queue = [1]
# count = BFS(computer, queue, check)
DFS(computer, 1, check)
print(count - 1)