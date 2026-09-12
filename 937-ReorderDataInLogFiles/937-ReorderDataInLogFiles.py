# Last updated: 9/12/2026, 10:23:48 AM
class Solution:
    def reorderLogFiles(self, logs):

        letter_logs = []
        digit_logs = []

        for log in logs:
            parts = log.split()

            if parts[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        # Sort letter logs by content and identifier
        letter_logs.sort(
            key=lambda x: (x.split(" ", 1)[1], 
                           x.split(" ", 1)[0])
        )

        return letter_logs + digit_logs


# Driver Code
obj = Solution()

# Update input data here
logs = [
    "dig1 8 1 5 1",
    "let1 art can",
    "dig2 3 6",
    "let2 own kit dig",
    "let3 art zero"
]

result = obj.reorderLogFiles(logs)

print("Updated Logs:")
for log in result:
    print(log)