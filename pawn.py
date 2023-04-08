import pygame
import csv

class Pawn:
    def __init__(self, x, y, color, sprite_path):
        self.x = x
        self.y = y
        self.color = color
        self.sprite = pygame.image.load(sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, (60, 60))

    def draw(self, screen):
        screen.blit(self.sprite, (self.x * 60, self.y * 60))

    def move(self, dx, dy, board_state):
        new_x = self.x + dx
        new_y = self.y + dy
        if new_x < 0 or new_x >= 8 or new_y < 0 or new_y >= 8:
            return False

        target_piece = board_state[new_y][new_x]
        if target_piece is None or target_piece.color != self.color:
            if dx == 0 and dy == (1 if self.color == "white" else -1):
                if target_piece is None:
                    self.x, self.y = new_x, new_y
                    return True
            elif abs(dx) == 1 and dy == (1 if self.color == "white" else -1):
                if target_piece is not None and target_piece.color != self.color:
                    self.x, self.y = new_x, new_y
                    return True

        return False
