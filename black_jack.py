#BlackJack Game
import random

def deal_cards():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    selected_card = random.choice(cards)
    return selected_card


user_cards = []
computer_cards = []

for _  in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

def calculate_score(score_list):
    #blackjack
    if sum(score_list) == 21 and len(score_list) == 2:
        return 0
    if 11 in score_list and sum(score_list) > 21:
        score_list.remove(11)
        score_list.append(1)
    return sum(score_list)

print(user_cards)
print(calculate_score(user_cards))