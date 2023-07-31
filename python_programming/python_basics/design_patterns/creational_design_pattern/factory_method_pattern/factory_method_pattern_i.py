# Factory Method is a Creational Design Pattern that allows an interface or a class to create an object,
# but lets subclasses decide which class or object to instantiate.

# Using the Factory method, we have the best ways to create an object. Here, objects are created without exposing the logic to the client, and for creating the new type of object, the client uses the same common interface.


class Button(object):
	html = ""
	def get_html(self):
		return self.html

class Image(Button):
   html = "<img></img>"

class Input(Button):
   html = "<input></input>"

class Flash(Button):
   html = "<obj></obj>"

class ButtonFactory():
		def create_button(self, typ):
			if typ == "image":
				return Image()
			elif typ == "input":
				return Input()
			elif typ == "flash":
				return Flash()

button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
  print(button_obj.create_button(b).get_html())



# python3 "design_patterns/creational_design_pattern/factory_method_pattern/factory_method_pattern_ii.py"

# output:
# <img></img>
# <input></input>
# <obj></obj>
