# Last updated: 8/11/2026, 4:02:36 PM
import bisect

class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        n, m = len(landStartTime), len(waterStartTime)

        landFinish = [landStartTime[i] + landDuration[i] for i in range(n)]
        waterFinish = [waterStartTime[j] + waterDuration[j] for j in range(m)]

        # Preprocess water rides
        water = sorted(zip(waterStartTime, waterDuration))
        ws = [w[0] for w in water]
        wd = [w[1] for w in water]
        ws_plus = [w[0] + w[1] for w in water]

        prefixMinDur = [0]*m
        prefixMinDur[0] = wd[0]
        for j in range(1,m):
            prefixMinDur[j] = min(prefixMinDur[j-1], wd[j])

        suffixMinStartPlusDur = [0]*m
        suffixMinStartPlusDur[-1] = ws_plus[-1]
        for j in range(m-2,-1,-1):
            suffixMinStartPlusDur[j] = min(suffixMinStartPlusDur[j+1], ws_plus[j])

        ans = float('inf')

        # Land -> Water
        for lf in landFinish:
            idx = bisect.bisect_right(ws, lf) - 1
            if idx >= 0:
                ans = min(ans, lf + prefixMinDur[idx])
            idx2 = bisect.bisect_right(ws, lf)
            if idx2 < m:
                ans = min(ans, suffixMinStartPlusDur[idx2])

        # Preprocess land rides
        land = sorted(zip(landStartTime, landDuration))
        ls = [l[0] for l in land]
        ld = [l[1] for l in land]
        ls_plus = [l[0] + l[1] for l in land]

        prefixMinDurLand = [0]*n
        prefixMinDurLand[0] = ld[0]
        for i in range(1,n):
            prefixMinDurLand[i] = min(prefixMinDurLand[i-1], ld[i])

        suffixMinStartPlusDurLand = [0]*n
        suffixMinStartPlusDurLand[-1] = ls_plus[-1]
        for i in range(n-2,-1,-1):
            suffixMinStartPlusDurLand[i] = min(suffixMinStartPlusDurLand[i+1], ls_plus[i])

        # Water -> Land
        for wf in waterFinish:
            idx = bisect.bisect_right(ls, wf) - 1
            if idx >= 0:
                ans = min(ans, wf + prefixMinDurLand[idx])
            idx2 = bisect.bisect_right(ls, wf)
            if idx2 < n:
                ans = min(ans, suffixMinStartPlusDurLand[idx2])

        return ans
