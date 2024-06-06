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

MAIN_MENU = False


# ------Colors--------------
TITLE_COLOR = (187, 173, 160)
MENU_BG_COLOR = (95, 92, 80)
MENU_FONT_COLOR = (255, 240, 231)
BTN_COLOR = (139, 140, 121)
BTN_OUTLINE_COLOR = (19, 20, 21)


# -------Window Settings ---------------
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Menu Rip Off for Game")


# --------Others------------------------
FONT = pg.font.SysFont("Jacquard 12", 60, bold=True)

########################################################################
# ------------------------Classes--------------------------------------#
########################################################################


########################################################################
# ------------------------Functions------------------------------------#
########################################################################


def draw_game():
    menu_btn = pg.draw.rect(WIN, BTN_COLOR, [500, 10, 260, 50], 0, 5)
    pg.draw.rect(WIN, BTN_OUTLINE_COLOR, [500, 10, 260, 50], 5, 5)
    btn_text = FONT.render("Main Menu", True, MENU_FONT_COLOR)
    WIN.blit(btn_text, (515, 15))

    if menu_btn.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
        menu = True
    else:
        menu = False

    return menu


def draw_menu():
    pg.draw.rect(WIN, MENU_FONT_COLOR, [300, 100, 300, 300])
    # exit menu button
    menu_btn = pg.draw.rect(WIN, BTN_COLOR, [315, 110, 260, 50], 0, 5)
    pg.draw.rect(WIN, BTN_OUTLINE_COLOR, [315, 110, 260, 50], 5, 5)
    btn_text = FONT.render("Exit menu", True, MENU_FONT_COLOR)
    WIN.blit(btn_text, (320, 112))

    if menu_btn.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
        menu = False
    else:
        menu = True

    return menu


########################################################################
# ---------------------------Main loop----------------------------------#
########################################################################


while run:
    WIN.fill(MENU_BG_COLOR)
    clock.tick(FPS)

    if MAIN_MENU:
        MAIN_MENU = draw_menu()

    else:
        MAIN_MENU = draw_game()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()
pg.quit()
