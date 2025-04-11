# Read input
HH, MM = map(int, input().split())

# Start time in minutes from 0 (9:00 AM)
start_minutes = 9 * 60

# Submission time in total minutes
submission_minutes = HH * 60 + MM

# Time consumed is the difference
time_consumed = submission_minutes - start_minutes

# Output result
print(time_consumed)
