"""
Theatre Square in the capital city of Berland has a rectangular shape with the
size n * m meters. On the occasion of the city's anniversary, a decision was
taken to pave the Square with square granite flagstones. Each flagstone is
of the size a * a

What is the least number of flagstones needed to pave the Square? It's allowed
to cover the surface larger than the Theatre Square, but the Square has to be
covered. It's not allowed to break the flagstones. The sides of flagstones
should be parallel to the sides of the Square.

Input
    The input contains three positive integer numbers in the first line:
    n, m and a (1 <= n, m, a <=109)
Output
    Write the needed number of flagstones.
"""

def theatre_square(n, m, a):
    assert n > 1 and a <= 109
    # Assume n is the larger side or swap accordingly
    if m > n:
        n, m = m, n
    # Find amount of tiles to cover n side
    n_tiles, n_remainder = n / a, n % a
    if n_remainder > 0:
        n_tiles += 1

    # If the tile width (a) is longer than m, we already have determined
    # the amount of tiles needed. Otherwise we need to cover m.
    if a >= m:
        total_tiles = n_tiles
    else:
        m_tiles, m_remainder = m / a, m % a
        if m_remainder > 0:
            m_tiles += 1
        total_tiles = m_tiles * n_tiles
    return total_tiles

    
def test_theatre_square():
    least_stones = theatre_square(6, 6, 4)
    assert least_stones == 4
    least_stones = theatre_square(4, 10, 4)
    assert least_stones == 3
