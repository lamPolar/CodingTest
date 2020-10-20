#정수 제곱근 판별 
"""
import math
def solution(n):
    answer = 0
    x = math.sqrt(n)
    if x.is_integer():
        answer = (x+1)**2
    else :  answer = -1
    return answer
"""
def solution(n):
    answer = 0
    for i in range(n+1):
        if i**2 ==n:
            answer = (i+1)**2
            return answer
    answer = -1
    return answer
