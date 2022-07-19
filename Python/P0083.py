from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr:
            while curr.next and curr.next.val == curr.val: # check duplicate
                curr.next = curr.next.next # remove duplicate
            curr = curr.next # update current node 
        return head

