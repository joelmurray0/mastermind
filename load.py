import pickle

class Load():
     def __init__(self, filename):
          self.filename = filename
     
     def load_onclick(self):
          return pickle.load(open(self.filename, "rb"))

     