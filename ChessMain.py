"""
This is our main driver file. It will be responsible for handling user input and displaying the current GameState object.
"""

import pygame
import ChessEngine

# CONSTANTS
WIDTH = HEIGHT = 512
DIMENSION = 8 # board size is 8x8
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # important for animations later on
IMAGES = {}

"""
Initialize a global dictionary of images. This will be called exactly once in main
"""
def load_images():
    pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]

    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))
    # NOTE: we can access an image by saying 'IMAGES["wP"]'