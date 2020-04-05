#card_1 = input("what card did you get: ")
#card_2 = input("what other card did you get: ")
#hand = [card_1,card_2]
#for i in range (3):
	#card = input("what did you get dealt: ")
	#card = int(card)
	#hand.append(card)
#hand = (int (i) for i in hand)
#print(sum(hand))
hand = []
class Blackjack:

	def __init__(self, decks, players):
		self.hand = []

	def deal(self):
		prompt = input("what card:")
		hand.append(prompt)
		hand = (int (i) for i in hand)
		print(hand)

game = Blackjack(1,1)
game.deal()
	def get_ace(self):
		if hand.count(ace) >= 1:
			if sum(hand) >= 22:
				B = 1
			if sum(hand) <= 21:
				B = 11
		else:
			B = 11
		ace = B
#ace = 1 ace = [:] clear ace apeend ace with 1 or 11