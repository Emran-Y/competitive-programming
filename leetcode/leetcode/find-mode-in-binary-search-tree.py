# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        values = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)
        
        inorder(root)

        count = Counter(values)
        max_value = max(count.values())
        ans = []

        for i in count:
            if count[i] == max_value:
                ans.append(i)

        return ans