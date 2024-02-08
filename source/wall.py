from pygame.math import Vector2
from pygame.surface import Surface
from source.entity import Entity

class Wall(Entity):
    def __init__(self, groups, game: any, pos: Vector2, image: Surface) -> None:
        super().__init__(groups, game, pos, image)
        self.game = game
        self.game.walls.append(self)

    def update(self) -> None:
        return super().update()