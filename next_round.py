def next_round(entrants, advance_point):
    """
    "Contestant who earns a score equal to or greater than the k-th place
    finisher's score will advance to the next round, as long as the
    contestant earns a positive score -- an excerpt from contest rules.

    A total of n participants took part in the contest n >= k and you
    already know their scores. Calculate how many participants will 
    advance to the next round.

    8, 5
    10, 9, 8, 7, 7, 7, 5, 5
    --> 6
    """
    # Check input parameters
    assert len(entrants) > 1 and len(entrants) < 50
    assert len(entrants) > advance_point
    # Initialize starting point
    initial_advancing_score = entrants[advance_point - 1]
    advancing_score = initial_advancing_score
    # Walk forwards or backwards through advancing point to find
    # cutoff for advancing players.
    while advancing_score == initial_advancing_score:
        if advance_point == 0:
            return [], 0
        elif advancing_score == 0:
            advance_point -= 1
            advancing_score = entrants[advance_point - 1]
        else:
            advance_point += 1
            advancing_score = entrants[advance_point - 1]
    advancing_scores = entrants[:advance_point - 1]
    return advancing_scores, len(advancing_scores)

def test_next_round():
    result1 = next_round([10, 9, 8, 7, 7, 7, 5, 5], 5)
    assert result1 == ([10, 9, 8, 7, 7, 7], 6)
    result2 = next_round([0, 0, 0, 0], 2)
    assert result2 == ([], 0)
