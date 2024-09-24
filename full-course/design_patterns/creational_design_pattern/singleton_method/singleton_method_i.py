# The Singleton pattern is a design pattern that ensures a class has only one instance and provides a global point of access to that instance


class Singleton:
   __instance = None

   @staticmethod
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
        Singleton()
      return Singleton.__instance

   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         # store same object in instance
         Singleton.__instance = self

s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)
