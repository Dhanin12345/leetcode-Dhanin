// Last updated: 9/12/2026, 10:19:35 AM
class Solution {

    public int minMovesToCaptureTheQueen(
            int a, int b,
            int c, int d,
            int e, int f) {

        // Rook captures queen
        if (a == e) {
            if (!(c == a && between(d, b, f))) {
                return 1;
            }
        }

        if (b == f) {
            if (!(d == b && between(c, a, e))) {
                return 1;
            }
        }

        // Bishop captures queen
        if (Math.abs(c - e) == Math.abs(d - f)) {
            if (!(Math.abs(a - e) == Math.abs(b - f)
                    && between(a, c, e)
                    && between(b, d, f))) {
                return 1;
            }
        }

        return 2;
    }

    // Checks whether x is strictly between y and z
    private boolean between(int x, int y, int z) {
        return x > Math.min(y, z) && x < Math.max(y, z);
    }
}