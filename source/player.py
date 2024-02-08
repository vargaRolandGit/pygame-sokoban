import pygame
from pygame.math import Vector2
from pygame.sprite import Group
from pygame.surface import Surface
from source.entity import Entity
from pygame import Rect

class Player(Entity):
    def __init__(self, groups, game: any, pos: Vector2, image: Surface) -> None:
        super().__init__(groups, game=game, pos=pos, image=image)
        self.speed : int = 5
        self.game = game
        self.animationSpeed = 10

    def input(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.velocity.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.velocity.y = 1
        else:
            self.velocity.y = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity.x = 1
        else:
            self.velocity.x = 0

        if keys[pygame.K_r]:
            self.game.load_level(self.game.levels[self.game.currentLevel])

    def animate(self) -> None:
        ...

    def move(self) -> None:
        if self.velocity.magnitude() != 0:
            self.velocity = self.velocity.normalize()
        
        self.velocity.x *= self.speed
        self.velocity.y *= self.speed

    def update(self) -> None:
        self.input()
        self.move()
        return super().update()