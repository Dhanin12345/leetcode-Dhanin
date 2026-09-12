// Last updated: 9/12/2026, 10:19:37 AM
import java.util.*;

class Solution {
    public long maximumSubarraySum(int[] nums, int k) {

        Map<Long, Long> minPrefix = new HashMap<>();

        long prefixSum = 0;
        long maxSum = Long.MIN_VALUE;

        for (int x : nums) {

            long value = x;

            // Case 1: first element = x - k
            if (minPrefix.containsKey(value - k)) {
                long sum = prefixSum + value
                         - minPrefix.get(value - k);

                maxSum = Math.max(maxSum, sum);
            }

            // Case 2: first element = x + k
            if (minPrefix.containsKey(value + k)) {
                long sum = prefixSum + value
                         - minPrefix.get(value + k);

                maxSum = Math.max(maxSum, sum);
            }

            // Keep minimum prefix sum for this value
            minPrefix.merge(
                value,
                prefixSum,
                Math::min
            );

            prefixSum += value;
        }

        return maxSum == Long.MIN_VALUE ? 0 : maxSum;
    }
}