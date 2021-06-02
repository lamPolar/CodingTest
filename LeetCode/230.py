# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#트리에서 k번째로 작은 수 찾기
class Solution:
    
    #inorder 트리순회방법 이용 - 재귀를 이용해 왼쪽, val, 오른쪽순으로 탐색후 val을 순서대로 ret에 저장
    def inorder(self,root, ret):
        if root.left is not None: 
            self.inorder(root.left,ret)
        ret.append(root.val)
        if root.right is not None:
            self.inorder(root.right,ret)
        return ret
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ret = list()
        ret = self.inorder(root,ret) 
        return ret[k-1] #결과적으로 받은 순서대로 정렬된 list에서 k번째로 작은 수를 return
