import sys

# Read all input at once
tokens = sys.stdin.read().split()

# First token is the number of items (can be ignored since we read all)
list_items = tokens[1:]

# Track longest complete-pass streak
current_streak = 0
longest_streak = 0

for item in list_items:
    if item == "I":
        current_streak = 0
    else:
        current_streak += 1
        if current_streak > longest_streak:
            longest_streak = current_streak

print(longest_streak)
