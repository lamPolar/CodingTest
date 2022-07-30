import sys
sys.setrecursionlimit(10**4)

def DFS(X, Y, jirung, check):
    direction = [[1,0],[0,1],[0,-1],[-1,0]]
    if (check[Y][X] == 1):
        return
    save_X = X
    save_Y = Y
    check[Y][X] = 1
    for i in direction:
        X = save_X + i[0]
        Y = save_Y + i[1]
        if (X < 0 or Y < 0 or X == len(check[0]) or Y == len(check)):
            continue
        # print(X, Y)
        if (jirung[Y][X] == 1):
            DFS(X, Y, jirung, check)

T = int(input())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    jirung = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        jirung[Y][X] = 1
    check = [[0] * M for _ in range(N)]
    count = 0
    for Y in range(N):
        for X in range(M):
            if (check[Y][X] == 0 and jirung[Y][X] == 1):
                DFS(X, Y, jirung, check)
                count += 1
    print(count)
