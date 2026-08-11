# Last updated: 8/11/2026, 4:02:08 PM
class Solution:
    def checkGoodInteger(self, n):
        digitSum = 0
        squareSum = 0

        while n > 0:
            digit = n % 10
            digitSum += digit
            squareSum += digit * digit
            n //= 10

        if squareSum - digitSum >= 50:
            return True
        else:
            return False