import pygame
from pygame.math import Vector2
from pygame.surface import Surface
from source.entity import Entity

class Ground(Entity):
    def __init__(self, groups, game: any, pos: Vector2, image: Surface) -> None:
        super().__init__(groups, game, pos, image)