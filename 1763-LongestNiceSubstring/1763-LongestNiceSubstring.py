# Last updated: 9/12/2026, 10:21:01 AM
class Solution:
    def longestNiceSubstring(self, s):

        def is_nice(sub):
            st = set(sub)
            for c in st:
                if c.swapcase() not in st:
                    return False
            return True

        def solve(s):
            if len(s) < 2:
                return ""

            st = set(s)

            for i, c in enumerate(s):
                if c.swapcase() not in st:
                    left = solve(s[:i])
                    right = solve(s[i+1:])
                    return left if len(left) >= len(right) else right

            return s  # whole string is nice

        return solve(s)