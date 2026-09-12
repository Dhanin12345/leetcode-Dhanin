# Last updated: 9/12/2026, 10:22:38 AM
class Solution:
    def balanceBST(self, root):

        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        nums = inorder(root)

        def build(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            node = TreeNode(nums[mid])

            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)

            return node

        return build(0, len(nums) - 1)