# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head
        while curr:
            nextNode = curr.next
            if nextNode in seen:
                return True
            seen.add(nextNode)
            curr = nextNode
        return False
        