import sys
from collections import deque

n = int(input())
balloons = deque(enumerate(map(int, input().split())))
count = 0
move = 0 # 실질적으로 가리키는 위치

while (count < n):
    if (move > 0):
        balloons.rotate(-1 * move + 1)
    elif (move < 0) :
        balloons.rotate(-1 * move)
    num, move = balloons.popleft()
    print(num + 1)
    count += 1
        