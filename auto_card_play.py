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
		self.bet2 = 0
		self.bet3 = 0
		self.bet4 = 0
		self.bet5 = 0
		self.bet6 = 0
		self.bet7 = 0
		self.bet8 = 0
		self.bet9 = 0
		self.bet10 = 0
		self.total_bet = 0
		self.profit_loss = 0
		

	def shuffle_cards(self):
		random.shuffle(card_deck)
	
	def starting_hand(self):
		
		for i in range(2):
			hand.append(card_deck.pop(0))
		print(hand)

	def dealer_starting_hand(self):
		
		for i in range(2):
			dealer_cards.append(card_deck.pop(0))
		dealer_first_card.append(dealer_cards.pop(0))



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
				hand.append(card_deck.pop(0))
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
				dealer_cards.append(card_deck.pop(0))
				
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
		# 2 count
		if card_deck.count(2) >= 1:
			count_2 = (len(card_deck)-card_deck.count(2))/card_deck.count(2)
		else:
			count_2 = 50
		# bet for 2 count
		if count_2 <= 9:
			self.bet2 = 6
		elif count_2 <= 15:
			self.bet2 = 4
		elif count_2 > 15:
			self.bet2 = 0
		#3 count
		if card_deck.count(3) >= 1:
			count_3 = (len(card_deck)-card_deck.count(3))/card_deck.count(3)
		else:
			count_3 = 50
		# bet for 3 count
		if count_3 <= 14:
			self.bet3 = 6
		elif count_3 <= 19:
			self.bet3 = 4
		elif count_3 <= 30:
			self.bet3 = 2
		elif count_3 > 30:
			self.bet3 = 1
		#4 count
		if card_deck.count(4) >= 1:
			count_4 = (len(card_deck)-card_deck.count(4))/card_deck.count(4)
		else:
			count_4 = 50
		# bet for 4 count
		if count_4 <= 14:
			self.bet4 = 5
		elif count_4 <= 19:
			self.bet4 = 4
		elif count_4 <= 30:
			self.bet4 = 2
		elif count_4 > 30:
			self.bet4 = 2
		#5 count
		if card_deck.count(5) >= 1:
			count_5 = (len(card_deck)-card_deck.count(5))/card_deck.count(5)
		else:
			count_5 = 50
		# bet for 5 count
		if count_5 <= 9:
			self.bet5 = 6
		elif count_5 <= 15:
			self.bet5 = 4
		elif count_5 <= 19:
			self.bet5 = 1
		elif count_5 > 19:
			self.bet5 = 0
		#6 count
		if card_deck.count(6) >= 1:
			count_6 = (len(card_deck)-card_deck.count(6))/card_deck.count(6)
		else:
			count_6 = 50
		# bet for 6 count
		if count_6 <= 14:
			self.bet6 = 5
		elif count_6 <= 19:
			self.bet6 = 4
		elif count_6 <= 30:
			self.bet6 = 2
		elif count_6 > 30:
			self.bet6 = 1
		#7 count
		if card_deck.count(7) >= 1:
			count_7 = (len(card_deck)-card_deck.count(7))/card_deck.count(7)
		else:
			count_7 = 50
		# bet for 7 count
		if count_7 <= 9:
			self.bet7 = 2
		elif count_7 <= 14:
			self.bet7 = 4
		elif count_7 <= 19:
			self.bet7 = 6
		elif count_7 > 19:
			self.bet7 = 8
		#8 count
		if card_deck.count(8) >= 1:
			count_8 = (len(card_deck)-card_deck.count(8))/card_deck.count(8)
		else:
			count_8 = 50
		# bet for 8 count
		if count_8 <= 9:
			self.bet8 = 2
		elif count_8 <= 14:
			self.bet8 = 2
		elif count_8 <= 19:
			self.bet8 = 3
		elif count_8 > 19:
			self.bet8 = 5
		#9 count
		if card_deck.count(9) >= 1:
			count_9 = (len(card_deck)-card_deck.count(9))/card_deck.count(9)
		else:
			count_9 = 50
		# bet for 9 count
		if count_9 <= 9:
			self.bet9 = 4
		elif count_9 <= 14:
			self.bet9 = 5
		elif count_9 <= 19:
			self.bet9 = 7
		elif count_9 > 19:
			self.bet9 = 10
		#10 count
		if card_deck.count(10) >= 1:
			count_10 = (len(card_deck)-card_deck.count(10))/card_deck.count(10)
		else:
			count_10 = 50
		# bet for 10 count
		if count_10 <= 4:
			self.bet10 = 5
		elif count_10 < 6:
			self.bet10 = 5
		elif count_10 < 9:
			self.bet10 = 15
		elif count_10 >= 9:
			self.bet10 = 30



		#calculating total bet
		self.total_bet = (self.bet2+self.bet3+self.bet4+self.bet5+self.bet6+self.bet7+self.bet8+self.bet9+self.bet10)
		print(f"bet: {self.total_bet}")









		

	
	def play_blackjack(self):
	
		
		game.starting_hand()
		game.dealer_starting_hand()
		dealer_cards.extend(dealer_first_card)
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

game.shuffle_cards()


for i in range(100_000):
	game.play_blackjack()
	if len(card_deck) < 35:
		card_deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4*game.amount_of_decks
		game.shuffle_cards()
		while discarded_cards:
			discarded_cards.pop()



	






print(f"you went bust {game.bust_count} times")
print(f"won {game.games_won} times")
print(f"lost {game.games_lost} times")
print(f"tied {game.games_drawn} times")
print(f"profit or loss: ${game.bank_roll-1000}")
card = 1
#while card <=10:
	#print(f"{card}: {card_deck.count(card)}")
	#card += 1
