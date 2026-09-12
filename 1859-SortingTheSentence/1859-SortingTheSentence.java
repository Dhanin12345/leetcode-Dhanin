// Last updated: 9/12/2026, 10:20:51 AM
class Solution {
    public String sortSentence(String s) {
        String[] words = s.split(" ");
        String[] result = new String[words.length];

        for (String word : words) {
            int index = word.charAt(word.length() - 1) - '1';
            result[index] = word.substring(0, word.length() - 1);
        }

        StringBuilder ans = new StringBuilder();

        for (int i = 0; i < result.length; i++) {
            ans.append(result[i]);
            if (i != result.length - 1) {
                ans.append(" ");
            }
        }

        return ans.toString();
    }
}