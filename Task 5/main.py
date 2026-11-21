
import random
import time
import sys

readings = [random.randint(-60, 60) for _ in range(10000)]

# Method 1: Using for loop and append
valid = []

for temp in readings:
    if -50 <= temp <= 50:
        valid.append(temp)

fahrenheit = []

for temp in valid:
    fahrenheit.append((temp * 9/5) + 32)

# Method 2: Using list comprehension
valid_comp = [t for t in readings if -50 <= t <= 50]

fahrenheit_comp = [(t * 9/5) + 32 for t in valid_comp]

# Method 3: Using map(), filter() and lambda
valid_map = list(filter(lambda t: -50 <= t <= 50, readings))

fahrenheit_map = list(map(lambda t: (t * 9/5) + 32, valid_map))

# Alarm minutes (outside 2 to 8 degrees)
alarms = [
    minute for minute, temp in enumerate(readings, start=1)
    if -50 <= temp <= 50 and not (2 <= temp <= 8)
]

# Dictionary comprehension
temp_dict = {i+1: t for i, t in enumerate(valid_comp)}

# Set comprehension
temp_set = {t for t in valid_comp}

print("Valid readings:", valid_comp)
print("Fahrenheit:", fahrenheit_comp)
print("Alarm minutes:", alarms)
print("Dictionary:", temp_dict)
print("Set:", temp_set)

print("All methods equal:", valid == valid_comp == valid_map)

# Generator expression memory
generator = (t for t in readings if -50 <= t <= 50)

print("List memory:", sys.getsizeof(valid_comp))
print("Generator memory:", sys.getsizeof(generator))

# Execution time
start = time.time()
[t for t in readings if -50 <= t <= 50]
print("Comprehension time:", time.time() - start)
