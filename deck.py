import random


class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.shuffle()

    def shuffle(self):
        # shuffle the cards in the deck
        random.shuffle(self.cards)

    def draw(self):
        # draw a card from the top of the deck
        return self.cards.pop()

    def remaining(self):
        # return the number of cards remaining in the deck
        return len(self.cards)