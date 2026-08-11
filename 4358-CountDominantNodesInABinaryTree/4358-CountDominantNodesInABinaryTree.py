# Last updated: 8/11/2026, 4:02:09 PM
class Solution(object):
    def countDominantNodes(self, root):
        self.count=0
        def dfs(node):
            if not node:
                return float('-inf')
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            subtree_max = max(node.val,left_max,right_max)
            if node.val ==subtree_max:
                self.count +=1
            return subtree_max
        dfs(root)
        return self.count