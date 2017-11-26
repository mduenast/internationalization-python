# -*- coding: utf-8 -*-

import pytest

from cat.udl.tennis.tennis import TennisGame
from cat.udl.tennis.tennis_unittest import test_cases, play_game


class TestTennis:
    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_game(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(TennisGame, p1Points, p2Points, p1Name, p2Name)
        print(score)
        assert score == game.score()
        game.resetScore()
