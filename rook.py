import pygame

class Rook:
    def __init__(self, x, y, color, sprite_path):
        self.x = x
        self.y = y
        self.color = color
        self.sprite = pygame.image.load(sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, (60, 60))
    
    def draw(self, screen):
        screen.blit(self.sprite, (self.x * 60, self.y * 60))

    def move(self, dx, dy, board_state):
        return False