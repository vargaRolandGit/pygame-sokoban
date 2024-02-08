import pygame
from pygame.math import Vector2
from pygame.surface import Surface 
from source.entity import Entity

class EndTile(Entity):
    def __init__(self, groups, game: any, pos: Vector2, image: Surface) -> None:
        super().__init__(groups, game, pos, image)
        self.game = game

    def collideBox(self, boxes) -> None:
        for box in boxes:
            if self.rect.colliderect(box.rect):
                self.game.load_level(self.game.levels[self.game.currentLevel + 1])
                self.game.currentLevel += 1

    def update(self) -> None:
        self.collideBox(self.game.boxes)
        return super().update()