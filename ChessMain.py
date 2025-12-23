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

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    gamestate = ChessEngine.GameState()
    load_images() # only call once

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_gamestate(screen, gamestate)

        clock.tick(MAX_FPS)
        pygame.display.flip()

"""
Responsible for all the graphics within a current gamestate
"""
def draw_gamestate(screen, gamestate):
    draw_board(screen) # draws squares onto the board
    # add piece highlighting and move suggestions (later)
    draw_pieces(screen, gamestate.board) # draws pieces ontop of those squares

"""
Draw the squares on the board. Top left is always light
"""
def draw_board(screen):
    colours = ["white", "grey"]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            colour = colours[(row + col) % 2]
            pygame.draw.rect(screen, colour, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

"""
Draw the pieces on the board using the current GameState.board
"""
def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--": # not empty square
                screen.blit(IMAGES[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

if __name__ == "__main__":
    main()