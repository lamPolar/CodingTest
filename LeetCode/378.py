from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        mergedlist = []
        for i in range(n):
            for j in range(n):
                mergedlist.append(matrix[i][j])

        return sorted(mergedlist)[k-1]

    def kthSmallest(self, matrix:List[List[int]], k:int) -> int:
        return sorted([j for row in matrix for j in row])[k-1]
        #한줄로 줄인것


if __name__ == "__main__":
    a = Solution()
    result = a.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8)
    print(result)
