# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursive dfs approach
        q = deque()

        q.append(root)
        working = []
        while q:
            node = q.pop()
            if not node:
                continue
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            
            dummy = node.right
            node.right = node.left
            node.left = dummy
        return root



