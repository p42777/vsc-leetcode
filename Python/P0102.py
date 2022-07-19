from ast import List

from matplotlib import collections

# Level Order Traversal by Breadth First Search
class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        result = []

        q = collections.deque() # Queue Initialization
        q.append(root)

        while q:
            qLength = len(q) # one level at a time
            level = []
            for i in range(qLength):
                node = q.popleft() # FIFO
                if node :
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
        
        return result



