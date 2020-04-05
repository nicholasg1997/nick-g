from random import randint

class Die:
	"""a class representing a single die"""
	def __init__(self,num_sides = 6):
		"""assume six sided die"""
		self.num_sides = num_sides

	def roll(self):
		"""roll die"""
		return randint(1,self.num_sides)