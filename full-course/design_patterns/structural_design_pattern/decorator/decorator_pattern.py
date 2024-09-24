# https://www.geeksforgeeks.org/decorator-method-python-design-patterns/

# Decorator Method is a Structural Design Pattern which allows you to dynamically attach new behaviors to objects
# without changing their implementation by placing these objects inside the wrapper objects that contains the behaviors

class WrittenText:

	"""Represents a Written text """

	def __init__(self, text):
		self._text = text

	def render(self):
		return self._text

class UnderlineWrapper(WrittenText):

	"""Wraps a tag in <u>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<u>{}</u>".format(self._wrapped.render())

class ItalicWrapper(WrittenText):

	"""Wraps a tag in <i>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<i>{}</i>".format(self._wrapped.render())

# class BoldWrapper(WrittenText):

# 	"""Wraps a tag in <b>"""

# 	def __init__(self, wrapped):
# 		self._wrapped = wrapped

# 	def render(self):
# 		return "<b>{}</b>".format(self._wrapped.render())

""" main method """

if __name__ == '__main__':

	before_gfg = WrittenText("GeeksforGeeks")
	# after_gfg = UnderlineWrapper(before_gfg)
	after_gfg = ItalicWrapper(UnderlineWrapper(before_gfg))

	# after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

	print("before :", before_gfg.render())
	print("after :", after_gfg.render())
