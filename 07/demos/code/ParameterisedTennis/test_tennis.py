import pytest

from tennis import score_tennis

#this allows you to set test perameters for the test cases that would otherwise be used. It allows the same tests to be succintly created without as much code needed

@pytest.mark.parametrize("player1_points, player2_points, expected_score",
                         [(0, 0, "Love-All"),
                          (1, 1, "Fifteen-All"),
                          (2, 2, "Thirty-All"),
                          (2, 1, "Thirty-Fifteen"),
                          (3, 1, "Forty-Fifteen"),
                          (4, 1, "Win for Player 1"),
                          (4, 3, "Advantage Player 1"),
                          (4, 5, "Advantage Player 2"),
                          ])
def test_score_tennis(player1_points, player2_points, expected_score):
    assert score_tennis(player1_points, player2_points) == expected_score
