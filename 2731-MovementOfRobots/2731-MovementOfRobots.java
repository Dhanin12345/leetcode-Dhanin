// Last updated: 9/12/2026, 10:20:01 AM
import java.util.*;

class Solution {
    public int sumDistance(int[] nums, String s, int d) {

        int n = nums.length;
        long[] positions = new long[n];

        // Calculate final positions
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == 'L') {
                positions[i] = (long) nums[i] - d;
            } else {
                positions[i] = (long) nums[i] + d;
            }
        }

        // Sort final positions
        Arrays.sort(positions);

        long result = 0;
        long prefixSum = 0;
        long MOD = 1_000_000_007L;

        // Calculate sum of pairwise distances
        for (int i = 0; i < n; i++) {

            result += positions[i] * i - prefixSum;
            result %= MOD;

            prefixSum += positions[i];
            prefixSum %= MOD;
        }

        return (int) result;
    }
}