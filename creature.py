from card import Card
from player import Player


class Creature(Card):

    def __init__(self, name, abilities, mana_cost, card_type, attack=0,
                 defense=0):
        super().__init__(name, abilities, mana_cost, card_type)
        self.attack_value = attack
        self.defense_value = defense
        self.tapped = False
        self.player = None
        self.card_type = card_type
        self.flying = "Flying" in abilities
        self.reach = "Reach" in abilities

    def can_attack(self, target):
        # check if the creature can attack the target
        if not (isinstance(target, Creature) or isinstance(target, Player)):
            raise ValueError("Target must be a Creature or Player")
        if self.tapped:
            return False

        if isinstance(target, Creature):
            if target.tapped:
                return False

            if self.flying and not (target.flying or target.reach):
                return False

        return True

    def can_block(self, attacker):
        # check if this creature can block a given attacker
        if isinstance(attacker, Creature):
            # if the attacker is a creature and has flying or reach,
            # this creature can block it
            if attacker.flying:
                return self.flying or self.reach
            return True
        else:  # the attacker is a player
            return False

    def can_play(self, mana_available):
        return super().can_play(mana_available)

    def play(self, player, target):
        # summon the creature
        player.creatures.append(self)
        self.player = player

    def attack(self, target):
        # attack a target with the creature
        if not self.tapped:
            target.take_damage(self.attack_value)
            self.tapped = True
        else:
            raise ValueError("This creature has already attacked this turn")

    def take_damage(self, amount):
        # reduce the creature's defense by the given amount
        self.defense_value -= amount
        if self.defense_value <= 0:
            # destroy the creature
            self.player.creatures.remove(self)
            self.player.graveyard.append(self)
            print(f"{self} from {self.player} has died.")
        else:
            print(f"{self} from {self.player} has {self.defense_value} defense"
                  + " remaining.")

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

    def copy(self):
        # create a new Card object with the same attributes as the original
        new_creature = Creature(
            name=self.name,
            abilities=self.abilities,
            mana_cost=self.mana_cost,
            card_type=self.card_type,
            attack=self.attack_value,
            defense=self.defense_value
        )
        # if the original card is a creature, also copy its attack and defense
        # values
        return new_creature


