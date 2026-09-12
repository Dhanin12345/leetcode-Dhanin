// Last updated: 9/12/2026, 10:19:40 AM
import java.util.Arrays;

class Solution {
    public long largestPerimeter(int[] nums) {

        Arrays.sort(nums);

        long totalSum = 0;

        for (int num : nums) {
            totalSum += num;
        }

        for (int i = nums.length - 1; i >= 2; i--) {

            if (totalSum - nums[i] > nums[i]) {
                return totalSum;
            }

            totalSum -= nums[i];
        }

        return -1;
    }
}