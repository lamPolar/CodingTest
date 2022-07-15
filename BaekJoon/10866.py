import sys
from collections import deque

n = int(input())
dequeue = deque()
for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push_front":
        dequeue.appendleft(int(cmd[1]))
    if cmd[0] == "push_back":
        dequeue.append(int(cmd[1]))
    if cmd[0] == "pop_front":
        if (len(dequeue)):
            print(dequeue.popleft())
        else :
            print(-1)
    if cmd[0] == "pop_back":
        if (len(dequeue)):
            print(dequeue.pop())
        else :
            print(-1)
    if cmd[0] == "size":
        print(len(dequeue))
    if cmd[0] == "empty":
        if (len(dequeue)):
            print(0)
        else :
            print(1)
    if cmd[0] == "front":
        if (len(dequeue)):
            print(dequeue[0])
        else:
            print(-1)
    if cmd[0] == "back":
        if (len(dequeue)):
            print(dequeue[-1])
        else:
            print(-1)
    
    
    
    