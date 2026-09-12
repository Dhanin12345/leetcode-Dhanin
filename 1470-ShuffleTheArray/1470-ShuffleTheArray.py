# Last updated: 9/12/2026, 10:21:45 AM
class Solution:
    def shuffle(self, nums, n):
        ans = []
        for i in range(n):
            ans.append(nums[i])       
            ans.append(nums[i + n])   
        return ans

sol = Solution()
nums1 = [2,5,1,3,4,7]
n1 = 3
print(sol.shuffle(nums1, n1))  

nums2 = [1,2,3,4,4,3,2,1]
n2 = 4
print(sol.shuffle(nums2, n2))  

nums3 = [1,1,2,2]
n3 = 2
print(sol.shuffle(nums3, n3))  