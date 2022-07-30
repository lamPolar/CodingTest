import heapq
import sys

heap = [] 
N = int(input())
for _ in range(N):
    cmd = int(sys.stdin.readline())
    if (cmd > 0):
        heapq.heappush(heap, cmd)
    else:
        if (len(heap)):
            print(heapq.heappop(heap))
        else : 
            print(0)
