# Last updated: 8/11/2026, 4:02:38 PM
class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        n, m = len(landStartTime), len(waterStartTime)
        ans = float('inf')

        for i in range(n):
            for j in range(m):
                # Case A: land → water
                finish_land = landStartTime[i] + landDuration[i]
                start_water = max(waterStartTime[j], finish_land)
                finish_water = start_water + waterDuration[j]
                ans = min(ans, finish_water)

                # Case B: water → land
                finish_water = waterStartTime[j] + waterDuration[j]
                start_land = max(landStartTime[i], finish_water)
                finish_land = start_land + landDuration[i]
                ans = min(ans, finish_land)

        return ans
