import random

#card_deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
dealer_first_card = []
hand = []
hit_or_stay = {'action': ''}
dealer_cards = []
discarded_cards = []
total_p_l = []
class Play_Blackjack:
	"""attempting to create auto card countin"""
	
	def __init__(self, players, decks):
		self.players = players
		self.amount_of_decks = decks
		self.bust_count = 0
		self.games_won = 0
		self.games_lost = 0
		self.games_drawn = 0
		self.card_count_plus = 0
		self.card_count_negative = 0
		self.bank_roll = 1000
		self.bet1 = 0
		self.bet2 = 0
		self.bet3 = 0
		self.total_bet = 0
		self.profit_loss = 0
		

	def deck_amount(self):
		how_many_decks = input("how many decks: ")
	
	def starting_hand(self):
		prompt = input("what was your first card: ")
		hand.append(int(prompt))
		prompt = input("what was your second card: ")
		hand.append(int(prompt))
		print(sum(hand))
		


	def dealer_starting_hand(self):
		prompt = input("what card is dealer showing: ")
		dealer_cards.append(int(prompt))
		


	def hit_or_stay(self):
		if 2 in dealer_first_card:
			if sum(hand) <= 12:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'	

		if 3 in dealer_first_card:
			if sum(hand) <= 12:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 4 in dealer_first_card:
			if sum(hand) <= 11:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 5 in dealer_first_card:
			if sum(hand) <= 11:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 6 in dealer_first_card:
			if sum(hand) <= 11:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 7 in dealer_first_card:
			if sum(hand) <= 16:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 8 in dealer_first_card:
			if sum(hand) <= 16:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 9 in dealer_first_card:
			if sum(hand) <= 16:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 10 in dealer_first_card:
			if sum(hand) <= 16:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'

		if 1 in dealer_first_card:
			if sum(hand) <= 17:
				hit_or_stay['action'] = 'hit'
			else:
				hit_or_stay['action'] = 'stay'
		print(hit_or_stay.values())

	def auto_play(self):
		while True:
			if sum(hand) >= 22:
				print(f"you went bust with a {sum(hand)}")
				self.bust_count += 1
				break
			elif 'hit' in hit_or_stay.values():
				print("hit")
				card_dealt = input("what card were you dealt: ")
				hand.append(card_dealt)
				hand = (int (i) for i in hand)
				print(f"the new sum is {sum(hand)}")
				self.hit_or_stay()
			elif 'stay' in hit_or_stay.values():
				print(f"you finished with a {sum(hand)}")
				break
	def dealer_auto_play(self):
		while True:
			if sum(dealer_cards) == 21:
				print("the dealer got a blackjack")
				break
			if sum(dealer_cards) <=17:
				dealer_dealt = input("what was dealer dealt: ")
				dealer_cards.append(dealer_dealt)
				dealer_cards =(int (i) for i in dealer_cards)
				
			if sum(dealer_cards) >= 22:
				print("dealer went bust")
				break
			else:
				break
		print(f"the dealer finished with a {sum(dealer_cards)}")

	def who_won(self):
		
		if sum(hand) <= 21:
			if sum(dealer_cards) <= 21:
				if sum(hand) - sum(dealer_cards) > 0:
					print("you win")
					self.games_won += 1
					self.bank_roll += self.total_bet
					
				if sum(hand) - sum(dealer_cards) < 0:
					print("you lose")
					self.games_lost += 1
					self.bank_roll -= self.total_bet
					
				if sum(hand) - sum(dealer_cards) == 0:
					print("you tied")
					self.games_drawn += 1
					
						
			elif sum(dealer_cards) >= 22:
				print("you won")
				self.games_won += 1
				self.bank_roll += self.total_bet
					
		elif sum(hand) >= 22:
			print("you lost")
			self.games_lost += 1
			self.bank_roll -= self.total_bet
				

	def card_counting(self):
		self.card_count_plus = discarded_cards.count(2)+ discarded_cards.count(3)+discarded_cards.count(4)+ discarded_cards.count(5)+discarded_cards.count(6)
		
		self.card_count_negative = discarded_cards.count(10)+ discarded_cards.count(1)
		self.total_count = (self.card_count_plus - self.card_count_negative)/self.amount_of_decks
		print(f"total count is at {self.total_count}")
		#5 count
		if card_deck.count(5) >= 1:
			count_5 = (len(card_deck)-card_deck.count(5))/card_deck.count(5)
		else:
			count_5 = 21
		#5 count amount bet
		if count_5 <= 13:
			self.bet1 = 1
		elif count_5 <= 20:
			self.bet1 = 2
		elif count_5 > 20:
			self.bet1 = 5
		#10 count
		if card_deck.count(10) >= 1:
			count_10 = (len(card_deck)-card_deck.count(10))/card_deck.count(10)
		else:
			count_10 = 0.99
		#10 count amount bet
		if count_10 < 1:
			self.bet2 = 20
		elif count_10 < 1.25:
			self.bet2 = 15
		elif count_10 < 1.5:
			self.bet2 = 4 #8
		elif count_10 <= 1.75:
			self.bet2 = 2 #5
		else:
			self.bet2 = 1

		if self.total_count <= 2:
			self.bet3 = 1
		elif self.total_count < 4:
			self.bet3 = 2
		elif self.total_count < 6:
			self.bet3 = 3
		elif self.total_count <= 9:
			self.bet3 = 5
		elif self.total_count < 15:
			self.bet3 = 10

		#calculating total bet
		self.total_bet = (self.bet1+self.bet2+self.bet3)*10 
		print(f"bet: {self.total_bet}")









		

	
	def play_blackjack(self):
		
		game.starting_hand()
		game.dealer_starting_hand()
		game.hit_or_stay()
		game.auto_play()
	
		print(f"dealers starting hand was{dealer_cards}")
		print(f"dealer has a {dealer_first_card} to start")
		game.dealer_auto_play()
		game.card_counting()
		game.who_won()
		while dealer_first_card:
			discarded_cards.append(dealer_first_card.pop())
		while dealer_cards:
			discarded_cards.append(dealer_cards.pop())
		while len(hand) >= 1:
			discarded_cards.append(hand.pop())
		




	

total_sum = []
game = Play_Blackjack(1,3)
card_deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4*game.amount_of_decks




for i in range(100):
	game.play_blackjack()
	if len(card_deck) < 35:
		card_deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4*game.amount_of_decks
		while discarded_cards:
			discarded_cards.pop()

print(total_p_l)
print(f"average p/L {sum(total_p_l)/50}")


	






print(f"you went bust {game.bust_count} times")
print(f"won {game.games_won} times")
print(f"lost {game.games_lost} times")
print(f"tied {game.games_drawn} times")
print(f"profit or loss: ${game.bank_roll-1000}")
card = 1
#while card <=10:
	#print(f"{card}: {card_deck.count(card)}")
	#card += 1