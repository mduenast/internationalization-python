# -*- coding: utf-8 -*-
from cat.udl.tennis.Player import Player
from cat.udl.tennis.ScoreMessage import ScoreMessage


class TennisGame:
    def __init__(self, player1Name="player 1", player2Name="player 2"):
        """self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0"""
        self.player1 = Player(player1Name)
        self.player2 = Player(player2Name)

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
        """if (self.p1points == self.p2points):
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")"""
        if self.areScoresEquals(self.player1, self.player2):
            result = self.playdownPhase()
        elif self.isScoreGreatterOrEqualThanFour(self.player1.score) \
                or self.isScoreGreatterOrEqualThanFour(self.player2.score):
            result = self.advantagePhase()
        else:
            result = self.normalPhase()
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

    def advantagePhase(self):
        result = ""
        minusResult = self.player1.score.value - self.player2.score.value
        if (minusResult == 1):
            result = ScoreMessage.ADVANTAGE + self.player1.playerName
        elif (minusResult == -1):
            result = ScoreMessage.ADVANTAGE + self.player2.playerName
        elif (minusResult >= 2):
            result = ScoreMessage.WIN_FOR + self.player1.playerName
        else:
            result = ScoreMessage.WIN_FOR + self.player2.playerName
        return result

    def normalPhase(self):

        """ for i in range(1, 3):
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
                """
        result = "{0}-{1}".format(self.getScoreMessageByScore(self.player1),
                                  self.getScoreMessageByScore(self.player2)
                                  )
        return result

    def getScoreMessageByScore(self, player):
        result = ""
        if self.isScoreZero(player.score):
            result = ScoreMessage.LOVE
        elif self.isScoreOne(player.score):
            result = ScoreMessage.FIFTEEN
        elif self.isScoreTwo(player.score):
            result = ScoreMessage.THIRTY
        elif self.isScoreThree(player.score):
            result = ScoreMessage.FORTY
        return result

    def resetScore(self):
        self.player1.score.value = 0
        self.player2.score.value = 0
