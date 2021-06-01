#두 list의 교집합 구하기

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #return할 리스트를 선언
        ret = list()
        for i in nums1:
            if i in nums2:
             #nums1에 있는 i가 nums2에 있는지 확인
                ret.append(i)
                nums2.remove(i)
        return ret
        
