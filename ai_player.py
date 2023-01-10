from player import Player
import random


class AIPlayer(Player):

    def __init__(self, name, deck, life, attack=0, defense=0):
        super().__init__(name, deck, life, attack, defense)

    def __str__(self):
        return super().__str__()

    def draw(self):
        return super().draw()

    def play(self, card, target=None):
        super().play(card, target)

    def play_cards(self):
        while len(self.hand) > 0 and self.mana_available > 0:
            # choose a random card from the hand to play
            card_index = random.randint(0, len(self.hand) - 1)
            chosen_card = self.hand[card_index]

            # check if the card can be played
            if chosen_card.can_play(self.mana_available):
                # play the card
                self.play(chosen_card)
                print(f"{self} plays {chosen_card}.")
            else:
                print(f"Not enough mana to play {chosen_card}. Skipping turn.")
                break

    def take_damage(self, amount):
        super().take_damage(amount)

    def is_dead(self):
        return super().is_dead()

    def generate_mana(self):
        super().generate_mana()

    def end_turn(self):
        super().end_turn()

    def has_untapped_creatures(self):
        return super().has_untapped_creatures()

    def get_untapped_creatures(self):
        return super().get_untapped_creatures()

    def retrieve_from_graveyard(self, card_name):
        super().retrieve_from_graveyard(card_name)
