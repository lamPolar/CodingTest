import sys

def BFS(map, N, M):
    check = [[[0 for _ in range(M)] for _ in range(N)]for _ in range(2)]
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = [[0, 0, 0]]
    check[0][0][0] = 1
    while (queue):
        W, X, Y = queue.pop(0)
        if (X == M - 1 and Y == N - 1):
            return (check[W][Y][X])
        for d in direction :
            newX, newY = X + d[0], Y + d[1]
            if ( 0 <= newX < M and 0 <= newY < N):
                if (map[newY][newX] == '0'):
                    # 다음에 진행할 곳이 벽이 아니라면,
                    # 만약 다음 값이 +1 보다 크면 갱신, 안크면 갱신 x
                    if (check[W][newY][newX] == 0 or check[W][newY][newX] > check[W][Y][X] + 1):
                        check[W][newY][newX] = check[W][Y][X] + 1
                    queue.append([W, newX, newY])
                else:
                    # 만약 다음에 진행할 곳이 벽이라면, 
                    # 벽을 부순전적이 없다면, 벽을 부숴보기
                    if (W == 0):
                        if (check[1][newY][newX] == 0 or check[1][newY][newX] > check[0][Y][X] + 1):
                            check[1][newY][newX] = check[0][Y][X] + 1
                        queue.append([1, newX, newY])
                    else :
                        pass
    return (-1)

N , M = map(int, sys.stdin.readline().split())
map = [list(sys.stdin.readline().strip()) for _ in range(N)]
print(BFS(map, N, M))