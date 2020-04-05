try:
	x = input("give me a number: ")
	x = int(x)

	y = input("give me another number: ")
	y = int(y)

except ValueError:
	print("i need 2 numbers")

else:
	sum = x + y
	print(f"the sum of {x} and {y} is {sum}")