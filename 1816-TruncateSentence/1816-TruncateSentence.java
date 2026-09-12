// Last updated: 9/12/2026, 10:20:58 AM
class Solution {
    public String truncateSentence(String s, int k) {
        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                count++;
                if (count == k) {
                    return s.substring(0, i);
                }
            }
        }

        return s;
    }
}