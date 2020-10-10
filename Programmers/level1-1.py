#약수의 합
def solution(n):
    answer = 0
    for i in range(1,n):
        if n % i ==0:
            answer += i
    answer += n
    return answer
