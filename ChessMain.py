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