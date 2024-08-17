import math

from helpers import *
import pygame
from pygame import Vector2

keys = set()

r1 = 50
r2 = 25

m1 = 30
m2 = 30

theta1 = 0
theta2 = 0

p1 = Vector2(0, r1)
p2 = Vector2(r2, r1)

old_p1 = p1
old_p2 = p2

b = Vector2(0, 0)


def setup(screen: Screen):
    pass


def loop(screen: Screen, dt: float, time: float):
    global theta1
    global theta2
    global old_p1
    global old_p2
    global p1
    global p2
    global b



    dt_s = dt / 1000
    if len(keys) > 0: print("Key: " + str(pygame.key.name(list(keys)[0])))

    if pygame.key.key_code("left") in keys:
        b -= Vector2(dt_s * 80, 0)
    if pygame.key.key_code("right") in keys:
        b += Vector2(dt_s * 80, 0)
    if pygame.key.key_code("up") in keys:
        b += Vector2(0, dt_s * 80)
    if pygame.key.key_code("down") in keys:
        b -= Vector2(0, dt_s * 80)

    a1 = Vector2(0, -500)


    v1 = p1 - old_p1
    old_p1 = p1
    p1 = p1 + v1 + a1 * (dt_s * dt_s)

    a2 = a1
    v2 = p2 - old_p2
    old_p2 = p2
    p2 = p2 + v2 + a2 * (dt_s * dt_s)
    '''
    if p1.magnitude() > 100:
        p1 = p1.normalize() * 100

    if p2.magnitude() > 100:
        p2 = p2.normalize() * 100
    '''
    for i in range(1):

        change = p1 - b
        length = change.magnitude()
        diff = r1 - length

        norm = change.normalize()
        p1 += norm * diff


        change = p2 - p1
        length = change.magnitude()
        diff = r2 - length

        norm = change.normalize()

        p1 -= norm * diff / 2
        p2 += norm * diff / 2

    screen.fill(Color(0, 0, 0, 0))
    screen.draw_line(Color(255, 255, 255), b, p1, 5)
    screen.draw_circle(Color(255, 255, 255), p1, 20)
    screen.draw_line(Color(255, 255, 255), p1, p2, 5)
    screen.draw_circle(Color(255, 255, 255), p2, 20)

    # screen.draw_line(Color(255, 0, 0), start_p1, p1 + (p1 - start_p1) * -100, 5)

    # screen.draw_line(Color(255, 0, 0), start_p2, p2 + (p2 - start_p2) * -100, 5)

    screen.flip()


def main():
    pygame.init()

    window = pygame.display.set_mode((1000, 1000))

    screen = Screen(Vector2(1000, 1000), window)
    setup(screen)

    running = True

    time = 0

    # Game loop
    while running:

        for event in pygame.event.get():

            # if event is of type quit then set
            # running bool to false
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key not in keys:
                keys.add(event.key)
                if event.key == pygame.K_ESCAPE:
                    return
            elif event.type == pygame.KEYUP and event.key in keys:
                keys.remove(event.key)
        dt = pygame.time.Clock().tick(120)
        time += dt
        # print("Delta Time: " + str(dt))
        loop(screen, dt, time)

    pygame.quit()
    return


if __name__ == "__main__":
    main()
