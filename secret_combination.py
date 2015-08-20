"""
1) Split the combination into individual integers
2) Build an array for each possible initial combination (swaps)
3) Determine amount needed to make array[0] == 0
4) Add the above amount to entire array
5) %10 each value to determine true value
6) Iterate through each combination to determine solution

579 -> 024
2014 -> 0142

4582 ->  0148
5824 ->  0379
8245 ->  0467
2458 ->  0236


initial = 1238
str(initial) -> '1238'
['1', '2', '3', '8']

additive = 9
list = [1,2,3,4]

[0, 0, 2, 3] -> 123
"""
from collections import deque

def secret_combination(length, initial):
    # We will use a double ended queue for easy O(n) rotation
    # of elements.
    initial = deque([int(x) for x in list(str(initial))])
    all_combinations = []

    for queue in range(0, length):
        # Rotate and add new [list of numbers] to all_combinations
        initial.rotate() # Rotate moves [1, 2, 3, 4] to [4, 1, 2, 3]
        all_combinations.append(list(initial))
    for index, combination in enumerate(all_combinations):
        # Determine additive to reach 0
        additive = 10 - combination[0]
        new_combination = [(x + additive) % 10 for x in combination]
        # Coerce list of numbers to single integer. [0, 1, 2, 3] -> 123 
        new_combination = int(''.join([str(x) for x in new_combination]))
        # Replace this combination with new integer
        all_combinations[index] = new_combination

    minimum = min(all_combinations)

    # Pad minimum with appropriate number of '0's
    min_array = list(str(minimum))
    secret_combination = ['0'] * length  # Initialize 0's
    secret_combination[-len(min_array):] = min_array
    return ''.join(secret_combination)
