import pygame
import csv
#board generation
regular = False

#width and height for cube chess piece spot. 
brwidth = 60;
brheight = 60;

#hard coded colors
BLACK = (0, 0, 0)
FWHITE = (227, 208, 184)
WHITE = (255, 255, 255)

class boardxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def drawBoard(self, screen):
        #defines current color to be used for the chess board
        CURRCOLOR = FWHITE
        positionX = 0
        positionY = 0
        for x in range(0, self.x):
            positionY = 0
            if(x % 2 != 0):
                CURRCOLOR = BLACK
            else:
                CURRCOLOR = FWHITE
            for y in range(0, self.y):
                pygame.draw.rect(screen, CURRCOLOR, (positionX, positionY, brwidth, brheight))
                positionY += 60
                if(CURRCOLOR == BLACK):
                    CURRCOLOR = FWHITE
                else:
                    CURRCOLOR = BLACK
            positionX += 60
    
    def setupScene(self):
        return pygame.display.set_mode((brwidth * self.x, brheight * self.y))


class boardcsv:
    def __init__(self, csvName):
        self.x = 0
        self.y = 0
        #For some reason it really doesn't like the self.csvfile being iterated here. I made a new csv file to read.
        try:
            self.csvfile = open(csvName, newline='')
        except FileNotFoundError:
            print("(error) - No csv file detected named \"board.csv\"")
            quit()
        csvfileNum = open(csvName, newline='')
        self.reader = csv.reader(self.csvfile, delimiter=',', quotechar='|')
        readerNum = csv.reader(csvfileNum, delimiter=',', quotechar='|')
        for x in readerNum:
            self.x += 1
            self.y += 1


    def drawBoard(self, screen):
        positionX = 0
        positionY = 0
        for row in self.reader:
            for x in row:
                match x:
                    case 'x':
                        pygame.draw.rect(screen, WHITE, (positionX, positionY, brwidth, brheight))
                    case '1':
                        pygame.draw.rect(screen, FWHITE, (positionX, positionY, brwidth, brheight))
                    case '0':
                        pygame.draw.rect(screen, BLACK, (positionX, positionY, brwidth, brheight))
                positionX += 60
            
            positionX = 0
            positionY += 60
        
        self.csvfile.close()
    
    def setupScene(self):
        return pygame.display.set_mode((brwidth * self.x, brheight * self.y))