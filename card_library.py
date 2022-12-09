import json
from card import Card
from deck import Deck

class CardLibrary:
    def __init__(self):
        self.cards = []

    def import_cards(self, filename):
        # import cards from a JSON file
        with open(filename) as f:
            data = json.load(f)
        for card_data in data:
            card = Card(
                card_data["name"],
                card_data["card_type"],
                card_data["abilities"],
                card_data["mana_cost"],
                attack=card_data.get("attack", 0),
                defense=card_data.get("defense", 0),
            )
            self.add_card(card)

    def add_card(self, card):
        # add a card to the library
        self.cards.append(card)

    def remove_card(self, card):
        # remove a card from the library
        self.cards.remove(card)

    def search(self, name=None, card_type=None, ability=None):
        # search the library for cards matching the given criteria
        results = self.cards
        if name is not None:
            results = [c for c in results if c.name == name]
        if card_type is not None:
            results = [c for c in results if c.card_type == card_type]
        if ability is not None:
            results = [c for c in results if ability in c.abilities]
        return results

    def create_deck(self, names):
        # create a deck from the cards with the given names
        cards = [c for c in self.cards if c.name in names]
        return Deck(cards)
