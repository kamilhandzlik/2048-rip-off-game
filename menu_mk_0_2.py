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
MENU_COMMAND = 0

########################################################################
# ------------------------Classes--------------------------------------#
########################################################################


class Buttons:
    def __init__(self, txt, pos) -> None:
        self.txt = txt
        self.pos = pos
        self.button = pg.rect.Rect((self.pos[0], self.pos[1]), (260, 50))

    def draw(self):
        pg.draw.rect(WIN, BTN_COLOR, self.button, 0, 5)
        pg.draw.rect(WIN, BTN_OUTLINE_COLOR, self.button, 5, 5)
        btn_text = FONT.render(self.txt, True, MENU_FONT_COLOR)
        WIN.blit(btn_text, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            return True
        else:
            return False


########################################################################
# ------------------------Functions------------------------------------#
########################################################################


def draw_game():
    button = Buttons("Main menu", (500, 10))
    button.draw()
    return button.check_clicked()


def draw_menu():
    command = 0
    run = True

    pg.draw.rect(WIN, MENU_FONT_COLOR, [300, 100, 300, 310])
    # exit menu button
    menu_btn = Buttons("Exit Menu", [315, 110])
    btn_1 = Buttons("Restart", [315, 170])
    btn_2 = Buttons("Continue", [315, 230])
    btn_3 = Buttons("Settings", [315, 290])
    btn_4 = Buttons("Quit Game", [315, 350])
    menu_btn.draw()
    btn_1.draw()
    btn_2.draw()
    btn_3.draw()
    btn_4.draw()

    if menu_btn.check_clicked():
        command = 1
    if btn_1.check_clicked():
        command = 2
    if btn_2.check_clicked():
        command = 3
    if btn_3.check_clicked():
        command = 4
    if btn_4.check_clicked():
        command = 5
    return command


########################################################################
# ---------------------------Main loop----------------------------------#
########################################################################


while run:
    WIN.fill(MENU_BG_COLOR)
    clock.tick(FPS)

    if MAIN_MENU:
        MENU_COMMAND = draw_menu()
        if MENU_COMMAND > 0:
            MAIN_MENU = False
            if MENU_COMMAND == 5:
                run = False

    else:
        MAIN_MENU = draw_game()
        if MENU_COMMAND > 1:
            text = FONT.render(
                f"Button { MENU_COMMAND - 1} was clicked!", True, "black"
            )
            WIN.blit(text, (100, 200))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()
pg.quit()
