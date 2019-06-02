import pygame
import random


pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# SHAPE FORMATS 2D ARRAYS

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]



class TetrisPiece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors(shape.index(shape))
        self.rotation = 0

def create_grid(locked_positions={}):
    grid = [[0,0,0] for x in range(10)] for x in range(20)]

    for r in range(len(grid)):
        for c in range(len(grid[i])):
            for(c, r) in locked_pos:
                colour = locked_pos[(c, r)]
                geid[r][c] = colour
    return grid

def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape(shapes):
    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    pass

def draw_grid(surface, grid):
    for r in range(len(grid)):
        for c in range(len(grid[c])) :
            pygame.draw.rect(surface, grid[r][c], (top_left_x + c*peice_size0, top_left_y + r*peice_size, peice_size, peice_size), 0)

    pygame.draw.rect(surface, (255,0,0), (top_left_x, top_left_y, play_width, play_height), 4)



def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface, grid):
    surface.fill((0,0,0))
    pygame.font.init()
    font = pygame.font.SysFont('calibri', 60)
    label = font.render('Python Tetris', 1, (255,255,255))

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 30))
    draw_grid(surface, grid)
    pygame.display.update()

def main():
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_shape = False
    run = True
    current_shape = get_shape()
    next_shape = get_shape()
    clock = pygame.time.clock()
    fall_time = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_shape.x -= 1
                    if not(valid_space(current_shape, grid)):
                        current_shape += 1
                if event.key == pygame.L_RIGHT:
                    current_shape.x += 1
                    if not(valid_space(current_shape, grid)):
                        current_shape -= 1
                if event.key == pygame.K_DOWN:
                    current_shape.y += 1
                if event.key == pygame.K_UP:
                    current_shape.rotation += 1


def main_menu():
    pass

main_menu()  # start game
