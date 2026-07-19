# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revlist=[]
        prev_node=None
        temp=head
        if head is None:
            return head
        
        while temp is not None:
            next_node=temp.next
            temp.next=prev_node
            prev_node=temp
            temp=next_node
        return prev_node