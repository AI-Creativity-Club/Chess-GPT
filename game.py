#https://www.pygame.org/docs/
import board
import pygame
import sys
#Length of the command lines 
argvLen = len(sys.argv)
#setup board object first.
#Choose between setting up with a hardcoded standard board of whatever size, or load from a csv file
#If there is no option selected then it will launch with default commands. AKA. the regular chess board size 8x8
if(argvLen == 3 and int(sys.argv[1]) >= 4 and int(sys.argv[2]) >= 4):
    gameBoard = board.boardxy(int(sys.argv[1]), int(sys.argv[2]))
    pygame.init()
    screen = gameBoard.setupScene()
    clock = pygame.time.Clock()
    running = True
    gameBoard.drawBoard(screen)
#If the user launches with the csv agrument then the code will launch using board.csv as the template
elif(argvLen == 2 and sys.argv[1] == 'csv'):
    csvBoard = board.boardcsv('board.csv')
    pygame.init()
    screen = csvBoard.setupScene()
    clock = pygame.time.Clock()
    running = True
    csvBoard.drawBoard(screen)
#If there are no commands specified, Regular chess board size 8x8
else:
    print("(warning) - Incorrect arguemnts or no arguements selected - launching with default commands (8x8)")
    gameBoard = board.boardxy(8, 8)
    pygame.init()
    screen = gameBoard.setupScene()
    clock = pygame.time.Clock()
    running = True
    gameBoard.drawBoard(screen)

#Main game loop, where piece logic will be implemented
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #render game / game loop - called every 60th of a second

    pygame.display.flip()

    clock.tick(60)

pygame.quit()