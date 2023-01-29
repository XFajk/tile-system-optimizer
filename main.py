import pygame
import random as rnd
from pygame.locals import *

pygame.init()


def create_level() -> list:  # generates the 1000 by 1000 level
    level = []
    for i in range(1000):
        level.append([])
        for j in range(1000):
            level[i].append(rnd.randint(1, 3))
    return level


def surf_rect(w, h, color) -> pygame.Surface:  # generates a rectangle surface with
    surf = pygame.Surface((w, h))
    surf.fill(color)
    return surf


def main() -> None:
    window = pygame.display.set_mode((800, 608))  # makes the widow surface
    clock = pygame.time.Clock()

    level = create_level()  # variable that stores the tile information

    # store the randomly colored tiles that have size 16x16 pixels
    img = [surf_rect(16, 16, (rnd.randint(0, 155), rnd.randint(0, 155), rnd.randint(0, 155))),
           surf_rect(16, 16, (rnd.randint(0, 155), rnd.randint(0, 155), rnd.randint(0, 155))),
           surf_rect(16, 16, (rnd.randint(0, 155), rnd.randint(0, 155), rnd.randint(0, 155))),
           surf_rect(16, 16, (rnd.randint(0, 155), rnd.randint(0, 155), rnd.randint(0, 155)))]

    scroll = [0, 0]  # this variable the offset of all the tiles

    op = True  # op stands for optimization aka this variable controls if the tile rendering is optimized or not

    # main loop
    done = False
    while not done:

        keys = pygame.key.get_pressed()  # gets the input from our keyboard

        # moves the level around
        if keys[K_w]:
            scroll[1] -= 5
        if keys[K_s]:
            scroll[1] += 5
        if keys[K_a]:
            scroll[0] -= 5
        if keys[K_d]:
            scroll[0] += 5

        window.fill((0, 0, 0))

        # the optimized rendering system
        if op:
            for y in range(int(scroll[1] / 16), int(scroll[1] / 16) + int(608 / 16) + 1):
                for x in range(int(scroll[0] / 16), int(scroll[0] / 16) + int(800 / 16) + 1):
                    try:
                        if x < 0 or x > len(level[y]):
                            pass
                        elif y < 0 or y > len(level):
                            pass
                        else:
                            window.blit(img[level[y][x]], (x * 16 - scroll[0], y * 16 - scroll[1]))
                    except IndexError:
                        pass

        # the unoptimized system
        if not op:
            for y, row in enumerate(level):
                for x, tile in enumerate(row):
                    window.blit(img[tile], (x * 16 - scroll[0], y * 16 - scroll[1]))

        pygame.display.update()

        # event loop
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if op:
                        op = False
                    else:
                        op = True

        # prints out on the window caption fps if optimized and the pos of the screen in tile coordination's
        pygame.display.set_caption(f"{int(clock.get_fps())} {op} {int(scroll[1] / 16)} {int(scroll[0] / 16)}")
        clock.tick(999)  # caps the fps


if __name__ == '__main__':
    main()
    pygame.quit()
    exit()
