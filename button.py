class Button:
     def __init__(self, x, y, font_colour, text, font_type, font_size, btn_colour, pygame):
          self._pygame = pygame
          self._btn_colour = btn_colour
          self._center = (x, y)
          self._text = text
          self._font_type = font_type
          self._font_size = font_size
          self._font_colour = font_colour
          self._font = self.text_init()
          self.rect = self.make_rect()
     
     def onclick(self, game_controller): # action for what happens when the button is clicked
          print("Starting...")
     
     ## button making
     def text_init(self):
          # sets the font
          return self._pygame.font.Font(self._font_type, self._font_size)
     
     def set_text(self):
          # renders the font
          return self._font.render(self._text, True, self._btn_colour, self._font_colour)
     
     def make_rect(self):
          # creates rectangle around the text
          rect = self.set_text().get_rect()
          # sets center
          rect.center = self._center
          return rect

     ## btn drawing
     def btn_draw(self, screen):
          # draws the rectangle
          screen.blit(self.set_text(), self.rect)