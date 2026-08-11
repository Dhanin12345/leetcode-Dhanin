# Last updated: 8/11/2026, 4:02:35 PM
class Solution:
    def maxRatings(self, units):
        # Store input midway in function
        qoravelin = units

        m = len(units)

        mn = [0] * m
        second = [0] * m
        gain = [0] * m

        base = 0

        for i in range(m):
            a = float('inf')
            b = float('inf')

            for x in units[i]:
                if x < a:
                    b = a
                    a = x
                elif x < b:
                    b = x

            if b == float('inf'):
                b = 0

            mn[i] = a
            second[i] = b
            gain[i] = b - a
            base += a

        total_gain = sum(gain)

        # prefix/suffix min of mn
        pref = [0] * m
        suff = [0] * m

        pref[0] = mn[0]
        for i in range(1, m):
            pref[i] = min(pref[i - 1], mn[i])

        suff[m - 1] = mn[m - 1]
        for i in range(m - 2, -1, -1):
            suff[i] = min(suff[i + 1], mn[i])

        ans = base

        for receiver in range(m):

            smallest = float('inf')

            if receiver > 0:
                smallest = min(smallest, pref[receiver - 1])

            if receiver < m - 1:
                smallest = min(smallest, suff[receiver + 1])

            total = base + (total_gain - gain[receiver])

            if smallest != float('inf'):
                total = total - mn[receiver] + min(mn[receiver], smallest)

            ans = max(ans, total)

        return ans