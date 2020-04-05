sandwich_orders = ['veggie','pastrami', 'meatball', 'cold cut', 'pastrami', 'tuna']
finished_sandwiches = []

print("sorry no pastrami")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')



while sandwich_orders:
	sandwiche = sandwich_orders.pop()

	print(f"you're {sandwiche} sandwich is being made.")
	finished_sandwiches.append(sandwiche)

print("\nmade sandwich list:")

for sandwich in finished_sandwiches:
	print(f"\ti made a {sandwich} sandwich")

