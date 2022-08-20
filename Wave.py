import math
import random

import EnemyType
import MovementPatterns
import pygame

COOLDOWN = 100


class Wave:
    def __init__(self, number_of_wave, board_ratio, data):
        self.data = data
        self.EnemySpawnQueue = []
        self.number_of_wave = number_of_wave
        self.cooldownCounter = COOLDOWN
        self.board_ratio = board_ratio
        shape = (number_of_wave * (1 + number_of_wave)) / 2
        shape %= 3
        for i in range(number_of_wave):
            if shape == 0:
                self.EnemySpawnQueue.append([board_ratio[0] / 2, 100, True])

            if shape == 1:
                self.enemy_DNA(self.EnemySpawnQueue,
                               2,
                               (board_ratio[0] / 2),
                               (board_ratio[0] / 12),
                               20)
            if shape == 2:
                self.enemy_double_DNA(self.EnemySpawnQueue,
                                      3,
                                      (board_ratio[0] / 4),
                                      ((3 * board_ratio[0]) / 4),
                                      (board_ratio[0] / 12),
                                      30)
            shape = (shape + 1) % 3

    def __copy__(self, data):
        # todo fix this! @JoJo
        # test code, this obviously does not work properly on multiple separate instances
        self.data = data
        return self

    def number_getter(self):
        return self.number_of_wave

    def enemy_DNA(self, EnemySpawnQueue, number_of_arches, offset, change_factor, frames):
        for i in range(number_of_arches * 12):
            factor = math.cos(i * math.pi / 12) * change_factor
            EnemySpawnQueue.append([offset + factor, frames, False])

            if factor != 0:
                EnemySpawnQueue.append([offset - factor, 0, False])

    def enemy_double_DNA(self, EnemySpawnQueue, number_of_arches, offset1, offset2, change_factor, frames):
        for i in range(number_of_arches * 12):
            factor = math.cos(i * math.pi / 12) * change_factor
            EnemySpawnQueue.append([offset1 + factor, frames, False])
            EnemySpawnQueue.append([offset2 + factor, 0, False])

            if factor != 0:
                EnemySpawnQueue.append([offset1 - factor, 0, False])
                EnemySpawnQueue.append([offset2 - factor, 0, False])

    def update(self):
        if len(self.EnemySpawnQueue) == 0:
            if self.cooldownCounter == COOLDOWN:
                print("end of wave")
            if self.cooldownCounter == 0:
                return 1
            self.cooldownCounter -= 1
        else:
            while self.EnemySpawnQueue[0][1] <= 0:
                head = self.EnemySpawnQueue.pop(0)
                if head[2]:
                    gato = pygame.image.load(r"resources\en_boss.png")
                    EnemyType.EnemyShooter([head[0], 0], pygame.transform.scale(gato,[75,75]),
                                           self.data, MovementPatterns.StraightPattern((0, 1)),
                                           [MovementPatterns.StraightPattern((0, 2)),
                                            MovementPatterns.StraightPattern((-1, 2)),
                                            MovementPatterns.StraightPattern((1, 2)),
                                            MovementPatterns.StraightPattern((0, -1)),
                                            MovementPatterns.StraightPattern((1, 0)),
                                            MovementPatterns.StraightPattern((-1, 0)),
                                            MovementPatterns.StraightPattern((1, 1)),
                                            MovementPatterns.StraightPattern((-1, 1)),
                                            MovementPatterns.StraightPattern((1, -1)),
                                            MovementPatterns.StraightPattern((-1, -1))])
                else:
                    EnemyType.EnemyShooter([head[0], 0], r"resources\en.png", self.data, MovementPatterns.StraightPattern((0, 1)), [MovementPatterns.StraightPattern(((random.random(), 4 * random.random())))])
                if len(self.EnemySpawnQueue) == 0:
                    break
            else:
                self.EnemySpawnQueue[0][1] -= 1
