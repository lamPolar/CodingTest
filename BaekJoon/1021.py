import sys
from collections import deque

N, M = map(int, input().split())
queue = deque([i+1 for i in range(N)])
elements = list(map(int, input().split()))
t_cnt = 0
cnt1 = 0
cnt2 = 0
i = 0
while (i < M):
    if (elements[i] == queue[0]):
        queue.popleft()
        i += 1
        if (cnt1 > cnt2):
            t_cnt += cnt2
        else:
            t_cnt += cnt1
        cnt1 = 0
        cnt2 = 0
    else :
        while (elements[i] != queue[0]):
            queue.rotate(1)
            cnt1 += 1
        queue.rotate(-1 * cnt1)
        while (elements[i] != queue[0]):
            queue.rotate(-1)
            cnt2 += 1
print(t_cnt)