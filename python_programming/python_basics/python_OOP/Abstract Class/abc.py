# Python program invoking a
# method using super()

import abc
from abc import ABC, abstractmethod

class R(ABC):
    def rk(self):
        print("Abstract Base Class")

class K(R):
  pass
  
r = K()
r.rk()
