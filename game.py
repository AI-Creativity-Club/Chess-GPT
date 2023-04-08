import sys
import pygame
from board import boardxy, boardcsv
from pawn import Pawn

# Initialize the board state with pawns
def initialize_board():
    board_state = [[None for _ in range(8)] for _ in range(8)]

    # Add white pawns
    for x in range(8):
        board_state[1][x] = Pawn(x, 1, "white", "pawnwhite60x60.png")

    # Add black pawns
    for x in range(8):
        board_state[6][x] = Pawn(x, 6, "black", "pawnblack60x60.png")

    return board_state

# Draw all the pieces on the board
def draw_pieces(screen, board_state):
    for row in board_state:
        for piece in row:
            if piece is not None:
                piece.draw(screen)

def main():
    argvLen = len(sys.argv)
    if argvLen == 3 and int(sys.argv[1]) >= 4 and int(sys.argv[2]) >= 4:
        gameBoard = boardxy(int(sys.argv[1]), int(sys.argv[2]))
    elif argvLen == 2 and sys.argv[1] == 'csv':
        gameBoard = boardcsv('board.csv')
    else:
        print("(warning) - Incorrect arguments or no arguments selected - launching with default commands (8x8)")
        gameBoard = boardxy(8, 8)

    pygame.init()
    screen = gameBoard.setupScene()
    clock = pygame.time.Clock()
    running = True
    gameBoard.drawBoard(screen)

    board_state = initialize_board()
    draw_pieces(screen, board_state)

    selected_piece = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                grid_x, grid_y = x // 60, y // 60

                if selected_piece is None:
                    piece = board_state[grid_y][grid_x]
                    if piece is not None:
                        selected_piece = piece
                else:
                    dx = grid_x - selected_piece.x
                    dy = grid_y - selected_piece.y
                    if selected_piece.move(dx, dy, board_state):
                        # Capture the piece if present
                        if board_state[grid_y][grid_x] is not None:
                            board_state[grid_y][grid_x] = None
                        board_state[selected_piece.y][selected_piece.x] = None
                        board_state[grid_y][grid_x] = selected_piece

                        gameBoard.drawBoard(screen)
                        draw_pieces(screen, board_state)

                    selected_piece = None

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
