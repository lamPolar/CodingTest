# 0부터 n까지 2진법으로 바꿨을 때 1의 개수를 담은 list구하기

class Solution:
    def countBits(self, n: int) -> List[int]:
        m = 1
        ans = []
        for i in range(n+1):
            #0과 1일 경우 직접 추가
            if i==0:
                ans.append(0)
                continue
            if i==1:
                ans.append(1)
                continue
            #i가 2이상일경우, 2의 m제곱인지 아닌지로 나누어서 계산
            if i == 2**m:
                ans.append(1)
                m += 1 
                #i가 2의 m제곱일 경우 다음 m을 설정
                continue    
            #elif i == (2**m) -1:
            #    ans.append(m)
            #    continue     # 2의 m제곱-1의 경우 이게 더 빠르지만 컴팩트한 코드를 위해 삭제
            
            #i가 2의 m제곱이 아닐경우
            temp = i-(2**(m-1))
            ans.append(ans[temp]+1)
        return ans
