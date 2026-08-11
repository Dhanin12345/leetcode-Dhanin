# Last updated: 8/11/2026, 4:02:24 PM
class Solution:
    def totalWaviness(self, num1, num2):

        def solve(n):
            if n < 0:
                return 0

            s = str(n)
            memo = {}

            def dp(pos, tight, started, length_state, prev2, prev1):
                key = (pos, tight, started, length_state, prev2, prev1)

                if key in memo:
                    return memo[key]

                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                total_count = 0
                total_wavy = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            False,
                            0,
                            10,
                            10
                        )
                        total_count += cnt
                        total_wavy += wav

                    elif not started:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            1,
                            10,
                            d
                        )
                        total_count += cnt
                        total_wavy += wav

                    elif length_state == 1:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            2,
                            prev1,
                            d
                        )
                        total_count += cnt
                        total_wavy += wav

                    else:
                        add = 0

                        if ((prev1 > prev2 and prev1 > d) or
                            (prev1 < prev2 and prev1 < d)):
                            add = 1

                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            2,
                            prev1,
                            d
                        )

                        total_count += cnt
                        total_wavy += wav + add * cnt

                memo[key] = (total_count, total_wavy)
                return memo[key]

            return dp(0, True, False, 0, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)