from player import Player


class HumanPlayer(Player):

    def __init__(self, name, deck, life, attack=0, defense=0):
        super().__init__(self, name, deck, life, attack, defense)

    def __str__(self):
        return super().__str__()

    def play(self, card, target=None):
        super().play(card, target)

    def draw(self):
        return super().draw()

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
