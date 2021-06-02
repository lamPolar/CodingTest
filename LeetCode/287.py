#1부터 n중에 중복되는 1개의 수 찾기

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ret =0 #return용
        temp = sorted(nums[:])#정렬된 nums

        while ret==0: #return 값이 정해지지 않은동안
            mid = int(len(temp)/2) 
            #set된 결과와 같지 않으면 중복값이 있다는 뜻임
            if temp[:mid] != sorted(set(temp[:mid])): 
                temp = temp[:mid]
                continue
            if temp[mid:] != sorted(set(temp[mid:])):
                temp = temp[mid:]
                continue
            #if조건이 두개 다 맞지 않으면 ret에 할당 가능
            ret = temp[mid]
        return ret
