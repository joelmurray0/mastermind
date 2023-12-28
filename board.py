from screen import Screen
from rectBtn import RectButton
from textBtn import TextButton
from circle import Circle
import pickle

class Board(Screen):
     def __init__(self, mastermind, pygame, screen):
          super().__init__(screen)

          self._pygame = pygame
          self._mastermind = mastermind
          self.counter = 0
          self.colours = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (128,0,255), (255,128,0), (0,255,255), (255,0,255), (128,128,255), (128,255,128), (255,255,128), (255,0,128)]
          self._colours = self.colours[:self._mastermind._options]
          self._dict_colours = self.make_colour_dict()
          self.filename = "save.txt"

          self._btn_width = round((400 - 25*(self._mastermind._slots - 1))/self._mastermind._slots)
          self._btn_height = round((400 - 10*(self._mastermind._guesses - 1))/self._mastermind._guesses)

          self.write_past()
          self.make_next_row()

          text = "Click  the  grey  buttons  to  change  colour"
          self.text_display = self.text_box_write(22, text)
          self._text_dict["terminal"] = self.text_display

          enter_btn = TextButton(700, 500, (0,0,0), "Guess", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          enter_btn.onclick = self.enter_onclick
          self.add_button("start", enter_btn)

          exit_btn = TextButton(100, 50, (0,0,0), "Quit", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          exit_btn.onclick = self.exit_onclick
          self.add_button("exit", exit_btn)

          save_btn = TextButton(700, 50, (0,0,0), "Save", "arcadeclassic\ARCADECLASSIC.TTF", 32, (255,255,255), self._pygame)
          save_btn.onclick = self.save_onclick
          self.add_button("save", save_btn)

     def colour_to_number(self, colour):
          output = []
          for i in colour:
               output.append(self._dict_colours[i])
          return tuple(output)

     def write_past(self):
          for i in range(len(self._mastermind.gamestate)):
               guess, colour_response = self._mastermind.gamestate[i]
               y = 120 + i*(self._btn_height+10)
               self.print_answer(y, guess)
               self.draw_circles(y, colour_response)
               self.counter += 1

     def make_colour_dict(self):
          output = {}
          for i in range(1, self._mastermind._options + 1):
               output[self._colours[i-1]] = i
          return output

     ## answer work
     def print_answer(self, y, colour_answer):
          for j in range(self._mastermind._slots):
               x = (200+(self._btn_width)/2) + j*(self._btn_width+25)
               btn = RectButton(x, y, self._colours, self._btn_width, self._btn_height, colour_answer[j], self._pygame)
               btn.onclick = btn.null
               self.add_button(f"{self.counter}"+f"{j}", btn)

     # checks if guess is correct
     def colour_result_correct_check(self, colour_result):
          output = True
          i=0
          while i != len(colour_result) and output:
               if colour_result[i] != (0,255,0):
                    output = False
               i += 1
          return output
     
     # turns mastermind response to a tuple of rgb values
     def number_to_colour(self):
          output = []
          for i in self._mastermind._answer:
               output.append(self._colours[i-1])
          return tuple(output)

     # draws coloured circles at a given y value according to a tuple of rgb values
     def draw_circles(self, y, colour_result):
          for i in range(self._mastermind._slots):
               _x = 200/(self._mastermind._slots+1)
               x = _x*(i+1)
               circle = Circle(x, y, colour_result[i], 6, self._pygame)
               self._circle_dict[f"{x}"+f"{y}"] = circle

     ## row work
     def make_row_btns(self, y): # makes the slots in a row
          for j in range(self._mastermind._slots):
               x = (200+(self._btn_width)/2) + j*(self._btn_width+25)

               btn = RectButton(x, y, self._colours, self._btn_width, self._btn_height, (128, 128, 128), self._pygame)
               btn.onclick = btn.colour_shift
               self.add_button(f"{self.counter}"+f"{j}", btn)
     
     def make_next_row(self):
          self.make_row_btns(120 + self.counter*(self._btn_height+10))

     # stops a row's button from working
     def disable_current_row(self):
          for k in range(self._mastermind._slots):
               self._btn_dict[f"{self.counter}" + f"{k}"].onclick = self.null_onclick

     # confirms if all the guesses are selected
     def check_row_on_guess(self):
          output = True
          for i in range(self._mastermind._slots):
               if self._btn_dict[f"{self.counter}" + f"{i}"].btn_colour == (128,128,128):
                    output = False
          return output

     ## button actions
     def enter_onclick(self, game_controller):
          checked = False
          checked = self.check_row_on_guess()
          if checked:
               if self.counter != self._mastermind._guesses - 1:
                    colour_guess = tuple(self._btn_dict[f"{self.counter}" + f"{k}"].btn_colour for k in range(self._mastermind._slots))
                    numerical_guess = self.colour_to_number(colour_guess)
                    colour_result = self._mastermind.save_guess(colour_guess, numerical_guess, self.counter)
                    self.draw_circles(120 + (self.counter)*(self._btn_height+10), colour_result)
                    if self.colour_result_correct_check(colour_result):
                         self.text_display.update_message(40,"win")
                         self.text_display.y = 30
                         self._text_dict["terminal"] = self.text_display
                         self.disable_current_row()
                         self._btn_dict["start"].onclick = self.null_onclick
                         self._btn_dict["save"].onclick = self.null_saveclick
                    else:
                         self.disable_current_row()
                         self.counter += 1
                         self.make_next_row()
               else:
                    colour_guess = tuple(self._btn_dict[f"{self.counter}" + f"{k}"].btn_colour for k in range(self._mastermind._slots))
                    numerical_guess = self.colour_to_number(colour_guess)
                    colour_result = self._mastermind.save_guess(colour_guess, numerical_guess, self.counter)
                    self.draw_circles(120 + (self.counter)*(self._btn_height+10), colour_result)
                    if not self.colour_result_correct_check(colour_result):
                         self.text_display.update_message(40, "lose")
                         self.text_display.y = 30
                         self._text_dict["terminal"] = self.text_display
                         self.disable_current_row()
                         self.counter += 1
                         self._btn_dict["start"].onclick = self.null_onclick
                         self.print_answer(120 + (self.counter)*(self._btn_height+10), self.number_to_colour())
                    else:
                         self.text_display.update_message(40,"win")
                         self._text_dict["terminal"] = self.text_display
                         self.disable_current_row()
                         self._btn_dict["start"].onclick = self.null_onclick
                         self._btn_dict["save"].onclick = self.null_saveclick
          else:
               self.text_display.update_message(22, "use  all  slots")
               self._text_dict["terminal"] = self.text_display

     def null_saveclick(self, game_controller):
          self.text_display.update_message(22, "cannot  save  a  finished  game")
          self._text_dict["terminal"] = self.text_display
    
     def null_onclick(self, game_controller):
          self.text_display.update_message(22, "cannot  click  that")
          self._text_dict["terminal"] = self.text_display
     
     def exit_onclick(self, game_controller):
          game_controller.message("exitboard")

     def save_onclick(self, game_controller):
          pickle.dump(self._mastermind, open(self.filename, "wb"))
          game_controller.message("exitboard")