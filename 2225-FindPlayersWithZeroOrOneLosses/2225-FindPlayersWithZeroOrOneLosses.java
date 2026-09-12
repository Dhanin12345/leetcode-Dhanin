// Last updated: 9/12/2026, 10:22:22 AM
import java.util.*;

class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {

        Map<Integer, Integer> losses = new HashMap<>();

        // Count losses for every player
        for (int[] match : matches) {
            int winner = match[0];
            int loser = match[1];

            // Make sure both players are recorded
            losses.putIfAbsent(winner, 0);
            losses.put(loser, losses.getOrDefault(loser, 0) + 1);
        }

        List<Integer> zeroLoss = new ArrayList<>();
        List<Integer> oneLoss = new ArrayList<>();

        // Separate players by number of losses
        for (Map.Entry<Integer, Integer> entry : losses.entrySet()) {

            int player = entry.getKey();
            int loss = entry.getValue();

            if (loss == 0) {
                zeroLoss.add(player);
            }
            else if (loss == 1) {
                oneLoss.add(player);
            }
        }

        // Increasing order
        Collections.sort(zeroLoss);
        Collections.sort(oneLoss);

        return Arrays.asList(zeroLoss, oneLoss);
    }
}