from cat.udl.tennis.tennis import TennisGame


class Match(object):
    def __init__(self):
        self.tennis = TennisGame()
    def main(self):
        markerPlayer = ""

        print("Welcome to mytennis")
        print("Player 1 name :")
        self.getPlayerName(self.tennis.player1)
        print("Player 2 name :")
        self.getPlayerName(self.tennis.player2)
        while not "Win for " in self.tennis.score():
            print("Who scores ?" +
                  "{0}/{1}".format(self.tennis.player1.playerName,
                                   self.tennis.player2.playerName
                                   )
                  )
            markerPlayer = input()
            if markerPlayer == self.tennis.player1.playerName:
                self.tennis.player1WonPoint()
            elif markerPlayer == self.tennis.player2.playerName:
                self.tennis.player2WonPoint()
            print(self.tennis.score())
        print("End of match")


    def getPlayerName(self,player):
        player.playerName = input()
        while len(player.playerName) == 0:
            player.playerName = input()

if __name__ == "__main__":
    match = Match()
    match.main()