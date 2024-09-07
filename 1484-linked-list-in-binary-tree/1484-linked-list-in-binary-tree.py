# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        res=False
        if root==None: return False
        if head==None: return True
        if root.val==head.val:
            res=self.ispath(head.next,root.right)or self.ispath(head.next,root.left)
        return res or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)
    
    def ispath(self,l:Optional[ListNode],t:Optional[TreeNode])-> bool:
        if l==None: return True
        if t==None: return False

        if l.val==t.val:
            return self.ispath(l.next,t.left) or self.ispath(l.next,t.right)
        else:
            return False
