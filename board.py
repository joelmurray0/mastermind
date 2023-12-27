from screen import Screen
from rectBtn import RectButton
from textBtn import TextButton
from circle import Circle
from infoPanel import InfoPanel

class Board(Screen):
     def __init__(self, mastermind, pygame, screen):
          super().__init__(screen)

          self._pygame = pygame
          self._mastermind = mastermind
          self.counter = 0
          self.colours = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (128,0,255), (255,128,0)]
          self._colours = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (128,0,255), (255,128,0)][:self._mastermind._options]
          self._dict_colours = self.make_colour_dict()

          self._btn_width = round((400 - 25*(self._mastermind._slots - 1))/self._mastermind._slots)
          self._btn_height = round((400 - 10*(self._mastermind._guesses - 1))/self._mastermind._guesses)

          self.make_next_row()

          text = "Click the grey buttons to change colour"
          text_display = self.text_box_update(text)
          self._text_dict["terminal"] = text_display

          enter_btn = TextButton(700, 500, (0,128,128), "Guess", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          enter_btn.onclick = self.enter_onclick
          self.add_button("start", enter_btn)
          exit_btn = TextButton(100, 50, (0,128,128), "Return", 'freesansbold.ttf', 32, (255,255,255), self._pygame)
          exit_btn.onclick = self.exit_onclick
          self.add_button("exit", exit_btn)

     def make_colour_dict(self):
          output = {}
          for i in range(1, self._mastermind._options + 1):
               output[self._colours[i-1]] = i
          return output

     ## answer work

     def print_answer(self, y):
          colour_answer = self.answer_to_colour()
          for j in range(self._mastermind._slots):
               x = (200+(self._btn_width)/2) + j*(self._btn_width+25)

               btn = RectButton(x, y, self._colours, self._btn_width, self._btn_height, colour_answer[j], self._pygame)
               btn.onclick = self.null
               self.add_button(f"{self.counter}"+f"{j}", btn)

     def colour_result_correct_check(self, colour_result):
          output = True
          i=0
          while i != len(colour_result) and output:
               if colour_result[i] != (0,255,0):
                    output = False
               i += 1
          return output

     def answer_to_colour(self):
          output = []
          for i in self._mastermind._answer:
               output.append(self._colours[i-1])
          return tuple(output)

     def draw_circles(self, colour_result):
          for i in range(self._mastermind._slots):
               _x = 200/(self._mastermind._slots+1)
               x = _x*(i+1)
               y =  120 + (self.counter-1)*(self._btn_height+10)
               circle = Circle(x, y, colour_result[i], 6, self._pygame)
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

     def check_row_on_guess(self):
          output = True
          for i in range(self._mastermind._slots):
               if self._btn_dict[f"{self.counter - 1}" + f"{i}"].btn_colour == (128,128,128):
                    output = False
          return output

     def text_box_update(self, new_message):
          return InfoPanel(400, 15, 800, 80, new_message, 22, "freesansbold.ttf", self._pygame)

     ## button actions
     def enter_onclick(self, game_controller):
          if self.check_row_on_guess():
               guess = tuple(self._dict_colours[self._btn_dict[f"{self.counter - 1}" + f"{k}"].btn_colour] for k in range(self._mastermind._slots))
               colour_result = self._mastermind.answer_to_colour(guess)
               self.draw_circles(colour_result)
          else:
               self.text_display = self.text_box_update("Please click all buttons.")
               self._text_dict["terminal"] = self.text_display

          if self.counter == self._mastermind._guesses:
               text_display = self.text_box_update("You lost! The answer is on the lowest row.")
               self._text_dict["terminal"] = text_display
               self.disable_row()
               self._btn_dict["start"].onclick = self.null_onclick
               
               guess = tuple(self._dict_colours[self._btn_dict[f"{self.counter - 1}" + f"{k}"].btn_colour] for k in range(self._mastermind._slots))
               colour_result = self._mastermind.answer_to_colour(guess)
               self.draw_circles(colour_result)
               self.print_answer(120 + self.counter*(self._btn_height+10))   
          else:
               if self.colour_result_correct_check(colour_result):
                    self.disable_row()
                    self._btn_dict["start"].onclick = self.null_onclick
                    text_display = self.text_box_update("You win!")
                    self._text_dict["terminal"] = text_display
               else:
                    self.disable_row()
                    self.make_next_row()
    
     def null_onclick(self, game_controller):
          self.text_display = self.text_box_update("Can't click that!")
          self._text_dict["terminal"] = self.text_display

     def null(self):
          pass
     
     def exit_onclick(self, game_controller):
          game_controller.message("exitboard")