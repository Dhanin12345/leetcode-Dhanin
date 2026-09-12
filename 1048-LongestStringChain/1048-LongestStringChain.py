# Last updated: 9/12/2026, 10:23:15 AM
class Solution:
    def longestStrChain(self, words):
        words.sort(key=len)

        dp = {}
        ans = 1

        for word in words:
            dp[word] = 1

            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]

                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)

            ans = max(ans, dp[word])

        return ans