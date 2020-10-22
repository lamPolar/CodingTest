#주식가격
def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt=0 #마지막까지 가격이 안떨어진것 확인용
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                #print(answer)
                cnt=1
                break
        if cnt == 0:
            answer.append(len(prices)-i-1)
    return answer
#주식가격-stack 방식
def solution(prices):
    n= len(prices)
    answer = [0]*n
    stack = [prices[0]]
    clock = 1
    clock_stack = [1]    
    for i in prices[1:]:
        clock+=1
        while len(stack)>0 and stack[-1]>i:
            stack.pop()
            t= clock_stack.pop()
            answer[t-1]=clock-t
        stack.append(i)
        clock_stack.append(clock)
   # print(answer,stack)
    for i in range(n):
        if answer[i]==0:
            answer[i] = n-i-1
   # print(answer, stack)
    return answer
