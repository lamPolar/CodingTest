#자릿수 더하기
"""
def solution(n):
    answer = 0
    n2 = str(n)
    for i in range(len(n2)):
        answer += int(n2[i])
    
    return answer
"""
def solution(n):
    answer =0
    while True:
        answer += n%10
        n = n//10
        if n<10:
            answer += n
            break
    return answer
