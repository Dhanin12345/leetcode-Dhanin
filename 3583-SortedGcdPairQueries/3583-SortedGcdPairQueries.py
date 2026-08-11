# Last updated: 8/11/2026, 4:02:49 PM
class Solution(object):
    def gcdValues(self, nums, queries):
        import bisect
        
        max_val = max(nums)
        
        # Step 1: frequency
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
        
        # Step 2: count multiples
        count = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            for multiple in range(g, max_val + 1, g):
                count[g] += freq[multiple]
        
        # Step 3: count pairs
        pairs = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            if count[g] >= 2:
                pairs[g] = count[g] * (count[g] - 1) // 2
        
        # Step 4: inclusion-exclusion
        for g in range(max_val, 0, -1):
            for multiple in range(2*g, max_val + 1, g):
                pairs[g] -= pairs[multiple]
        
        # Step 5: prefix sums (simulate sorted gcdPairs)
        gcd_vals = []
        prefix = []
        total = 0
        
        for g in range(1, max_val + 1):
            if pairs[g] > 0:
                total += pairs[g]
                gcd_vals.append(g)
                prefix.append(total)
        
        # Step 6: answer queries
        ans = []
        for q in queries:
            idx = bisect.bisect_left(prefix, q + 1)
            ans.append(gcd_vals[idx])
        
        return ans