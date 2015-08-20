"""
You got a box with a combination lock. The lock has a display showing n digits.
There are two buttons on the box, each button changes digits on the display.
You have quickly discovered that the first button adds 1 to all the digits
(all digits 9 become digits 0), and the second button shifts all the digits on
the display one position to the right (the last digit becomes the first one). 
For example, if the display is currently showing number 579, then if we push 
the first button, the display will show 680, and if after that we push the 
second button, the display will show 068.

You know that the lock will open if the display is showing the smallest
possible number that can be obtained by pushing the buttons in some order.
The leading zeros are ignored while comparing numbers. Now your task is to
find the desired number.

1) Split the combination into individual integers
2) Build an array for each possible initial combination (swaps)
3) Determine amount needed to make array[0] == 0
4) Add the above amount to entire array
5) %10 each value to determine true value
6) Iterate through each combination to determine solution
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

def test_secret_combination():
    assert '024' == secret_combination(3, 579)
    assert '0142' == secret_combination(4, 2014)
    assert '0148' == secret_combination(4, 4582)
