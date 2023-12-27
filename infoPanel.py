from pygame import Rect
from textBtn import TextButton
import math

class InfoPanel():
     def __init__(self, x, y, width, height, message, font_size, font_type, pygame):
          self.x = x
          self.y = y
          self._width = width
          self._height = height
          self._pygame = pygame
          self._font_type = font_type
          self.update_message(font_size, message)

     def null(self):
          pass

     def update_message(self, new_font_size, new_message):
          self.font_size = new_font_size
          self.message = new_message
          self.char_width = 4*self.font_size/3
          self.letters_allowed = math.trunc(self._width/self.char_width)
          self.lines = self.make_text_list()
     
     def find_words_in_line(self, i):
          index = (i+1)*self.letters_allowed - 1
          new_index = index
          if self.message[index] == " ":
               output = self.message[(i)*self.letters_allowed:index] 
          else:
               new_index = self.message.rindex(" ", 0, index)
               output = self.message[(i)*self.letters_allowed:new_index] 

          return output, new_index

     def make_text_list(self):
          lines = []
          latest_index = 0
          for i in range(len(self.message)//self.letters_allowed):
               line, latest_index = self.find_words_in_line(i)
               lines.append(line)
          lines.append(self.message[latest_index:])
          return lines
     
     def text_draw(self, screen):
          self.rect_height = self._height/len(self.lines)
          for i in range(len(self.lines)):
               text = TextButton(self.x, self.y + i*self.rect_height, (0,0,0), self.lines[i], self._font_type, self.font_size, (255,255,255), self._pygame)
               text.onclick = self.null
               text.btn_draw(screen)
