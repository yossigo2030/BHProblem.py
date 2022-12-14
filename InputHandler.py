import numpy as np
import pygame

dct = {pygame.K_LEFT: False,
       pygame.K_RIGHT: False,
       pygame.K_UP: False,
       pygame.K_DOWN: False,
       pygame.K_SPACE: False,
       pygame.K_ESCAPE: False}


def get_input():
    direction = np.array([0, 0])
    events = pygame.event.get()
    for event in events:
        if event.type != pygame.KEYDOWN:
            continue
        if event.key == pygame.K_LEFT:
            dct[pygame.K_LEFT] = True
        if event.key == pygame.K_RIGHT:
            dct[pygame.K_RIGHT] = True
        if event.key == pygame.K_UP:
            dct[pygame.K_UP] = True
        if event.key == pygame.K_DOWN:
            dct[pygame.K_DOWN] = True
        if event.key == pygame.K_SPACE:
            dct[pygame.K_SPACE] = True
        if event.key == pygame.K_ESCAPE:
            dct[pygame.K_ESCAPE] = True
            print('QUIT')

    if dct[pygame.K_LEFT]:
        direction -= [1, 0]
    if dct[pygame.K_RIGHT]:
        direction += [1, 0]
    if dct[pygame.K_UP]:
        direction -= [0, 1]
    if dct[pygame.K_DOWN]:
        direction += [0, 1]
    for event in events:
        if event.type != pygame.KEYUP:
            continue
        if event.key == pygame.K_LEFT:
            dct[pygame.K_LEFT] = False
        if event.key == pygame.K_RIGHT:
            dct[pygame.K_RIGHT] = False
        if event.key == pygame.K_UP:
            dct[pygame.K_UP] = False
        if event.key == pygame.K_DOWN:
            dct[pygame.K_DOWN] = False
        if event.key == pygame.K_SPACE:
            dct[pygame.K_SPACE] = False
    return direction


def get_shot():
    return dct[pygame.K_SPACE]


def quit():
    if dct[pygame.K_ESCAPE]:
        return True
    return False


def clear():
    pygame.event.get()
