import gettext
import os
import sys
from gettext import gettext as _

from cat.udl.tennis.tennis import TennisGame

appdir = os.path.dirname(sys.argv[0])
appdir = os.path.abspath(appdir)
localedir = os.path.join(appdir, "locales")

gettext.install('bundle', localedir, "utf-8")


class Match(object):
    def __init__(self):
        self.tennis = TennisGame()

    def main(self):
        markerPlayer = ""

        print(_("Welcome to mytennis"))
        print(_("Player 1 name :"))
        self.getPlayerName(self.tennis.player1)
        print(_("Player 2 name :"))
        self.getPlayerName(self.tennis.player2)
        while not "Win for " in self.tennis.score():
            print(_("Who scores ?") +
                  "({0}/{1})".format(self.tennis.player1.playerName,
                                     self.tennis.player2.playerName
                                     )
                  )
            markerPlayer = input()
            if markerPlayer == self.tennis.player1.playerName:
                self.tennis.player1WonPoint()
            elif markerPlayer == self.tennis.player2.playerName:
                self.tennis.player2WonPoint()
            print(self.tennis.score())
        print(_("End of match"))

    def getPlayerName(self, player):
        player.playerName = input()
        while len(player.playerName) == 0:
            player.playerName = input()


if __name__ == "__main__":
    match = Match()
    match.main()
