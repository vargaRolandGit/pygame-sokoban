import pygame
from pygame.math import Vector2
from pygame.surface import Surface
from source.entity import Entity
from source.player import Player
from source.wall import Wall

class Box(Entity):
    def __init__(self, groups, game: any, pos: Vector2, image: Surface) -> None:
        super().__init__(groups, game, pos, image)
        self.game = game
        self.game.boxes.append(self)



    def collidePlayer(self, player : Player, force : int):
        if self.rect.colliderect(player.rect):
            if abs(player.rect.top - self.rect.bottom) < self.COLLISION_TOLERANCE:
                player.rect.top = self.rect.bottom
                if self.blockedDir != Vector2(0,1):
                    self.velocity.y = -1 * force
            if abs(player.rect.bottom - self.rect.top) < self.COLLISION_TOLERANCE:
                player.rect.bottom = self.rect.top
                if self.blockedDir != Vector2(0,-1):
                    self.velocity.y = force
            if abs(player.rect.right - self.rect.left) < self.COLLISION_TOLERANCE:
                player.rect.right = self.rect.left
                if self.blockedDir != Vector2(1,0):
                    self.velocity.x = force
            if abs(player.rect.left - self.rect.right) < self.COLLISION_TOLERANCE:
                player.rect.left = self.rect.right
                if self.blockedDir != Vector2(-1,0):
                    self.velocity.x = -1 * force

    def update(self) -> None:
        self.collidePlayer(self.game.player, 5)
        return super().update()