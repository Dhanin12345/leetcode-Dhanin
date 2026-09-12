// Last updated: 9/12/2026, 10:19:30 AM
import java.util.*;

class Solution {
    public int minimumPushes(String word) {

        // Count frequency of each character
        int[] freq = new int[26];

        for (char c : word.toCharArray()) {
            freq[c - 'a']++;
        }

        // Sort frequencies
        Arrays.sort(freq);

        int pushes = 0;
        int cost = 1;
        int count = 0;

        // Process from highest frequency to lowest
        for (int i = 25; i >= 0; i--) {

            if (freq[i] == 0) {
                break;
            }

            pushes += freq[i] * cost;
            count++;

            // Every 8 letters get the same push cost
            if (count % 8 == 0) {
                cost++;
            }
        }

        return pushes;
    }
}