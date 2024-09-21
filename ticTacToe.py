class MasterGame():
    def __init__(self):
        self.board = [
            [Game(), Game(), Game()],
            [Game(), Game(), Game()],
            [Game(), Game(), Game()]
        ]

        self.oTurn = True
        self.winner = "-"
        self.moveLog = []
        self.availableGames = [] # Provides a list of tuples that represent the coordinates of games that are available
        self.availableGamesLog = []

        for r in range(3):
            for c in range(3):
                self.availableGames.append((r, c))

    

    def makeMove(self, move):
        g = self.board[move[0] // 3][move[1] // 3]
        

        if (move[0] // 3, move[1] // 3) in self.availableGames:
            r, c = move[0] % 3, move[1] % 3

            if g.isAvailable(r, c):
                side = "o" if self.oTurn else "x"
                g.updateTile(r, c, side)
                g.updateWinner()

                self.updateWinner()
                self.updateAvailableGames(move)

                self.moveLog.append(move)
                self.availableGamesLog.append(self.availableGames)

                self.oTurn = not self.oTurn

                return True # Return true if the move was successful
        
        return False # Return false is the move was unsuccessful


    def undoMove(self):
        if len(self.moveLog) > 0:
            move = self.moveLog[-1]
            g = self.board[move[0] // 3][move[1] // 3]
            g.updateTile(move[0] % 3, move[1] % 3, "-")
            g.updateWinner()

            self.oTurn = not self.oTurn
            self.updateWinner()
            self.moveLog.pop()
            self.availableGamesLog.pop()


            if len(self.availableGamesLog) > 0:
                self.availableGames = self.availableGamesLog[-1]
            else:
                self.availableGames.clear()

                for r in range(3):
                    for c in range(3):
                        self.availableGames.append((r, c))

    
    def reset(self):
        self.__init__()


    def updateAvailableGames(self, move):
        if self.winner != "-":
            self.availableGames.clear()
            return


        r, c = move[0] % 3, move[1] % 3
    

        if self.board[r][c].winner == "-":
            self.availableGames = [(r, c)]
        else:
            self.availableGames = []
            
            for r in range(3):
                for c in range(3):
                    g = self.board[r][c]

                    if g.winner == "-":
                        self.availableGames.append((r, c))
    

    def updateWinner(self):
        b = self.board
        g = Game()
        g.board = [
            [b[0][0].winner, b[0][1].winner, b[0][2].winner],
            [b[1][0].winner, b[1][1].winner, b[1][2].winner],
            [b[2][0].winner, b[2][1].winner, b[2][2].winner]
        ]

        g.updateWinner()
        self.winner = g.winner


        

class Game():
    def __init__(self):
        self.board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]

        self.winner = "-"
    

    def isAvailable(self, r, c):
        return self.board[r][c] == "-"


    def updateTile(self, r, c, side):
        self.board[r][c] = side
    

    def updateWinner(self):
        for r in range(3):
            if self.board[r][0] != "-" and self.board[r][0] == self.board[r][1] == self.board[r][2]:
                self.winner = self.board[r][0]
                return
        
        for c in range(3):
            if self.board[0][c] != "-" and self.board[0][c] == self.board[1][c] == self.board[2][c]:
                self.winner = self.board[0][c]
                return
        
        if self.board[0][0] != "-" and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.winner = self.board[0][0]
            return
        elif self.board[0][2] != "-" and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            self.winner = self.board[0][2]
            return


        self.winner = "-"