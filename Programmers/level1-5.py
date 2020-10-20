#3진법 뒤집기
def solution(n):
    answer = ""
    q = n
    while q>2:
        q,r = divmod(q,3)
        answer += str(r)
    answer += str(q)
    ans = 0
    for i in answer:
        ans *= 3
        ans += int(i)
    return ans
