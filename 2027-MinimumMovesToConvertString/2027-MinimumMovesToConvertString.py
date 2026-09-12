# Last updated: 9/12/2026, 10:20:33 AM
class Solution:
    def minimumMoves(self, s):
        moves = 0
        i = 0

        while i < len(s):
            if s[i] == 'X':
                moves += 1
                i += 3      # Skip the next 3 characters
            else:
                i += 1

        return moves