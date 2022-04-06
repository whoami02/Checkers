import pygame
from minimax.algo import minimax
from checkers.constants import BLACK, SQUARE_SIZE, WHITE, WIDTH, HEIGHT
from checkers.board import Board
from checkers.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_pos_Mouse(pos):
    x,y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row, col 

def main():
    run = True
    clock = pygame.time.Clock()
    # board = Board()
    game = Game(WIN)
 
    # piece = board.get_piece(0,1)
    # board.move(piece, 4, 3)

    while(run):
        clock.tick(60)


        if game.winner() != None:
            print(game.winner())

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_Mouse(pos)
                # piece = board.get_piece(row, col) 
                # board.move(piece, 4, 3)
                # if game.turn == BLACK:
                game.select(row, col)
        game.update()
        # board.draw(WIN)
        # pygame.display.update()

    pygame.quit()

main()