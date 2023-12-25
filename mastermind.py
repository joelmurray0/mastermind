import numpy
import random

class Mastermind:
     

     def __init__(self, slots, options, guesses, duplicate_mode):
          self._correct = 0
          self._in = 1
          self._wrong = 2

          self._slots = slots
          self._options = options
          self._guesses = guesses
          self._answer = self._generate_answer()
          self._duplicate_mode = duplicate_mode

          self._answer_dict = {
               self._correct: (0,255,0),
               self._in: (255, 165, 0),
               self._wrong: (255,0,0)
          }
     
     def _generate_answer(self):
          return tuple([random.randint(1,self._options) for i in range(self._slots)])

     def check_guess(self, guess):
          if self._duplicate_mode:
               clone_answer = list(self._answer).copy()

               correct_answers = []
               for i in range(self._slots):
                    if guess[i] == clone_answer[i]:
                         correct_answers.append(i)
               
               for j in range(len(correct_answers)):
                    del guess[correct_answers[j]]
                    del clone_answer[correct_answers[j]]
               
               output = []
               for k in range(self._slots):
                    if k == correct_answers[k]:
                         output.append(self._correct)
                    else:
                         if guess[0] in clone_answer:
                              output.append(self._in)
                         else:
                              output.append(self._wrong)
          else:
               guess = tuple(guess)
               comparison = numpy.subtract(guess, self._answer)
               output = [self.CORRECT for i in range(self._slots)]

               for i in range(self._slots):
                    if comparison[i] != self._correct:
                         if guess[i] in self._answer:
                              output[i] = self._in
                         else:
                              output[i] = self._wrong

          return tuple(output)
     
     def answer_to_colour(self, guess):
          output = []
          guess_result = self.check_guess(guess)
          for i in range(self._slots):
               output.append(self._answer_dict[guess_result[i]])

          return tuple(output)
