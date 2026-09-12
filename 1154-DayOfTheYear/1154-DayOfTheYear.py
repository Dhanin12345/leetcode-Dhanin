# Last updated: 9/12/2026, 10:22:42 AM
class Solution:
    def dayOfYear(self, date):
        year, month, day = map(int, date.split("-"))

        days_in_month = [
            31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31
        ]

        # Leap year check
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            days_in_month[1] = 29

        result = day

        for i in range(month - 1):
            result += days_in_month[i]

        return result