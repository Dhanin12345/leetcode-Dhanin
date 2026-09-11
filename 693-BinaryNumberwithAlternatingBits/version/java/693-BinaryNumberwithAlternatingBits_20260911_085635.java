// Last updated: 9/11/2026, 8:56:35 AM
1class Solution {
2    public boolean hasAlternatingBits(int n) {
3        int previous = n & 1;
4        n = n >> 1;
5
6        while (n > 0) {
7            int current = n & 1;
8
9            if (current == previous) {
10                return false;
11            }
12
13            previous = current;
14            n = n >> 1;
15        }
16
17        return true;
18    }
19}