from cat.udl.tennis.Score import Score


class Player(object):
    def __init__(self, playerName=""):
        self.playerName = playerName
        self.score = Score()
