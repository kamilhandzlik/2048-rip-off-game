import pygame as pg
import random
import math

pg.init()
#######################################################################
# -------------------------Variables/Settins--------------------------#
#######################################################################
# -------Window------------
WIDTH, HEIGHT = 800, 800
FPS = 60
ROWS = 4
COLS = 4
RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS


FONT = pg.font.SysFont("Jacquard 12", 60, bold=True)

# -------Loop-----------------
run = True
clock = pg.time.Clock()

# ------Colors--------------
OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)


# -------Window Settings ---------------
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("2048 Rip Off Game")


########################################################################
# ------------------------Classes--------------------------------------#
########################################################################
class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]

    def __init__(self, value, row, col) -> None:
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT


########################################################################
# ------------------------Functions------------------------------------#
########################################################################


def draw_grid(window):
    for row in range(1, ROWS):
        y = row * RECT_HEIGHT
        pg.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)

    for col in range(1, COLS):
        x = col * RECT_WIDTH
        pg.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

    pg.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)


def draw(window):
    window.fill(BACKGROUND_COLOR)
    draw_grid(window)
    pg.display.update()


########################################################################
# ---------------------------Main loop----------------------------------#
########################################################################


def main(window):
    clock.tick(FPS)
    run = True

    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
        draw(window)
    pg.quit()


if __name__ == "__main__":
    main(WIN)
