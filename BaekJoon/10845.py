import sys

n = int(input())
queue = []
for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        queue.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if (len(queue)):
            print(queue.pop(0))
        else :
            print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if (len(queue)):
            print(0)
        else :
            print(1)
    elif cmd[0] == "front":
        if (len(queue)):
            print(queue[0])
        else :
            print(-1)
    elif cmd[0] == "back":
        if (len(queue)):
            print(queue[-1])
        else :
            print(-1)