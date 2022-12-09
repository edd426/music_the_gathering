class Card:
    def __init__(self, name, card_type, abilities, mana_cost):
        self.name = name
        self.card_type = card_type
        self.abilities = abilities
        self.mana_cost = mana_cost

    def __str__(self):
        return self.name

    def can_play(self, mana_available):
        return mana_available >= self.mana_cost

    def play(self):
        # apply the effects of the card's abilities