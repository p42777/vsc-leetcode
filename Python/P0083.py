from black import Node


class Solution:
    def deleteDuplicates(self, head: Node) -> Node:
        curr = head

        while curr:
            while curr.next and curr.next.val == curr.val: # check duplicate
                curr.next = curr.next.next # remove duplicate
            curr = curr.next # update current node 
        return head

