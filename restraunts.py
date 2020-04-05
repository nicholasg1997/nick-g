class Restaurant():

	def __init__(self, name, cuisine):
		self.name = name.title()
		self.cuisine = cuisine
		self.number_served = 0

	def describe_restaurant(self):
		msg = f"\n{self.name} is serving {self.cuisine}"
		print(msg)

	def open_restaurant(self):
		msg = f"{self.name} is now open!"
		print(msg)

	def set_number_served(self, customers):
		self.number_served = customers

	def increment_customer(self, additional_customers):
		self.number_served += additional_customers

	def customers_served(self):
		print(f"we've served {self.number_served} people")






class User():
	def __init__(self, first_name, last_name, location):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.location = location.title()
		self.login_attempts = 0

	def describe_user(self):
		print(f"{self.first_name} {self.last_name}")
		print(f"location: {self.location}")

	def greet_user(self):
		print(f"hello {self.first_name} {self.last_name}")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0 

nick = User('nick', 'gault', 'whitefish')
nick.describe_user()
nick.increment_login_attempts()
nick.increment_login_attempts()
nick.increment_login_attempts()
nick.increment_login_attempts()
print(nick.login_attempts)
nick.reset_login_attempts()
print(nick.login_attempts)





