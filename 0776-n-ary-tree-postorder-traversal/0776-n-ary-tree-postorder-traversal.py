"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        if root is None:
            return []
        
        stack,res=[root],[]
        while stack:
            node=stack.pop()
            res.append(node.val)
            for c in node.children:
                if c:
                    stack.append(c)
        return res[::-1]
       