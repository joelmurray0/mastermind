class Circle:
     def __init__(self, x, y, circle_colour, radius, pygame):
          self._pygame = pygame
          self._centre = (x,y)
          self._circle_colour = circle_colour
          self._radius = radius
     
     def circle_draw(self, screen):
          self._pygame.draw.circle(screen, self._circle_colour, self._centre, self._radius)