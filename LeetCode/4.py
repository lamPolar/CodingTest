#4.median of two sorted arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mer = []
        if len(nums1)==0:
            mer = nums2
        elif len(nums2)==0:
            mer = nums1
        else :
            mer = nums1 + nums2
        mer.sort()
        sum = 0
        if len(mer)%2==0:
            for i in mer[len(mer)//2-1:len(mer)//2+1]:
                sum += i
            return sum/2
        else:
            return mer[len(mer)//2]

