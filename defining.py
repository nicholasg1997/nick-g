def sandwiches(*toppings):
	print("what would you like on your sandwich?")
	for topping in toppings:
		print(f"\t-im adding {topping} to your sandwich")
	print("your sandwich is ready")







def make_car(make, model, **other):
	car_dict = {
	'make': make.title(),
	'model': model.title(),
	}
	for other, value in other.items():
		car_dict[other] = value
	return car_dict

	

car = make_car('tesla', 'model x', color = 'white')
print(car)