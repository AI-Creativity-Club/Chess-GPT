"""
pawn.py: Functionality to do with intializing the board objects.
"""
import pygame
"""
CLASS: Pawn
DESC: defines a pawn that will be draw on the scene
"""
class Pawn:
    
    
    """
    FUNC: __init__
    DESC: stores information on the sprite
    I/O: self:obj, x:int, y:int, color:tuple, sprite_path:string | N/A
    """
    def __init__(self, x, y, color, sprite_path):
        self.x = x
        self.y = y
        self.color = color
        self.sprite = pygame.image.load(sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, (60, 60))
        self.first_move = 0

    """
    FUNC: draw
    DESC: draws the sprite on the board/scene
    I/O: self:obj, x:int, y:int | N/A
    """
    def draw(self, screen):
        screen.blit(self.sprite, (self.x * 60, self.y * 60))
    """
    FUNC: move
    DESC: moves the sprite along the board state 2d array object
    I/O: self:obj, dx:int, dy:int, board_state:2d array | bool
    """
    def move(self, dx, dy, board_state):
        self.first_move += 1
        new_x = self.x + dx
        new_y = self.y + dy
        if new_x < 0 or new_x >= 8 or new_y < 0 or new_y >= 8:
            return False
        target_piece = board_state[new_y][new_x]
        if target_piece is None or target_piece.color != self.color:
            if dx == 0 and dy == (1 if self.color == "white" else -1):
                if target_piece is None:
                    board_state[self.y][self.x] = None  # Update the old square to be empty
                    self.x, self.y = new_x, new_y
                    board_state[self.y][self.x] = self  # Update the new square with the piece
                    return True
            if dx == 0 and dy == (2 if self.color == "white" else -2) and self.first_move == 1:
                board_state[self.y][self.x] = None  # Update the old square to be empty
                self.x, self.y = new_x, new_y
                board_state[self.y][self.x] = self  # Update the new square with the piece
                return True
                        
            elif abs(dx) == 1 and dy == (1 if self.color == "white" else -1):
                if target_piece is not None and target_piece.color != self.color:
                    board_state[self.y][self.x] = None  # Update the old square to be empty
                    self.x, self.y = new_x, new_y
                    board_state[self.y][self.x] = self  # Update the new square with the piece
                    return True
        return False
