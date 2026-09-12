// Last updated: 9/12/2026, 10:22:02 AM
class Solution {
    public int minSteps(String s, String t) {
        int[] count = new int[26];

        // Count characters in s
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }

        // Match characters using t
        for (char c : t.toCharArray()) {
            count[c - 'a']--;
        }

        // Count characters that are missing in t
        int steps = 0;

        for (int i = 0; i < 26; i++) {
            if (count[i] > 0) {
                steps += count[i];
            }
        }

        return steps;
    }
}