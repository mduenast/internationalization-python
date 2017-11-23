# -*- coding: utf-8 -*-

import pytest
from cat.udl.tennis.tennis import TennisGame1, TennisGame2, TennisGame3

from cat.udl.tennis.tennis_unittest import test_cases, play_game

class TestTennis:

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_game1(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(TennisGame1, p1Points, p2Points, p1Name, p2Name)
        assert score == game.score()

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_game2(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(TennisGame2, p1Points, p2Points, p1Name, p2Name)
        assert score == game.score()

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_game3(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(TennisGame3, p1Points, p2Points, p1Name, p2Name)
        assert score == game.score()