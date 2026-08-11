// Last updated: 8/11/2026, 4:03:26 PM
class Solution {
    public int findTheLongestBalancedSubstring(String s) {
        int max = 0;
        int i = 0;
        int n = s.length();

        while (i < n) {
            int zeroCount = 0;
            int oneCount = 0;

            while (i < n && s.charAt(i) == '0') {
                zeroCount++;
                i++;
            }

            while (i < n && s.charAt(i) == '1') {
                oneCount++;
                i++;
            }

            max = Math.max(max, 2 * Math.min(zeroCount, oneCount));
        }

        return max;
    }
}