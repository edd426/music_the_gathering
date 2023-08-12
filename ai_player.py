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
        available_hand = self.hand.copy()
        while len(available_hand) > 0 and self.mana_available > 0:
            # choose a random card from the hand to play
            card_index = random.randint(0, len(available_hand) - 1)
            chosen_card = available_hand[card_index]

            # check if the card can be played
            if chosen_card.can_play(self.mana_available):
                # play the card
                self.play(chosen_card)
                available_hand.remove(chosen_card)
                print(f"{self} plays {chosen_card}.")
            else:
                print(f"Not enough mana to play {chosen_card}.")
                available_hand.remove(chosen_card)

    def choose_location(self, game_board):
        # Choose a random location to place a creature on the game board.
        # Get a list of available lanes and rows
        lanes = range(game_board.num_lanes)
        rows = range(game_board.num_rows)
        available_locations = [
            (lane, row) for lane in lanes for row in rows
            if not game_board.board[self.name][lane][row]]
        # Choose a random location from the available ones
        chosen_location = random.choice(available_locations)
        return chosen_location

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
