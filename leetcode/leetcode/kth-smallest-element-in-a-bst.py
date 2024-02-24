# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            nonlocal k
            if not root:
                return None
            
            left = inorder(root.left)

            if left != None:
                return left
            
            k-=1

            if k == 0:
                return root.val
            return inorder(root.right)
        return inorder(root)