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
        q.append(root)
        d=0

        while q:
            d+=1
            for _ in range(len(q)):
                first=q.popleft()
                if first.left:
                    q.append(first.left)
                if first.right:
                    q.append(first.right)


        return d
