responses = {}

poll_running = True

while poll_running:
	name = input("\nwhat is your name? ")
	response = input("what mountain would you like to climb? ")

	responses[name] = response

	repeat = input("would you like to let another person go (yes/no)?")
	if repeat == 'no':
		poll_running = False

print("\n---polling results---")
for name, response in responses.items():
	print(f"{name} would like to climb {response}")