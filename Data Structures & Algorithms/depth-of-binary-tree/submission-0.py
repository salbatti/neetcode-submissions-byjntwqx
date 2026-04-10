# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque()
        d=0
        q.append(root)
        while q:
            d+=1
            for i in range(len(q)):
                
                front=q.popleft()
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)

        return d