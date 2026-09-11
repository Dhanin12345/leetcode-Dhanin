// Last updated: 9/11/2026, 9:34:43 AM
1import java.util.*;
2
3class Solution {
4    public int subarraySum(int[] nums, int k) {
5
6        Map<Integer, Integer> map = new HashMap<>();
7
8        // Prefix sum 0 occurs once
9        map.put(0, 1);
10
11        int prefixSum = 0;
12        int count = 0;
13
14        for (int num : nums) {
15
16            prefixSum += num;
17
18            // Need previous prefix sum = prefixSum - k
19            if (map.containsKey(prefixSum - k)) {
20                count += map.get(prefixSum - k);
21            }
22
23            // Store current prefix sum
24            map.put(
25                prefixSum,
26                map.getOrDefault(prefixSum, 0) + 1
27            );
28        }
29
30        return count;
31    }
32}