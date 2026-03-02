# from random import choice
import random

# coin = choice(["heads", "tails"])
# coin = random.choice(["heads", "tails"])
# print(coin)
# number = random.randint(1, 100)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
