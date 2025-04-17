import numpy as np

array = np.array(["apple", "banana", "cherry", "date"])
centered = np.array([s.center(15, '_') for s in array])
left_justified = np.array([s.ljust(15, '_') for s in array])
right_justified = np.array([s.rjust(15, '_') for s in array])

print("Original Array:")
print(array)
print("\nCentered:")
print(centered)
print("\nLeft-Justified:")
print(left_justified)
print("\nRight-Justified:")
print(right_justified)