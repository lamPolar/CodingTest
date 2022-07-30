import sys

def BFS(want_X, want_Y, check, now_X, now_Y, L):
    count = 0
    queue = [[now_X, now_Y], [-1, 0]]
    direction = [[2,1], [2,-1], [1, 2], [1, -2], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
    while (queue):
        now_X, now_Y = queue.pop(0)
        if (now_X == -1):
            if (queue):
                queue.append([-1, 0])
                count += 1
            continue
        if (now_X == want_X and now_Y == want_Y):
            return (count)
        if (check[now_Y][now_X] == 0):
            check[now_Y][now_X] = 1
            for d in direction:
                X = now_X + d[0]
                Y = now_Y + d[1]
                if X < 0 or X >= L or Y < 0 or Y >= L:
                    continue
                if (check[Y][X] == 0):
                    queue.append([X, Y])
    return (-1)

T = int(sys.stdin.readline())
for _ in range(T):
    L = int(sys.stdin.readline())
    now_X, now_Y = map(int, sys.stdin.readline().split())
    want_X, want_Y = map(int, sys.stdin.readline().split())
    check = [[0] * L for _ in range(L)]
    count = BFS(want_X, want_Y, check, now_X, now_Y, L)
    print(count)

 # 이런식으로도 작성가능
 # if (X not in range(len(check))):
 # if (not 0<X<=len(check)):
 # 둘다 가능하지만 시간복잡도상 추천하지 않음
 # 원래 코드 :
 # if X < 0 or X >= len(check) or Y < 0 or Y >= len(check):
 # 변경 코드 :
 # if X < 0 or X >= L or Y < 0 or Y >= L:
 # len(check)를 수행하는 부분이 check가 커질수록 시간복잡도가 증가하기 때문에
 # main에서 받은 값인 L을 매개변수로 넣어주는걸로 해결