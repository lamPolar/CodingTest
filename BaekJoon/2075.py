import heapq
import sys

N = int(input())
numbers = []
box = []
for _ in range(N):
    numbers = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(numbers)
    if (len(box) >= N):
        for _ in range(N) :
            num = heapq.heappop(numbers)
            if num > box[0]:
                heapq.heappush(box, num)
                heapq.heappop(box)
    else:
        for _ in range(N):
            heapq.heappush(box, heapq.heappop(numbers))
print(heapq.heappop(box))