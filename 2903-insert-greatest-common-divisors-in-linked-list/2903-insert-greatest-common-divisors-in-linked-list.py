# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        while cur.next:
            temp=ListNode(math.gcd(cur.val,cur.next.val),cur.next)
            cur.next=temp
            cur=temp.next
        return head
        