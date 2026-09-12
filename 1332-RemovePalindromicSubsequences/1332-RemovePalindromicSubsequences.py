# Last updated: 9/12/2026, 10:22:15 AM
class Solution:
    def removePalindromeSub(self, s):
        if s == s[::-1]:
            return 1
        return 2