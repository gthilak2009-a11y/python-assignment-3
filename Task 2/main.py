
import copy
import sys
import time

rows, cols = 3, 4

# Incorrect grid
bad = [[0] * cols] * rows
bad[0][1] = 7

# Correct grid using list comprehension
good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7

print("bad :", bad)
print("good:", good)
print(bad[0] is bad[1], good[0] is good[1])

# Tuples as dictionary keys
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}

print(stops[(13.0418, 80.2341)])

# Tuple unpacking
for coordinates, name in stops.items():
    latitude, longitude = coordinates
    print(name, latitude, longitude)

# Aliasing
a = [10, 20, 30]
b = a
b[0] = 100
print("Aliasing:", a)

# Shallow copy
c = [10, 20, 30]
d = copy.copy(c)
d[0] = 200
print("Original:", c)
print("Shallow copy:", d)

# Deep copy
x = [[1, 2], [3, 4]]
y = copy.deepcopy(x)
y[0][0] = 99

print("Original nested list:", x)
print("Deep copy:", y)

# Memory comparison
values = list(range(1000000))
tuple_values = tuple(values)

print("List memory:", sys.getsizeof(values))
print("Tuple memory:", sys.getsizeof(tuple_values))

# Time comparison
start = time.time()
list_data = list(range(100000))
print("List creation time:", time.time() - start)

start = time.time()
tuple_data = tuple(range(100000))
print("Tuple creation time:", time.time() - start)
