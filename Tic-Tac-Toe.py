import pygame

# intiating module
pygame.init()

# configuring window size
win = pygame.display.set_mode((550, 550))

# setting window color
win.fill((255, 255, 255))

# window title
pygame.display.set_caption("Tic-Tac-Toe")

# first row
f1 = pygame.draw.rect(win, (0, 0, 0), (25, 25, 150, 150))
s1 = pygame.draw.rect(win, (0, 0, 0), (200, 25, 150, 150))
t1 = pygame.draw.rect(win, (0, 0, 0), (375, 25, 150, 150))

# second row
f2 = pygame.draw.rect(win, (0, 0, 0), (25, 200, 150, 150))
s2 = pygame.draw.rect(win, (0, 0, 0), (200, 200, 150, 150))
t2 = pygame.draw.rect(win, (0, 0, 0), (375, 200, 150, 150))

# third row
f3 = pygame.draw.rect(win, (0, 0, 0), (25, 375, 150, 150))
s3 = pygame.draw.rect(win, (0, 0, 0), (200, 375, 150, 150))
t3 = pygame.draw.rect(win, (0, 0, 0), (375, 375, 150, 150))

# variable to be able to run game
run = True

# variable to know which player turn
player = 1
# variable to know if the game end with tie
click = 0

# bools for checking if boxes are empty
f1_empty = True
s1_empty = True
t1_empty = True
f2_empty = True
s2_empty = True
t2_empty = True
f3_empty = True
s3_empty = True
t3_empty = True

ar = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

game = 0


