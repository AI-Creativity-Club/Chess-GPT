"""
Chess-GPT. Created by the contributors of the OSU AICC GitHub Org.
MAIN FILE: game.py
EXTERNAL FILES: board.py, pawn.py, genboard.py

**IF YOU'RE PUSHING TO MAIN PLEASE UPDATE HEADER COMMENT(S) IF INFORMATION CHANGES.
(To make the code easier to read and to better understand the outputs and what we write, 
comments are to be made under the assumption that each variable has a "type". Even if it's not the case.)
"""
#IMPORTED LIBRARIES & EXTERNAL FILES
import sys
import pygame
from board import boardxy, boardcsv
from pawn import Pawn

"""
FUNC: intialize_board
DISC: Initialize the board state with pawns. 
IO: board_size:int | board_state:2d array
"""
def initialize_board(board_size):
    board_state = [[None for _ in range(board_size)] for _ in range(board_size)]

    # Add white pawns
    for x in range(board_size):
        board_state[1][x] = Pawn(x, 1, "white", "pawnwhite60x60.png")

    # Add black pawns
    for x in range(board_size):
        board_state[board_size - 2][x] = Pawn(x, board_size - 2, "black", "pawnblack60x60.png")

    return board_state

"""
FUNC: draw_pieces
DISC: Draw all the pieces on the board
IO: screen:obj | board_state:2d array
"""
def draw_pieces(screen, board_state):
    for row in board_state:
        for piece in row:
            if piece is not None:
                piece.draw(screen)
"""
FUNC: draw_turn_indicator
DISC: Draws which players turn it is using a text element.
IO: screen:obj , current_turn:string| NA
"""
def draw_turn_indicator(screen, current_turn):
    font = pygame.font.Font(None, 24)
    text = font.render("Turn: " + current_turn.capitalize(), True, (255, 255, 255))
    screen.blit(text, (10, 10))
"""
** MAIN GAME LOOP FUNCION
FUNC: main
DISC: contains primary game loop and initializes elements of the game.
IO: NA | NA
"""
def main():
    argvLen = len(sys.argv)
    if argvLen == 3 and int(sys.argv[1]) >= 4 and int(sys.argv[2]) >= 4:
        board_size = int(sys.argv[1])
        gameBoard = boardxy(board_size, board_size)
    elif argvLen == 2 and sys.argv[1] == 'csv':
        gameBoard = boardcsv('board.csv')
        board_size = gameBoard.x
    else:
        print("(warning) - Incorrect arguments or no arguments selected - launching with default commands (8x8)")
        board_size = 8
        gameBoard = boardxy(board_size, board_size)

    #Scene elements are initialized as board objects set up, gets game clock runnning
    pygame.init()
    screen = gameBoard.setupScene()
    clock = pygame.time.Clock()
    running = True
    gameBoard.drawBoard(screen)

    #Visual elements are next to be set up. Draw pieces and sets up the board_state array
    board_state = initialize_board(board_size)
    draw_pieces(screen, board_state)

    #The while loop is the game loop and is where the logic is stored.
    selected_piece = None
    current_turn = "white" #white goes first
    draw_turn_indicator(screen, current_turn)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #Gets the position of the mouse at the current press and selects the given piece
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                grid_x, grid_y = x // 60, y // 60 #60 being the size of each square on the board
                if selected_piece is None:
                    piece = board_state[grid_y][grid_x]
                    if piece is not None and piece.color == current_turn:
                        selected_piece = piece
                else:
                    dx = grid_x - selected_piece.x
                    dy = grid_y - selected_piece.y
                    if selected_piece.move(dx, dy, board_state):
                        # Capture the piece if present
                        if board_state[grid_y][grid_x] is not None and board_state[grid_y][grid_x].color != selected_piece.color:
                            board_state[grid_y][grid_x] = None
                        board_state[selected_piece.y][selected_piece.x] = None
                        board_state[grid_y][grid_x] = selected_piece
                        #Draws the updated scene after the piece has been captured
                        gameBoard.drawBoard(screen)
                        draw_pieces(screen, board_state)
                        draw_turn_indicator(screen, current_turn)

                        # Switch turns
                        current_turn = "black" if current_turn == "white" else "white"

                    selected_piece = None

        #Swaps the buffers, and compute time between swaps. In this case every 60th of a second
        pygame.display.flip()
        clock.tick(60) # ~60fps

        gameBoard.drawBoard(screen)
        draw_pieces(screen, board_state)
        draw_turn_indicator(screen, current_turn)

    pygame.quit()

if __name__ == "__main__":
    main()