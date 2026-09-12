# Last updated: 9/12/2026, 10:18:43 AM
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