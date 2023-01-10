from abc import ABC, abstractmethod


class Player(ABC):

    # define the __init__, draw, generate_mana, play, end_turn,
    # take_damage, and is_dead methods as @abstractmethods
    @abstractmethod
    def __init__(self, name, deck, life, attack=0, defense=0):
        self.name = name
        self.deck = deck
        self.life = life
        self.hand = []
        self.creatures = []
        self.mana = 0
        self.mana_available = 0
        self.attack = attack
        self.defense = defense
        self.graveyard = []
        self.empty_draws = 0

    @abstractmethod
    def __str__(self):
        return self.name

    @abstractmethod
    def draw(self):

        if self.deck.remaining() == 0:
            # increment the number of empty draws
            self.empty_draws += 1
            # deal damage to the player based on the number of empty draws
            print(f"{self} takes {self.empty_draws} damage"
                  + " due to empty draws.")
            self.take_damage(self.empty_draws)
            return None
        # draw a card from the player's deck
        card = self.deck.draw()
        print(f"{self} draws {card}.")
        self.hand.append(card)
        return card

    @abstractmethod
    def play(self, card, target=None):
        # play a card from the player's hand
        if card.can_play(self.mana_available):
            self.hand.remove(card)
            card.play(self, target)
            self.mana_available -= card.mana_cost
        else:
            raise ValueError("Not enough mana to play this card")

    @abstractmethod
    def take_damage(self, amount):
        # reduce the player's life by the given amount
        self.life -= amount
        print(f"{self} has {self.life} life remaining.")

    @abstractmethod
    def is_dead(self):
        # check if the player's life is less than or equal to 0
        if self.life <= 0:
            return True
        return False

    @abstractmethod
    def generate_mana(self):
        # generate additional mana for the player
        self.mana += 1
        self.mana_available += 1

    @abstractmethod
    def end_turn(self):
        # reset the player's mana and creatures
        self.mana_available = self.mana
        for creature in self.creatures:
            creature.tapped = False

    @abstractmethod
    def has_untapped_creatures(self):
        any([not c.tapped for c in self.creatures])

    @abstractmethod
    def get_untapped_creatures(self):
        return [c for c in self.creatures if not c.tapped]

    @abstractmethod
    def retrieve_from_graveyard(self, card_name):
        # retrieve a card with the given name from the graveyard
        for card in self.graveyard:
            if card.name == card_name:
                self.graveyard.remove(card)
                self.hand.append(card)
                break
        else:
            raise ValueError("Card not found in graveyard")
