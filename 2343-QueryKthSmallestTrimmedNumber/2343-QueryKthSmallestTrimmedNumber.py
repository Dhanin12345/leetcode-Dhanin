# Last updated: 9/12/2026, 10:20:25 AM
class Solution:
    def smallestTrimmedNumbers(self, nums, queries):
        ans = []
        n = len(nums)
        
        for k, trim in queries:
            # Trim each number to the last 'trim' digits
            trimmed = [(num[-trim:], i) for i, num in enumerate(nums)]
            
            # Sort by trimmed value, then by index
            trimmed.sort(key=lambda x: (x[0], x[1]))
            
            # Get the index of the k-th smallest
            ans.append(trimmed[k - 1][1])
        
        return ans


# Example usage
solver = Solution()
print(solver.smallestTrimmedNumbers(["102","473","251","814"], [[1,1],[2,3],[4,2],[1,2]]))
# Output: [2,2,1,0]

print(solver.smallestTrimmedNumbers(["24","37","96","04"], [[2,1],[2,2]]))
# Output: [3,0]
