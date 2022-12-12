from abc import ABC, abstractmethod


class Card(ABC):

    def __init__(self, name, abilities, mana_cost, card_type):
        self.name = name
        self.abilities = abilities
        self.mana_cost = mana_cost
        self.card_type = card_type

    def __str__(self):
        return self.name

    @abstractmethod
    def can_play(self, mana_available):
        return mana_available >= self.mana_cost

    @abstractmethod
    def play(self, player, target=None):
        pass

    @abstractmethod
    def print_stats(self):
        # create the top of the box
        box = "+" + "-" * (len(self.name) + 2) + "+\n"

        # add the card's name to the box
        box += "| " + self.name + " |\n"

        # add a line to the box
        box += "+" + "-" * (len(self.name) + 2) + "+\n"

        # add the card's abilities to the box
        abilities = ", ".join(self.abilities)
        box += "| Abilities: " + abilities + " |\n"

        # add the card's mana cost to the box
        box += "| Mana cost: " + str(self.mana_cost) + " |\n"

        # add the card's other stats to the box
        if self.card_type == "Creature":
            box += "| Attack: " + str(self.attack_value) + " |\n"
            box += "| Defense: " + str(self.defense_value) + " |\n"

        # add the bottom of the box
        box += "+" + "-" * (len(self.name) + 2)
        print(box)

