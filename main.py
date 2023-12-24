import pygame
from gameController import GameController

pygame.init()

screen = pygame.display.set_mode((800, 600))

#game = Game(pygame, screen)

game_controller = GameController(pygame, screen)

run = True
while run:
     screen.fill((0,0,0))
     game_controller.screen.draw()
     

     #event handler
     for event in pygame.event.get():
          #game quit
          if event.type == pygame.QUIT:
               run = False
          #click checker
          if event.type == pygame.MOUSEBUTTONDOWN:
               game_controller.screen.on_mouse_down(pygame.mouse.get_pos(), game_controller)

     pygame.display.update()
pygame.quit()