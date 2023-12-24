import numpy
import random

class Mastermind:
     CORRECT = 0
     IN = 1
     WRONG = 2

     def __init__(self, slots, options, guesses):
          self._slots = slots
          self._options = options
          self._guesses = guesses
          self._answer = self._generate_answer()
     
     def _generate_answer(self):
          return tuple([random.randint(1,self._options) for i in range(self._slots)])

     def check_guess(self, guess):
          comparison = numpy.subtract(guess, self._answer)
          output = [self.CORRECT for i in range(self._slots)]

          for i in range(self._slots):
               print(i)
               if comparison[i] != self.CORRECT:
                    if guess[i] in self._answer:
                         output[i] = self.IN
                    else:
                         output[i] = self.WRONG

          return tuple(output), guess
