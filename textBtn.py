from button import Button

class TextButton(Button):
     def __init__(self, x, y,btn_colour , text, font_type, font_size, font_colour, pygame):
          super().__init__(x, y, btn_colour, pygame)
          self._text = text
          self._font_type = font_type
          self._font_size = font_size
          self._font_colour = font_colour
          self._font = self.text_init()
          self._rect = self.make_rect()

     ## button making
     def text_init(self):
          # sets the font
          return self._pygame.font.Font(self._font_type, self._font_size)
     
     def set_text(self):
          # renders the font
          return self._font.render(self._text, True,self._font_colour, self.btn_colour)
     
     def make_rect(self):
          # creates rectangle around the text
          rect = self.set_text().get_rect()
          # sets center
          rect.center = self._center
          return rect
     
     ## btn drawing
     def btn_draw(self, screen):
          # draws the rectangle
          screen.blit(self.set_text(), self._rect)
     
     def onhover(self):
          left_chr = TextButton(self._center[0] - self._rect.width/2 - 20, self._center[1],(0,0,0), ">", "kongtext\kongtext.ttf", self._font_size, (255,255,255), self._pygame)
          left_chr.onlick = self.null
          right_chr = TextButton(self._center[0] + self._rect.width/2 + 20, self._center[1],(0,0,0), "<", "kongtext\kongtext.ttf", self._font_size, (255,255,255), self._pygame)
          right_chr.onlick = self.null
          return [left_chr, right_chr]
          

     def load_btn_onclick(self):
          return self.text[-1]