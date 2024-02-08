import pygame
from pygame.sprite import Sprite, Group
from pygame.math import Vector2
from pygame.surface import Surface
from pygame import Rect

class Entity(Sprite):
    def __init__(self, groups, game : any , pos : Vector2, image : Surface) -> None:
        super().__init__(groups)
        self.COLLISION_TOLERANCE = 10
        self.game : any = game
        self.position : Vector2 = pos
        self.velocity : Vector2 = Vector2(0, 0)
        self.image : Surface = image.convert_alpha()
        self.rect : Rect = self.image.get_rect(topleft = pos)
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        self.blockedDir = Vector2(0, 0)


    def render(self, surface : Surface) -> None:
        surface.blit(self.image, self.rect)

    def collideWalls(self, walls : list[any]):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if abs(wall.rect.top - self.rect.bottom) < self.COLLISION_TOLERANCE:
                    self.rect.bottom = wall.rect.top
                    self.velocity.y = 0
                    self.blockedDir = Vector2(0,1)
                if abs(wall.rect.bottom - self.rect.top) < self.COLLISION_TOLERANCE:
                    self.rect.top = wall.rect.bottom
                    self.velocity.y = 0
                    self.blockedDir = Vector2(0,-1)
                if abs(wall.rect.right - self.rect.left) < self.COLLISION_TOLERANCE:
                    self.rect.left = wall.rect.right
                    self.velocity.x = 0
                    self.blockedDir = Vector2(-1,0)
                if abs(wall.rect.left - self.rect.right) < self.COLLISION_TOLERANCE:
                    self.rect.right = wall.rect.left
                    self.velocity.x = 0
                    self.blockedDir = Vector2(1,0)


    def update(self) -> None:
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        self.collideWalls(self.game.walls)
        self.render(self.game.screen)