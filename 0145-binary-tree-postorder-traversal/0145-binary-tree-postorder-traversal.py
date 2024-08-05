# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans=[]
        head=[root]
        while head:
            node=head.pop()
            ans.append(node.val)
            if node.left:
                head.append(node.left)
            if node.right:
                head.append(node.right)
        return ans[::-1]



        