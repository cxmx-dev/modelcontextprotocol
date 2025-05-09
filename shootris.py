# shootris.py - Tetris clone with shooting mechanics

import pygame
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # I
    (255, 165, 0),  # L
    (0, 0, 255),    # J
    (255, 255, 0),  # O
    (128, 0, 128),  # T
    (255, 0, 0),    # Z
    (0, 255, 0)     # S
]

# Tetromino Shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0], [1, 0], [1, 1]],  # L
    [[0, 1], [0, 1], [1, 1]],  # J
    [[1, 1], [1, 1]],           # O
    [[1, 1, 1], [0, 1, 0]],     # T
    [[1, 1, 0], [0, 1, 1]],     # Z
    [[0, 1, 1], [1, 1, 0]]      # S
]

class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = COLORS[SHAPES.index(shape)]

class Projectile:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.active = True

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.projectiles = []
        self.score = 0

    def new_piece(self):
        shape = random.choice(SHAPES)
        return Tetromino(GRID_WIDTH // 2 - len(shape[0]) // 2, 0, shape)

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, COLORS[self.grid[y][x] - 1],
                                    (x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE-1, GRID_SIZE-1))

    def collision_check(self, piece, dx=0, dy=0):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = piece.x + x + dx
                    new_y = piece.y + y + dy
                    if (new_x < 0 or new_x >= GRID_WIDTH or
                        new_y >= GRID_HEIGHT or
                        (new_y >= 0 and self.grid[new_y][new_x])):
                        return True
        return False

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                target_x, target_y = pygame.mouse.get_pos()
                self.projectiles.append(Projectile(
                    GRID_WIDTH//2 * GRID_SIZE,
                    GRID_HEIGHT * GRID_SIZE,
                    target_x,
                    target_y
                ))

    def update(self):
        # Game update logic here
        pass

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid()
        # Draw projectiles
        for p in self.projectiles:
            if p.active:
                pygame.draw.circle(self.screen, WHITE, (p.x, p.y), 5)
        pygame.display.update()

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
