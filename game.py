import random
from human_player import HumanPlayer
from ai_player import AIPlayer


class Game:
    def __init__(self, players):
        self.players = players
        self.current_player = 0
        self.turn = 0

    def next_turn(self):
        # advance to the next turn
        self.turn += 1
        self.current_player = (self.current_player + 1) % len(self.players)

    def end_game(self):
        # determine the winner of the game
        alive = [p for p in self.players if not p.is_dead()]
        if len(alive) <= 1:
            return True
        return False

    def get_victorious_player(self):
        living_players = [p for p in self.players if not p.is_dead()]
        if living_players and len(living_players) <= 1:
            return living_players[0]
        else:
            return None

    def get_attackable_targets(self, attacking_player):
        other_players = [p for p in self.players
                         if p != attacking_player]
        opposing_creatures = [c for p in other_players for c in p.creatures]

        return other_players + opposing_creatures

    def choose_target(self, targets):
        return random.choice(targets)

    def play_cards(self, player):
        while True:
            print("Your hand:")
            for i, card in enumerate(player.hand):
                print(f"{i + 1}.")
                card.print_stats()
                print()
            choice = input(
                "Enter the number of the card you want to play, "
                + "or 0 to not play any more cards: "
            )
            try:
                if choice == "0":  # Don't play any more cards
                    return None
                # convert the user's input to an index in the player's hand
                card_index = int(choice) - 1
                chosen_card = player.hand[card_index]
                if chosen_card.can_play(player.mana_available):
                    player.play(chosen_card)
                    print(f"{player} plays {chosen_card}.")
                else:
                    # If the player doesn't have enough mana to play this card,
                    # stop asking for card choices
                    print("Not a playable card. Moving to attack phase.")
                    return None
            except (ValueError, IndexError):
                print("Invalid choice. Please try again.")

    def play(self):
        # main game loop
        while True:
            player = self.players[self.current_player]

            # generate mana
            player.generate_mana()
            print(f"\n*** {player} begins their turn. "
                  + f"They have {player.mana_available} mana. ***")

            # draw a card
            drawn_card = player.draw()

            # have the player summon any number of cards
            if isinstance(player, HumanPlayer):
                self.play_cards(player)
            elif isinstance(player, AIPlayer):
                player.play_cards()
            else:
                raise ValueError("Invalid player type")

            print(f"\n{player} attack phase begins.")
            for creature in player.get_untapped_creatures():
                targets = self.get_attackable_targets(player)
                target = self.choose_target(targets)
                print(f"{creature} from {player} attacks {target}.")
                creature.attack(target)

            player.end_turn()
            # check if the game has ended
            game_over = self.end_game()
            if game_over:
                winner = self.get_victorious_player()
                if winner:
                    print(f"\n{winner} wins the game!")
                else:
                    print("\nGame is a draw, no winner.")

                break

            self.next_turn()
