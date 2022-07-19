class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeElements(self, head: TreeNode, val: int) -> TreeNode:
        dummy = TreeNode(next = head)
        prev, curr = dummy, head # two pointers

        while curr:
            next = curr.next

            if curr.val == val:
                prev.next = next
            else:
                prev = curr

            curr = next
        
        return dummy.next # first node of Linked List


