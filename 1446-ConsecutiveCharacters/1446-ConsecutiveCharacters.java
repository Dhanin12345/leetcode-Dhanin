// Last updated: 9/12/2026, 10:21:48 AM
class Solution {
    public int maxPower(String s) {
        int max = 1;
        int count = 1;

        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                count++;
            } else {
                count = 1;
            }
            max = Math.max(max, count);
        }

        return max;
    }
}