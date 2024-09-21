'''
Ultimate Tic Tac Toe is a version of Tic Tac Toe showcased by VSauce each tile has its own separate Tic Tac Toe game
and when you choose a box. The next player must choose a move in the game that corresponds to the move. When a player
wins one of the games, that game turns into an X or O depending on the player's side.
'''

import pygame as p
import ticTacToe


LENGTH = 720
IMAGES = {}


def main():
    IMAGES["so"] = p.transform.scale(p.image.load("images/O.png"), (LENGTH//9,LENGTH//9))
    IMAGES["sx"] = p.transform.scale(p.image.load("images/X.png"), (LENGTH//9,LENGTH//9))
    IMAGES["bo"] = p.transform.scale(p.image.load("images/O.png"), (LENGTH//3,LENGTH//3))
    IMAGES["bx"] = p.transform.scale(p.image.load("images/X.png"), (LENGTH//3,LENGTH//3))


    p.init()
    screen = p.display.set_mode((LENGTH, LENGTH))
    p.display.set_caption("Ultimate Tic-Tac-Toe")
    clock = p.time.Clock()
    mg = ticTacToe.MasterGame()

    while True:
        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                break
            elif e.type == p.MOUSEBUTTONDOWN:
                mouse_pos = p.mouse.get_pos()
                pos = (mouse_pos[1] // (LENGTH // 9), mouse_pos[0] // (LENGTH // 9))
                mg.makeMove(pos)
            elif e.type == p.KEYDOWN:
                if e.key == p.K_SPACE:
                    mg.undoMove()
                elif e.key == p.K_BACKSPACE:
                    mg.reset()

        drawBoard(screen, mg)
        p.display.flip()
        clock.tick(15)


def drawBoard(screen, mg):
    colors = ["gray70", "gray80"]

    for x in range(9):
        for y in range(9):
            surface = p.Surface((LENGTH // 9, LENGTH // 9))
            surface.fill(colors[(x+y) % 2])
            screen.blit(surface,(x * LENGTH // 9,y * LENGTH // 9))
    

    highlightSquares(screen, mg)
    drawXOs(screen, mg)

    # Draw lines on the screen
    drawLine(screen, 0, LENGTH//3 - 1 , LENGTH, 2)
    drawLine(screen, 0, 2*LENGTH//3 - 1, LENGTH, 2)
    drawLine(screen, LENGTH//3 - 1, 0, 2, LENGTH)
    drawLine(screen, 2*LENGTH//3 - 1, 0, 2, LENGTH)



def drawLine(screen, x, y, w, h):
    surface = p.Surface((w, h))
    surface.fill("black")
    screen.blit(surface,(x, y))


def drawXOs(screen, mg):
    for r in range(3):
        for c in range(3):
            g = mg.board[r][c]

            for r2 in range(3):
                for c2 in range(3):
                    tile = g.board[r2][c2]

                    if tile == "x":
                        screen.blit(IMAGES["sx"], (c*LENGTH//3 + c2*LENGTH//9, r*LENGTH//3 + r2*LENGTH//9))
                    elif tile == "o":
                        screen.blit(IMAGES["so"], (c*LENGTH//3 + c2*LENGTH//9, r*LENGTH//3 + r2*LENGTH//9))

            if g.winner == "x":
                s = p.Surface((LENGTH//3, LENGTH//3))
                s.fill("black")
                s.set_alpha(150)
                screen.blit(s, (c*LENGTH//3, r*LENGTH//3))
                screen.blit(IMAGES["bx"], (c*LENGTH//3, r*LENGTH//3))
            elif g.winner == "o":
                s = p.Surface((LENGTH//3, LENGTH//3))
                s.fill("black")
                s.set_alpha(150)
                screen.blit(s, (c*LENGTH//3, r*LENGTH//3))
                screen.blit(IMAGES["bo"], (c*LENGTH//3, r*LENGTH//3))




def highlightSquares(screen, mg):
    for coord in mg.availableGames:
        r, c = coord[0], coord[1]
        
        surface = p.Surface((LENGTH // 3, LENGTH // 3))
        surface.fill("purple")
        surface.set_alpha(100)
        screen.blit(surface,(c* LENGTH //3,r * LENGTH // 3))



if __name__ == "__main__":
    main()