# Last updated: 9/12/2026, 10:24:05 AM
from collections import Counter
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        count = Counter(deck)

        x = reduce(gcd, count.values())

        return x >= 2