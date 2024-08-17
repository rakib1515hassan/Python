"""
    > We can write a Python script that finds the subset with the maximum sum from the given list a. We'll iterate through all possible subsets and calculate their sums, keeping track of the maximum sum encountered.
"""

import itertools

a = [5, 21, 11, 7, 29, 39, 51, 57, 83, 81]

# Initialize max sum
max_sum = 0
max_subset = []

# Generate all possible subsets
for r in range(1, len(a) + 1):
    for subset in itertools.combinations(a, r):
        subset_sum = sum(subset)
        if subset_sum > max_sum:
            max_sum = subset_sum
            max_subset = subset

print("Subset with maximum sum:", max_subset)
print("Maximum sum:", max_sum)



"""
    > Python script that not only finds the subset with the maximum sum but also identifies the two largest values within that subset along with their indices:
"""

import itertools

a = [5, 21, 11, 83, 7, 29, 39, 51, 57, 13, 81, 11]

# Initialize max sum
max_sum = 0
max_subset = []

# Generate all possible subsets
for r in range(1, len(a) + 1):
    for subset in itertools.combinations(a, r):
        subset_sum = sum(subset)
        if subset_sum > max_sum:
            max_sum = subset_sum
            max_subset = subset

# Find the two largest values in the max subset
max_values = sorted(max_subset, reverse=True)[:2]
max_indices = [a.index(val) for val in max_values]

print("Subset with maximum sum:", max_subset)
print("Maximum sum:", max_sum)
print("Two largest values:", max_values)
print("Indices of the two largest values:", max_indices)
