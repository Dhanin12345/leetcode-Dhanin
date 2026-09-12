// Last updated: 9/12/2026, 10:20:48 AM
class Solution {
    public boolean makeEqual(String[] words) {
        int[] count = new int[26];

        for (String word : words) {
            for (char ch : word.toCharArray()) {
                count[ch - 'a']++;
            }
        }

        int n = words.length;

        for (int i = 0; i < 26; i++) {
            if (count[i] % n != 0) {
                return false;
            }
        }

        return true;
    }
}