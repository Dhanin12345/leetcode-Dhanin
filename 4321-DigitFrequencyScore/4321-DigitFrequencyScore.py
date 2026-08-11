# Last updated: 8/11/2026, 4:02:21 PM
class Solution:
    def digitFrequencyScore(self, n):
        s = str(n)
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        score = 0
        for ch, count in freq.items():
            score += int(ch) * count

        return score