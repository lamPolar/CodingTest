import sys

# 어딘가를 떠나서 1000미터를 이동하기 전에, 편의점을 만나거나 페스티벌에 도착하면 된다.
# 어딘가에서 다음 위치로 이동할 때는 직각으로 이동한다 (대각선 아님)
# x좌표의 차이 + y좌표의 차이만큼이라고 생각.
def BFS(queue, Map, festX, festY):
    check = []
    while (queue):
        X, Y = queue.pop()
        if (abs(festX - X) + abs(festY - Y) <= 1000):
            print("happy")
            return
        check.append([X, Y])
        for i in Map:
            if (abs(i[0] - X) + abs(i[1] - Y) <= 1000) and i not in check:
                queue.append(i)
                Map.remove(i)
    print("sad")

    
T = int(input())
for _ in range(T):
    N = int(input())
    Map = []
    queue = []
    homeX, homeY = map(int, sys.stdin.readline().split())
    for _ in range(N):
        X, Y = map(int, sys.stdin.readline().split())
        Map.append([X, Y])
    festX, festY = map(int, sys.stdin.readline().split())
    queue.append([homeX, homeY])
    BFS(queue, Map, festX, festY)