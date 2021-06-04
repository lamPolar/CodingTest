from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitmax = 0 #리턴값
        minvalue = prices[0] # 최소값
        #매번 for문을 돌때마다 현재값에서 최소값을 뺀것과 현재 maxprofit을 비교
        for i in range(1 , len(prices)):
            profitmax = max(profitmax, prices[i]-minvalue)
            minvalue = min(minvalue, prices[i])
        return profitmax


if __name__ == "__main__":
    a = Solution()
#    result = a.maxProfit([2,7,3,5,1,6,4]) #
    result = a.maxProfit([7,6,4,3,1])
    print(result)
