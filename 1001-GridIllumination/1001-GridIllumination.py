# Last updated: 9/12/2026, 10:23:30 AM
class Solution:
    def gridIllumination(self, n, lamps, queries):

        lamp_set = set()

        row = {}
        col = {}
        diag1 = {}   # r - c
        diag2 = {}   # r + c

        # Add lamps
        for r, c in lamps:
            if (r, c) not in lamp_set:
                lamp_set.add((r, c))

                row[r] = row.get(r, 0) + 1
                col[c] = col.get(c, 0) + 1
                diag1[r - c] = diag1.get(r - c, 0) + 1
                diag2[r + c] = diag2.get(r + c, 0) + 1


        answer = []

        for r, c in queries:

            # Check light
            if (row.get(r, 0) > 0 or
                col.get(c, 0) > 0 or
                diag1.get(r-c, 0) > 0 or
                diag2.get(r+c, 0) > 0):

                answer.append(1)

            else:
                answer.append(0)


            # Turn off lamps in 3x3 area
            for nr in range(r-1, r+2):
                for nc in range(c-1, c+2):

                    if (nr, nc) in lamp_set:

                        lamp_set.remove((nr, nc))

                        row[nr] -= 1
                        col[nc] -= 1
                        diag1[nr-nc] -= 1
                        diag2[nr+nc] -= 1


        return answer