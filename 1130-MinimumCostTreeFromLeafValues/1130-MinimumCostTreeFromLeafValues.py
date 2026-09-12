# Last updated: 9/12/2026, 10:22:53 AM
class Solution:
    def mctFromLeafValues(self, arr):

        stack = [float('inf')]
        cost = 0

        for num in arr:

            # Remove smaller values
            while stack[-1] <= num:
                mid = stack.pop()
                cost += mid * min(stack[-1], num)

            stack.append(num)

        # Remove remaining values
        while len(stack) > 2:
            cost += stack.pop() * stack[-1]

        return cost