def winner_1():
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    black = (0, 0, 0)
    a = 400
    b = 400
    display_surface = pygame.display.set_mode((a, b))
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Player 1 is the winner', True, yellow, black)
    textrect = text.get_rect()
    textrect.center = (a // 2, b // 2)
    display_surface.fill(white)
    display_surface.blit(text, textrect)


def winner_2():
    whitee = (255, 255, 255)
    red = (255, 0, 0)
    blackk = (0, 0, 0)
    m = 400
    n = 400
    surface_display = pygame.display.set_mode((m, n))
    fontt = pygame.font.Font('freesansbold.ttf', 32)
    textt = fontt.render('Player 2 is the winner', True, red, blackk)
    recttext = textt.get_rect()
    recttext.center = (m // 2, n // 2)
    surface_display.fill(whitee)
    surface_display.blit(textt, recttext)


def tie():
    whiteee = (255, 255, 255)
    green = (0, 255, 0)
    blackkk = (0, 0, 0)
    e = 400
    f = 400
    surfacedisplay = pygame.display.set_mode((e, f))
    fonttt = pygame.font.Font('freesansbold.ttf', 30)
    texttt = fonttt.render('No winners, play again', True, green, blackkk)
    rectttext = texttt.get_rect()
    rectttext.center = (e // 2, f // 2)
    surfacedisplay.fill(whiteee)
    surfacedisplay.blit(texttt, rectttext)


def is_wining():
    for x in range(3):
        winner = 0
        for y in range(3):
            winner = winner + ar[x - 1][y - 1]
            if winner == 3:
                winner_1()
            elif winner == -3:
                winner_2()
    for x in range(3):
        winner = 0
        for y in range(3):
            winner = winner + ar[y - 1][x - 1]
            if winner == 3:
                winner_1()
            elif winner == -3:
                winner_2()
    d = 0
    for x in range(3):
        d = d + ar[x - 1][x - 1]
        if d == 3:
            winner_1()
        elif d == -3:
            winner_2()
    d = 0
    y = 2
    xp = 0
    for x in range(3):
        d = d + ar[xp][y]
        xp += 1
        y -= 1
        if d == 3:
            winner_1()
        elif d == -3:
            winner_2()
    if click == 9:
        tie()


def insert():
    global run, f1_empty, click, player, s1_empty, t1_empty, f2_empty, s2_empty, t2_empty, f3_empty, s3_empty, t3_empty
    # wait time at the start of each loop to prevent overlapping 1 second
    pygame.time.delay(100)
    # loop to  check for mouse click or closing window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            # getting position of mouse when clicked
            pos = pygame.mouse.get_pos()
            # checking if mouse clicked an empty to box to add something to it and then changing player turn
            if f1.collidepoint(pos) and f1_empty is True:
                click = click + 1
                if player == 1:
                    pygame.draw.line(win, (255, 255, 0), (50, 50), (150, 150), 10)
                    pygame.draw.line(win, (255, 255, 0), (50, 150), (150, 50), 10)
                    player = 2
                    f1_empty = False
                    ar[0][0] = 1
                else:
                    pygame.draw.circle(win, (255, 0, 0), (100, 100), 60)
                    pygame.draw.circle(win, (0, 0, 0), (100, 100), 55)
                    player = 1
                    f1_empty = False
                    ar[0][0] = -1

            if s1.collidepoint(pos) and s1_empty is True:
                click = click + 1
                if player == 1:
                    pygame.draw.line(win, (255, 255, 0), (225, 50), (325, 150), 10)
                    pygame.draw.line(win, (255, 255, 0), (225, 150), (325, 50), 10)
                    player = 2
                    s1_empty = False
                    ar[0][1] = 1
                else:
                    player = 1
                    pygame.draw.circle(win, (255, 0, 0), (275, 100), 60)
                    pygame.draw.circle(win, (0, 0, 0), (275, 100), 55)
                    s1_empty = False
                    ar[0][1] = -1

            if t1.collidepoint(pos) and t1_empty is True:
                click = click + 1
                if player == 1:
                    pygame.draw.line(win, (255, 255, 0), (400, 50), (500, 150), 10)
                    pygame.draw.line(win, (255, 255, 0), (400, 150), (500, 50), 10)
                    player = 2
                    t1_empty = False
                    ar[0][2] = 1
                else:
                    player = 1
                    pygame.draw.circle(win, (255, 0, 0), (450, 100), 60)
                    pygame.draw.circle(win, (0, 0, 0), (450, 100), 55)
                    t1_empty = False
                    ar[0][2] = -1

            if f2.collidepoint(pos) and f2_empty is True:
                click = click + 1
                if player == 1:
                    player = 2
                    pygame.draw.line(win, (255, 255, 0), (50, 225), (150, 325), 10)
                    pygame.draw.line(win, (255, 255, 0), (50, 325), (150, 225), 10)
                    f2_empty = False
                    ar[1][0] = 1

                else:
                    player = 1
                    pygame.draw.circle(win, (255, 0, 0), (100, 275), 60)
                    pygame.draw.circle(win, (0, 0, 0), (100, 275), 55)
                    f2_empty = False
                    ar[1][0] = -1

            if s2.collidepoint(pos) and s2_empty is True:
                click = click + 1
                if player == 1:
                    player = 2
                    s2_empty = False
                    pygame.draw.line(win, (255, 255, 0), (225, 225), (325, 325), 10)
                    pygame.draw.line(win, (255, 255, 0), (225, 325), (325, 225), 10)
                    ar[1][1] = 1

                else:
                    player = 1
                    pygame.draw.circle(win, (255, 0, 0), (275, 275), 60)
                    pygame.draw.circle(win, (0, 0, 0), (275, 275), 55)
                    s2_empty = False
                    ar[1][1] = -1

            if t2.collidepoint(pos) and t2_empty is True:
                click = click + 1
                if player == 1:
                    player = 2
                    pygame.draw.line(win, (255, 255, 0), (400, 225), (500, 325), 10)
                    pygame.draw.line(win, (255, 255, 0), (400, 325), (500, 225), 10)
                    t2_empty = False
                    ar[1][2] = 1
                else:
                    player = 1
                    pygame.draw.circle(win, (255, 0, 0), (450, 275), 60)
                    pygame.draw.circle(win, (0, 0, 0), (450, 275), 55)
                    t2_empty = False
                    ar[1][2] = -1

            if f3.collidepoint(pos) and f3_empty is True:
                click = click + 1
                if player == 1:
                    player = 2
                    pygame.draw.line(win, (255, 255, 0), (50, 400), (150, 500), 10)
                    pygame.draw.line(win, (255, 255, 0), (50, 500), (150, 400), 10)
                    f3_empty = False
                    ar[2][0] = 1
                else:
                    player = 1
                    pygame.draw.circle(win, (255, 0, 0), (100, 450), 60)
                    pygame.draw.circle(win, (0, 0, 0), (100, 450), 55)
                    f3_empty = False
                    ar[2][0] = -1

            if s3.collidepoint(pos) and s3_empty is True:
                click = click + 1
                if player == 1:
                    player = 2
                    pygame.draw.line(win, (255, 255, 0), (225, 400), (325, 500), 10)
                    pygame.draw.line(win, (255, 255, 0), (225, 500), (325, 400), 10)
                    s3_empty = False
                    ar[2][1] = 1

                else:
                    player = 1
                    pygame.draw.circle(win, (255, 0, 0), (275, 450), 60)
                    pygame.draw.circle(win, (0, 0, 0), (275, 450), 55)
                    s3_empty = False
                    ar[2][1] = -1

            if t3.collidepoint(pos) and t3_empty is True:
                click = click + 1
                if player == 1:
                    player = 2
                    pygame.draw.line(win, (255, 255, 0), (400, 400), (500, 500), 10)
                    pygame.draw.line(win, (255, 255, 0), (400, 500), (500, 400), 10)
                    t3_empty = False
                    ar[2][2] = 1

                else:
                    player = 1
                    pygame.draw.circle(win, (255, 0, 0), (450, 450), 60)
                    pygame.draw.circle(win, (0, 0, 0), (450, 450), 55)
                    t3_empty = False
                    ar[2][2] = -1

            is_wining()


def main():
    global run
    while run:
        insert()
        # updating window to be able to see the changes that happened in each iteration
        pygame.display.update()


main()
