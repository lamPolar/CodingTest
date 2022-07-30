import heapq
import sys

card = [] 
N = int(input())
sum = 0
for _ in range(N):
    number = int(sys.stdin.readline())
    heapq.heappush(card, number)
while(len(card) > 1):
    cnt = heapq.heappop(card) + heapq.heappop(card)
    sum += cnt
    heapq.heappush(card, cnt)
print(sum)
