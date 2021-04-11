import pygame as pg
from game import Game

SCREEN_WIDTH = 25 * Game.TILE_COLS
SCREEN_HEIGHT = 25 * Game.TILE_ROWS

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

all_sprites = pg.sprite.Group()
snake_sprites = pg.sprite.Group()

running = True
while running:
  for event in pg.event.get():
      if event.type == pg.QUIT:
          running = False

  screen.fill((40, 40, 40))

  pg.display.flip()
  clock.tick(60)

pg.quit()
