from screen import Screen
from rect_btn import RectButton
from text_btn import TextButton
from circle import Circle

class Board(Screen):
     def __init__(self, mastermind, pygame, screen):
          super().__init__(screen)

          self._pygame = pygame
          self._mastermind = mastermind
          self.counter = 0
          self.colours = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (128,0,255), (255,128,0)]
          self._colours = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (128,0,255), (255,128,0)][:self._mastermind._options + 1]
          self._dict_colours = self.make_colour_dict()
          print(self._dict_colours)


          self._btn_width = round((400 - 25*(self._mastermind._slots - 1))/self._mastermind._slots)
          self._btn_height = round((400 - 10*(self._mastermind._guesses - 1))/self._mastermind._guesses)

          self.make_next_row()

          enter_btn = TextButton(700, 500, (0,128,128), "Enter", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          enter_btn.onclick = self.enter_onclick
          self.add_button("start", enter_btn)
          exit_btn = TextButton(50, 50, (0,128,128), "Return", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          exit_btn.onclick = self.exit_onclick

     def make_colour_dict(self):
          output = {}
          for i in range(1, self._mastermind._options + 2):
               output[self._colours[i-1]] = i
          return output

     ## answer work

     def draw_circles(self, colour_result):
          for i in range(0,4):
               x = 20 + 50*i
               y =  120 + (self.counter-1)*(self._btn_height+10)
               circle = Circle(x, y, colour_result[i], 8, self._pygame)
               self._circle_dict[f"{x}"+f"{y}"] = circle

     ## row work
     def make_slot_btns(self, y): # makes the slots in a row
          for j in range(self._mastermind._slots):
               x = (200+(self._btn_width)/2) + j*(self._btn_width+25)

               btn = RectButton(x, y, self._colours, self._btn_width, self._btn_height, (128, 128, 128), self._pygame)
               btn.onclick = btn.colour_shift
               self.add_button(f"{self.counter}"+f"{j}", btn)
     
     def make_next_row(self):
          self.make_slot_btns(120 + self.counter*(self._btn_height+10))
          self.counter += 1
     
     def disable_row(self):
          for k in range(self._mastermind._slots):
               self._btn_dict[f"{self.counter - 1}" + f"{k}"].onclick = self.null_onclick

     ## button actions
     def enter_onclick(self, game_controller):
          if self.counter == self._mastermind._guesses:
               print(self._mastermind._answer)
               self.disable_row()
               self._btn_dict["start"].onclick = self.null_onclick
          else:
               guess = tuple(self._dict_colours[self._btn_dict[f"{self.counter - 1}" + f"{k}"].btn_colour] for k in range(self._mastermind._slots))
               
               print(guess)
               colour_result = self._mastermind.answer_to_colour(guess)
               self.draw_circles(colour_result)    
               if colour_result == ((0,255,0),(0,255,0),(0,255,0),(0,255,0)):
                    self.disable_row()
                    self._btn_dict["start"].onclick = self.null_onclick
                    print("WIN")
               else:
                    self.disable_row()
                    self.make_next_row()
               

     def null_onclick(self, game_controller):
          print("Can't click that!")
     
     def exit_onclick(self, game_controller):
          game_controller.message("exitboard")