# -*- coding: utf-8 -*-
from cat.udl.tennis.Player import Player
from cat.udl.tennis.ScoreMessage import ScoreMessage


class TennisGame:
    def __init__(self):
        """self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0"""
        self.player1 = Player()
        self.player2 = Player()

    """def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1"""

    def player1WonPoint(self):
        self.player1.score.value += 1

    def player2WonPoint(self):
        self.player2.score.value += 1

    def score(self):
        result = ""
        tempScore = 0
        """if (self.p1points == self.p2points):
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")"""
        if self.areScoresEquals(self.player1, self.player2):
            result = self.playdownPhase()
        elif self.isScoreGreatterOrEqualThanFour(self.player1.score) \
                and self.isScoreGreatterOrEqualThanFour(self.player2.score):
            minusResult = self.p1points - self.p2points
            if (minusResult == 1):
                result = "Advantage " + self.player1Name
            elif (minusResult == -1):
                result = "Advantage " + self.player2Name
            elif (minusResult >= 2):
                result = "Win for " + self.player1Name
            else:
                result = "Win for " + self.player2Name
        else:
            for i in range(1, 3):
                if (i == 1):
                    tempScore = self.p1points
                else:
                    result += "-"
                    tempScore = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[tempScore]
        return result

    def areScoresEquals(self, player1, player2):
        return player1.score.value == player2.score.value

    def isScoreZero(self, score):
        return score.value == 0

    def isScoreOne(self, score):
        return score.value == 1

    def isScoreTwo(self, score):
        return score.value == 2

    def isScoreThree(self, score):
        return score.value == 3

    def isScoreGreatterOrEqualThanFour(self, score):
        return score.value >= 4

    def playdownPhase(self):
        result = ""
        if self.isScoreZero(self.player1.score):
            result = ScoreMessage.LOVE_ALL
        elif self.isScoreOne(self.player1.score):
            result = ScoreMessage.FIFTEEN_ALL
        elif self.isScoreTwo(self.player1.score):
            result = ScoreMessage.THIRTY_ALL
        else:
            result = ScoreMessage.DEUCE
        return result
