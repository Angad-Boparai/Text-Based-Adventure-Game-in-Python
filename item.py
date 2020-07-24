class item():
	def __init__(self):
		self.name=None
		self.description=None

	def set_description(self,description):
		self.description=description

	def get_description(self):
		return self.description

	def describe(self):
		print(self.description)			


	def set_name(self,name):
		self.name=name

	def get_name(self):
		return self.name
	def set_location(self,location):
		self.location=location
	def get_location(self):
		return self.location
	def desc_location(self):
		print(self.location)