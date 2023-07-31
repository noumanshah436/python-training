# module = a file containing python code. ( i.e python file is also called a module )
# it May contain function , classes etc.
# used with modular programming, which is to separate a program into parts

# if we import a module, the code inside this module will execute
# ( i.e.  consider that we have run this file separately)

"""====== diff ways of accessing modules ===="""

# -----------  (1) using module name  ----------------
#

import messages

messages.hello()
messages.bye()

""" --------------- (2) using alias as module ---------------- """
#   we use alias for all attributes

import messages as msg

msg.hello()
msg.bye()

""" --------------------------------------------------------------
(3 i) list all the functions or classes you want to import 
-> not recommended if we import multiple modules
-> It do not need to write module name  """

from messages import hello, bye

hello()
bye()


"""  (3 ii) import all the functions and classes from module """
from messages import *

hello()
bye()


"""============ see list of built-in modules  ============ """

help("modules")

# *****

# Enter any module name to get more help.  Or, type "modules spam" to search
# for modules whose name or summary contain the string "spam". like
#
help("modules math")
help("modules os")



