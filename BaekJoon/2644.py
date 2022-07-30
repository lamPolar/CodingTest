import sys

def BFS(A, B, relative, check):
    queue = [A, 0]
    count = 0
    while (queue):
        person = queue.pop(0)
        if (person == B):
            return (count)
        if (person == 0):
            if (len(queue)):
                count += 1
                queue.append(0)
        if (check[person] == 0):
            for p in relative[person]:
                queue.append(p)
        check[person] = 1
    return (-1)


N = int(input())
A, B = map(int, input().split())
M = int(input())
relative = [[] for _ in range(N + 1)]
for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    relative[X].append(Y)
    relative[Y].append(X)
for i in range(M):
    relative[i].sort()
check = [0 for _ in range(N +1 )]
print(BFS(A, B, relative, check))
    