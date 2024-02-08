import pygame, sys
from pygame.math import Vector2
from pygame.sprite import Group
from source.player import Player
from source.box import Box
from source.wall import Wall
from source.endtile import EndTile
from source.ground import Ground

# TEST
level1 = [
    ['','w','w','w','w','w','w','w','w'],
    ['','w','w','w','','','','','w'],
    ['','w','','','','','w','','w'],
    ['','w','','b','p','','','w','w'],
    ['','w','','','','','','end','w'],
    ['','w','w','w','w','w','w','w','w'],
]

level2 = [
    ['w','','','w','w','w','w','w','w','w'],
    ['w','','','w','w','','','','','w'],
    ['w','','','','','','','w','','w'],
    ['w','p','','','b','','','','w','w'],
    ['w','','','','','','','','end','w'],
    ['w','','','w','w','w','w','w','w','w'],
]

class Game:
    def __init__(self) -> None:
        self.W_WIDTH : int = 1280
        self.W_HEIGHT : int = 720
        self.screen : pygame.Surface = pygame.display.set_mode((self.W_WIDTH, self.W_HEIGHT))
        self.clock : pygame.time.Clock = pygame.time.Clock()
        self.sprites : Group = Group()
        self.underSprites : Group = Group()
        self.groundLayer : Group = Group()
        self.walls : list[Wall] = []
        self.boxes : list[Box] = []
        self.currentLevel = 0
        self.levels = [level1, level2]

        self.load_level(self.levels[0])
        #self.player : Player = Player([self.sprites], self, Vector2(300,200), pygame.image.load(r'assets\Player\player_03.png'))
        #self.box : Box = Box([self.sprites], self, Vector2(500,500), pygame.image.load(r'assets\Crates\crate_07.png'))
        #self.wall : Wall = Wall([self.sprites], self, Vector2(100,500), pygame.image.load(r'assets\Crates\crate_11.png'))

    def load_level(self,level, step = 128):
        self.sprites.empty()
        self.underSprites.empty()
        self.boxes.clear()
        self.walls.clear()
        for x, row  in enumerate(level):
            for y, tile in enumerate(row):
                Ground([self.groundLayer], self, Vector2(y * step, x * step), pygame.image.load(r'assets\Ground\ground_04.png'))
                if tile == 'w':
                    Wall([self.sprites], self, Vector2(y * step, x * step), pygame.image.load(r'assets\Crates\crate_11.png'))
                elif tile == 'p':   
                    self.player = Player([self.sprites], self, Vector2(y * step, x * step), pygame.image.load(r'assets\playerFace_dark.png'))
                elif tile == 'b':
                    Box([self.sprites], self, Vector2(y * step, x * step), pygame.image.load(r'assets\Crates\crate_07.png'))  
                elif tile == 'end':
                    EndTile([self.underSprites], self, Vector2(y * step, x * step), pygame.image.load(r'assets\Crates\crate_10.png'))

    def run(self) -> None:
        while True:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.groundLayer.update()
            self.underSprites.update()
            self.sprites.update()
            pygame.display.update()
            self.clock.tick(60)

            