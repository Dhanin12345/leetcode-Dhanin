// Last updated: 9/12/2026, 10:20:54 AM
class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean[] seen = new boolean[26];

        for (char ch : sentence.toCharArray()) {
            seen[ch - 'a'] = true;
        }

        for (boolean letter : seen) {
            if (!letter) {
                return false;
            }
        }

        return true;
    }
}