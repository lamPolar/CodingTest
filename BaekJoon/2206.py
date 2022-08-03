import sys

def BFS(map, N, M):
    check = [[[0 for _ in range(M)] for _ in range(N)]for _ in range(2)]
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = [[0, 0, 0]]
    check[0][0][0] = 1
    while (queue):
        # for k in queue:
        #     print(k)
        # for l in check:
        #     print(l)
        W, X, Y = queue.pop(0)
        if (X == M - 1 and Y == N - 1):
            return (check[W][Y][X])
        for d in direction :
            newX = X + d[0]
            newY = Y + d[1]
            flag = 0
            if ( 0 <= newX < M and 0 <= newY < N):
                if (map[newY][newX] == '0'):
                    # 다음에 진행할 곳이 벽이 아니라면,
                    # 벽을 부수지 않았을 때의 값이 0이거나... 
                    # 앞으로 갈 곳의 방문배열의 벽을 부수지 않았을 때의 값이 현재 나의 방문배열의 값 + 1보다 크다면, 큐에 넣는다.
                    # 방문배열도 여기서 갱신
                    if (check[0][Y][X] != 0 and (check[0][newY][newX] == 0 or check[0][newY][newX] > check[0][Y][X] + 1)):
                        flag = 1
                        check[0][newY][newX] = check[0][Y][X] + 1
                    # 앞으로 갈 곳의 방문배열의 벽을 부쉈을 때의 값이 현재 나의 방문배열의 벽을 부쉈을 때읙 값 + 1 보다 크다면, 큐에 넣는다.
                    if (check[1][newY][newX] == 0 or check[1][newY][newX] > check[1][Y][X] + 1):
                        flag = 1
                        check[1][newY][newX] = check[1][Y][X] + 1
                else:
                    # 만약 다음에 진행할 곳이 벽이라면, 
                    # 벽을 부순전적이 없다면, 벽을 부숴보기
                    # 벽을 부수지 않고 진행한 나의 방문배열 값 + 1 보다 크다면 큐에 넣는다.
                    if (check[0][Y][X] != 0 and (check[1][newY][newX] == 0 or check[1][newY][newX] > check[0][Y][X] + 1)):
                        flag = 1
                        check[1][newY][newX] = check[0][Y][X] + 1
                    # 여기까지 벽을 부순 길로 진행했고, 이곳에서부터 벽을 만났다면, 큐에 넣지 않는다.
                    else :
                        pass
            if (flag):
                queue.append([newX, newY])
    return (-1)

N , M = map(int, sys.stdin.readline().split())
map = [list(sys.stdin.readline().strip()) for _ in range(N)]
#print(map)
print(BFS(map, N, M))