import pygame as pg

pg.init()
#######################################################################
# -------------------------Variables/Settins--------------------------#
#######################################################################
# -------Window------------
WIDTH, HEIGHT = 800, 800
FPS = 60

TITLE_FONT = pg.font.SysFont("Jacquard 12", 100, bold=True)
OPTIONS_FONT = pg.font.SysFont("Jacquard 12", 60, bold=True)
MENU_FONT = pg.font.SysFont("Jacquard 12", 80, bold=True)

# -------Loop-----------------
run = True
clock = pg.time.Clock()


# ------Colors--------------
TITLE_COLOR = (187, 173, 160)
BACKGROUND_COLOR = (205, 192, 180)
MENU_FONT_COLOR = (119, 110, 101)


# -------Window Settings ---------------
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("2048 Rip Off Game")


########################################################################
# ------------------------Functions------------------------------------#
########################################################################


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    text.blit(img, (x, y))


########################################################################
# ---------------------------Main loop----------------------------------#
########################################################################


def main(window):
    clock.tick(FPS)
    run = True

    while run:
        clock.tick(FPS)
        draw_text("Main Menu", TITLE_FONT, TITLE_COLOR, 160, 250)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break

    pg.quit()


if __name__ == "__main__":
    main(WIN)
