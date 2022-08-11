import sys

def RedGreen(map):
    newmap =[]
    for m in map:
        newmap.append(m.replace("G", "R"))
    return (newmap)
 
def Group(map, N):
    check = [[0 for _ in range(N)]for _ in range(N)]
    count = 0
    queue = []
    direction = [[1,0],[0,1],[-1,0],[0,-1]]
    for i in range(N):
        for j in range(N):
            if check[i][j] == 1:
                continue
            queue.append([i, j])
            while (queue):
                y, x = queue.pop()
                check[y][x] = 1
                for d in direction:
                    newY = y + d[0]
                    newX = x + d[1]
                    if (newY < 0 or newY == N or newX < 0 or newX == N):
                        continue
                    if (map[newY][newX] == map[y][x]):
                        if (check[newY][newX] == 0):
                            queue.append([newY, newX])
                if (len(queue) == 0):
                    count += 1
    print(count)

N = int(input())
map = [sys.stdin.readline().strip() for _ in range(N)]
Group(map, N)
newmap = RedGreen(map)
Group(newmap, N)