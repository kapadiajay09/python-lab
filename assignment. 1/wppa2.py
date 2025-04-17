import random

random_numbers = [random.randint(0, 1) for _ in range(100)]
longest_run = 0
current_run = 0

for num in random_numbers:
    if num == 0:
        current_run += 1
        longest_run = max(longest_run, current_run)
    else:
        current_run = 0

print("Random numbers:", random_numbers)
print("Longest run of zeroes:", longest_run)
