class MasterGame():
    pass

class Game():
    def __init__(self):
        self.board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
    

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
            return self.board[0,0]
        elif self.board[0][2] != "-" and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0,2]