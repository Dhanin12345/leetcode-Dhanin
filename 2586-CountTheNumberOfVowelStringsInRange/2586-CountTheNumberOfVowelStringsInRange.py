# Last updated: 9/12/2026, 10:20:14 AM
class Solution:
    def vowelStrings(self, words, left, right):
        vowels = "aeiou"
        count = 0

        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1

        return count