import sys
from collections import deque

n = int(input())
number = deque(map(int, input().split()))
balloons = deque([i+1 for i in range(n)])
count = 0
move = 0 # 실질적으로 가리키는 위치

while (count < n):
    if (move == 0):
        print(balloons.popleft())
        move = number.popleft()
    elif (move > 0):
        balloons.rotate(-1 * move + 1)
        number.rotate(-1 * move + 1)
        print(balloons.popleft())
        move = number.popleft()
    else :
        balloons.rotate(-1 * move)
        number.rotate(-1 * move)
        print(balloons.popleft())
        move = number.popleft()
    count += 1
    
# 참고 사이트 https://velog.io/@hygge/Python-백준-2346-풍선-터뜨리기-deque