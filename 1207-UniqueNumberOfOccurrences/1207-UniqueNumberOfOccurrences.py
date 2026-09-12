# Last updated: 9/12/2026, 10:22:30 AM
class Solution:
    def uniqueOccurrences(self, arr):
        # Count frequency of each number
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Check if frequencies are unique
        occurrences = set()

        for count in freq.values():
            if count in occurrences:
                return False
            occurrences.add(count)

        return True