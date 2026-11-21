
import random

readings = [random.randint(0, 20) for _ in range(365)]

# Weekly totals
weekly_totals = [sum(readings[i:i+7]) for i in range(0, 365, 7)]

print("Weekly totals:", weekly_totals)

# Maximum and minimum
print("Maximum rainfall:", max(readings))
print("Minimum rainfall:", min(readings))

print("Maximum position:", readings.index(max(readings)))
print("Minimum position:", readings.index(min(readings)))

# 7-day moving average
moving_average = [
    sum(readings[i:i+7]) / 7
    for i in range(len(readings) - 6)
]

print("Moving average:", moving_average)

# Dry days
dry_days = [i+1 for i in range(365) if readings[i] == 0]

print("Dry days:", dry_days)
