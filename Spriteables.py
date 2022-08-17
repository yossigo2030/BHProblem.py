import pygame.sprite
import Draw
from DataStructures import DataStructures
from MovementPatterns import *


class BulletHellSprite(pygame.sprite.Sprite):
    # _sprite_group = AllSpritesGroup

    def __init__(self, location, sprite, data: DataStructures, movement_pattern: MovePattern = StraightPattern((0, 10)), hitbox_size=(25, 25), image_size=(40, 40)):
        super().__init__()
        self.data = data
        self.data.AllSpritesGroup.add(self)
        self.location = location
        self.image = pygame.transform.scale(pygame.image.load(sprite).convert_alpha(), image_size)
        self.imsize = image_size
        self.hitbox = hitbox_size
        self.move_pattern = movement_pattern

    def get_hitbox(self):
        return pygame.rect.Rect(self.location[0] - self.hitbox[0] / 2,
                                self.location[1] - self.hitbox[1] / 2,
                                self.hitbox[0], self.hitbox[1])

    def update(self):
        self.location = self.move_pattern.get_next_position(self.location)

    def draw(self):
        Draw.draw_sprite(self.image, self.location)


def out_of_bounds(location, sprite_size):
    return location[0] < -sprite_size[0] or location[0] > Draw.WIDTH or location[1] < -sprite_size[1] or location[1] > Draw.LENGTH


def sprite_culling(data: DataStructures):
    for sprite in data.AllSpritesGroup.sprites():
        if out_of_bounds(sprite.location, sprite.imsize):
            sprite.kill()
            del sprite
