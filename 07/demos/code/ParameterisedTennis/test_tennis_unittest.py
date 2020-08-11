import unittest

from tennis import score_tennis


class TennisTest(unittest.TestCase):

    def test_score_tennis(self):
        test_cases = [
            (0, 0, "Love-All"),
            (1, 1, "Fifteen-All"),
            (2, 2, "Thirty-All"),
            (2, 1, "Thirty-Fifteen"),
            (3, 1, "Forty-Fifteen"),
            (4, 1, "Win for Player 1"),
        ]
        for player1_points, player2_points, expected_score in test_cases:
            with self.subTest(f"{player1_points}, {player2_points} -> {expected_score}"):
                self.assertEqual(expected_score, score_tennis(player1_points, player2_points))

#we will loop over the test cases to pass to the assertion to check them. We will have these listed as seperate test cases, meaning its still possible for individual tests to fail while allowing the others to execute. This allows for a shortened version of testing.
# We can use coverage to generate HTML data to view in browser for a breakdown of the python files available, and to view the specific coverage for a given result. This same thing can be achieved with pytest, where yuo would call cov-report and denote where to list the html file and from where it is pulling that information.
