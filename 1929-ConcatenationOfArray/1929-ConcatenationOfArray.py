# Last updated: 9/12/2026, 10:20:44 AM
class Solution:
    def getConcatenation(self, nums):
        return nums + nums  # Concatenate nums with itself

# Example usage:
sol = Solution()
nums = [1,2,1]
print(sol.getConcatenation(nums))
# Output: [1,2,1,1,2,1]

nums2 = [1,3,2,1]
print(sol.getConcatenation(nums2))
# Output: [1,3,2,1,1,3,2,1]