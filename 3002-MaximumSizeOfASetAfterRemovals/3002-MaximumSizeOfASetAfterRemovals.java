// Last updated: 9/12/2026, 10:19:52 AM
import java.util.*;

class Solution {
    public int maximumSetSize(int[] nums1, int[] nums2) {

        int n = nums1.length;
        int half = n / 2;

        Set<Integer> a = new HashSet<>();
        Set<Integer> b = new HashSet<>();

        for (int x : nums1) {
            a.add(x);
        }

        for (int x : nums2) {
            b.add(x);
        }

        Set<Integer> common = new HashSet<>(a);
        common.retainAll(b);

        int onlyA = a.size() - common.size();
        int onlyB = b.size() - common.size();

        int fromA = Math.min(onlyA, half);
        int fromB = Math.min(onlyB, half);

        int commonNeeded = 2 * half - fromA - fromB;

        int answer = fromA + fromB
                   + Math.min(common.size(), commonNeeded);

        return answer;
    }
}