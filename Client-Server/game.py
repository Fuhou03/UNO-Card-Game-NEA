class Game:
    def __init__(self, id):
        self.p1Went = False  # If they made a move yet
        self.p2Went = False
        self.ready = False
        self.id = id  # Each game we make has it's own id so we know which client is part of which game
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

    def get_player_move(self, p):
        ''' p in range [0,1] and move is returned '''
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move

        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):  # If two players are connected to a game
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):  # Called after both players performed a move and sees who won
        p1 = self.moves[0].upper()[0]  # Get the first letter of the move (R, S, P)
        p2 = self.moves[1].upper()[0]

        # winner = -1 # Tie
        # winner = 0 # P1 winner
        # winner = 1 # P1 winner
        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
