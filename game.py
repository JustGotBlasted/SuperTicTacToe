'''
Ultimate Tic Tac Toe is a version of Tic Tac Toe showcased by VSauce each tile has its own separate Tic Tac Toe game
and when you choose a box. The next player must choose a move in the game that corresponds to the move. When a player
wins one of the games, that game turns into an X or O depending on the player's side.
'''

import pygame as p
import ticTacToe


LENGTH = 900


def main():
    p.init()
    screen = p.display.set_mode((LENGTH, LENGTH))
    p.display.set_caption("Ultimate Tic-Tac-Toe")
    clock = p.time.Clock()

    while True:
        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                break
            elif e.type == p.MOUSEBUTTONDOWN:
                mouse_pos = p.mouse.get_pos()
                pos = (mouse_pos[0] // (LENGTH // 9), mouse_pos[1] // (LENGTH // 9))
                print(pos)

    
        drawBoard(screen)
        p.display.update()
        clock.tick(15)


def drawBoard(screen):
    colors = ["gray60", "gray80"]

    for x in range(9):
        for y in range(9):
            surface = p.Surface((LENGTH // 9, LENGTH // 9))
            surface.fill(colors[(x+y) % 2])
            screen.blit(surface,(x * LENGTH // 9,y * LENGTH // 9))
    
    
    # Draw lines on the screen
    drawLine(screen, 0, LENGTH//3, LENGTH, 5)
    drawLine(screen, 0, 2*LENGTH//3, LENGTH, 5)
    drawLine(screen, LENGTH//3, 0, 5, LENGTH)
    drawLine(screen, 2*LENGTH//3, 0, 5, LENGTH)


def drawLine(screen, x, y, w, h):
    surface = p.Surface((w, h))
    surface.fill("black")
    screen.blit(surface,(x, y))


if __name__ == "__main__":
    main()