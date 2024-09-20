class MasterGame():
    def __init__(self):
        self.board = [
            [Game(), Game(), Game()],
            [Game(), Game(), Game()],
            [Game(), Game(), Game()]
        ]

        self.moveLog = []
        self.availableGames = []

        for r in self.board:
            for g in r:
                self.availableGames.append(g)

    

    def makeMove(self, move):
        g = self.board[move[0] // 3][move[1] // 3]


        if g in self.availableGames:
            r, c = move[0] % 3, move[1] % 3

            if g.isAvailable(r, c):
                g.updateTile(r, c)
                self.updateAvailableGames(self, move)

                return True # Return true if the move was successful
        
        return False # Return false is the move was unsuccessful


    def updateAvailableGames(self, move):
        r, c = move[0] % 3, move[1] % 3
        

        if self.board[r][c].getWinner() == "-":
            self.availableGames = self.board[r][c]
        else:
            self.availableGames.clear()

            for r in self.board:
                for g in r:
                    if g.getWinner() == "-":
                        self.availableGames.append(g)

class Game():
    def __init__(self):
        self.board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
    

    def isAvailable(self, r, c):
        return self.board[r][c] == "-"


    def updateTile(self, r, c, side):
        self[r][c] = side
    

    def getWinner(self):
        for r in range(3):
            if self.board[r][0] != "-" and self.board[r][0] == self.board[r][1] == self.board[r][2]:
                return self.board[r][0]
        
        for c in range(3):
            if self.board[0][c] != "-" and self.board[0][c] == self.board[1][c] == self.board[2][c]:
                return self.board[0][c]
        
        if self.board[0][0] != "-" and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[0][2] != "-" and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]


        return "-" 