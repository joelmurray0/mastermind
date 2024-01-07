import numpy
import random

class Mastermind:
     def __init__(self, slots, options, guesses, duplicate_mode):
          self._correct = 1
          self._in = 2
          self._wrong = 3

          self._slots = slots
          self._options = options
          self._guesses = guesses
          self._answer = self.generate_answer()
          self._duplicate_mode = duplicate_mode
          self.gamestate = {}
     
     def generate_answer(self):
          return tuple([random.randint(1,self._options) for _ in range(self._slots)])
     
     def save_guess(self, numerical_guess, guess_num):
          self.gamestate[guess_num] = [numerical_guess, self.check_guess(numerical_guess)] # [guess, answer]
          return self.gamestate[guess_num][1]

     def check_guess(self, guess):
          comparison = tuple(numpy.subtract(guess, self._answer))
          comparison_list = []
          for i in range(self._slots):
               if comparison[i] == 0:
                    comparison_list.append(self._correct)
               else:
                    comparison_list.append(-1)

          for i in range(self._slots):
               if comparison_list[i] == -1:
                    numbers = []
                    for j in range(self._slots):
                         if not self._duplicate_mode:
                              if guess[i] == self._answer[j] and comparison[j] != 0:
                                   numbers.append(self._answer[j])
                         else:
                              if guess[i] == self._answer[j]:
                                   numbers.append(self._answer[j])
                    if guess[i] in numbers:
                         comparison_list[i] = self._in
                    else:
                         comparison_list[i] = self._wrong

          return tuple(comparison_list)