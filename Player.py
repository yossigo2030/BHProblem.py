import InputHandler
import cooldown
from DataStructures import Directions, DataStructures
from MovementPatterns import PlayerMovementPattern, StraightPattern
from Projectile import Projectile
from Spriteables import BulletHellSprite


class Player(BulletHellSprite):
    def __init__(self, location, sprite, data, speed=10, shoot_cd=10, hitbox_size=(25, 25), image_size=(40, 40)):
        super().__init__(location, sprite, data, PlayerMovementPattern(speed, image_size), hitbox_size, image_size)
        self.data.PlayerSpriteGroup.add(self)
        self.cd = cooldown.cooldown(shoot_cd)
        self.iframe = cooldown.cooldown(20)
        self.speed = speed
        self.hitbox_backup = self.hitbox
        self.lives = 3
        self.score = 0

    def get_location(self):
        return self.location

    def set_score(self, add):
        self.score += add

    def on_hit(self):
        if self.iframe.is_ready():
            self.iframe.use()
            self.hitbox = (0, 0)
            self.lives -= 1
        return self.lives > 0

    def update(self):
        super().update()
        shoot = InputHandler.get_shot()

        # Handle iFrames by removing the hitbox
        self.iframe.update()
        if self.iframe.is_ready():
            self.hitbox = self.hitbox_backup

        # Handle the shooting
        self.cd.update()
        if shoot and self.cd.is_ready():
            self.cd.use()
            Projectile(self.location, "resources\\ball.png", self.data, movement_pattern=StraightPattern(Directions.Up(10)), player_projectile=True)