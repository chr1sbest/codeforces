"""
One hot summer day Pete and his friend Billy decided to buy a watermelon. They
chose the biggest and the ripest one, in their opinion. After that the
watermelon was weighed, and the scales showed w kilos. They rushed home, dying
of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide
the watermelon in such a way that each of the two parts weighs even number of
kilos, at the same time it is not obligatory that the parts are equal. The
boys are extremely tired and want to start their meal as soon as possible,
that's why you should help them and find out, if they can divide the
watermelon in the way they want. For sure, each of them should get a part of
positive weight.
"""
def watermelon(weight):
    """ Split weight as evenly as possible and then recursively check for
    both pieces to be even."""
    assert weight > 1 and weight < 100
    if weight % 2 == 0:
        return check_both(weight / 2, weight / 2)
    else:
        heavier = (weight / 2) + 1
        lighter = weight / 2
        return check_both(heavier, lighter)

def check_both(side1, side2):
    """ Recursive helper function. Each iteration will increase the difference
    between the two sides until we reach the minimal size of 1."""
    if even(side1) and even(side2):
        return True
    elif side1 == 1:
        return False
    else:
        return check_both(side1 - 1, side2 + 1)

def even(x):
    """ Helper function to return true if a number is even. """
    return True if x % 2 == 0 else False

def test_watermelon():
    assert watermelon(8) == True
    assert watermelon(9) == False
    assert watermelon(10) == True # 4 and 6
    assert watermelon(2) == False # 1 and 1
