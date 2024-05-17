import pygame as pg
import random
import math

pg.init()
#######################################################################
# -------------------------Variables/Settins--------------------------#
#######################################################################
WIDTH, HEIGHT = 800, 800
FPS = 60
ROWS = 4
COLS = 4
RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS


FONT = pg.font.SysFont("Jacquard 12", 60, bold=True)

run = True
clock = pg.time.Clock()

# -----Colors--------------
OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)


# -----Window Settings ---------------
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("2048 Game")


########################################################################
# ------------------------Classes/Functions-----------------------------#
########################################################################


########################################################################
# ---------------------------Main loop----------------------------------#
########################################################################


def main(win):
    clock.tick(FPS)
    run = True

    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
    pg.quit()


if __name__ == "__main__":
    main(WIN)
