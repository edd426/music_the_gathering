import random
from human_player import HumanPlayer
from ai_player import AIPlayer
from game_board import GameBoard


class Game:
    def __init__(self, players):
        self.players = players
        self.current_player = 0
        self.turn = 0
        self.game_board = GameBoard(players=players)

    def next_turn(self):
        # advance to the next turn
        self.turn += 1
        self.current_player = (self.current_player + 1) % len(self.players)

    def end_game(self):
        # determine the winner of the game
        alive = [p for p in self.players if not p.is_dead()]
        if len(alive) == 1:
            return True, alive[0]
        elif len(alive) == 0:
            return True, None
        return False, None

    # def get_victorious_player(self):
    #     living_players = [p for p in self.players if not p.is_dead()]
    #     if living_players and len(living_players) <= 1:
    #         return living_players[0]
    #     else:
    #         return None

    def get_attackable_targets(self, attacking_creature, attacking_player):
        # only attack players if they have no blocking creatures
        attackable_targets = []
        other_players = [p for p in self.players if p != attacking_player]

        for p in other_players:
            player_attackable_creatures = []
            for c in p.creatures:
                if attacking_creature.can_attack(c):
                    player_attackable_creatures.append(c)

            attackable_targets.extend(player_attackable_creatures)

            if not player_attackable_creatures:
                attackable_targets.append(p)

        return attackable_targets

    def choose_target(self, targets):
        return random.choice(targets)

    def play_cards(self, player):
        while True:
            print(f"{player.name} has {player.mana_available}"
                  " mana available.\n"
                  f"{player.name}'s hand:")
            for i, card in enumerate(player.hand):
                print(f"{i + 1}.")
                card.print_stats()
                print()
            choice = input(
                "Enter the number of the card you want to play, "
                "or 0 to not play any more cards: "
            )
            try:
                if choice == "0":  # Don't play any more cards
                    return None
                # convert the user's input to an index in the player's hand
                card_index = int(choice) - 1
                chosen_card = player.hand[card_index]
                if chosen_card.can_play(player.mana_available):
                    player.play(chosen_card)
                    # Call the place_creature function here
                    # summon_lane, summon_row = player.choose_location()
                    # self.game_board.place_creature(
                    #     creature=chosen_card,
                    #     player=player,
                    #     lane=summon_lane,
                    #     row=summon_row
                    # )
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

            # check game end from mana burn
            if self.check_game_end():
                break

            # have the player summon any number of cards
            if isinstance(player, HumanPlayer):
                self.play_cards(player)
            elif isinstance(player, AIPlayer):
                player.play_cards()
            else:
                raise ValueError("Invalid player type")

            print(f"\n{player} attack phase begins.")
            for creature in player.creatures:
                if not creature.tapped:
                    targets = self.get_attackable_targets(creature, player)
                    target = self.choose_target(targets)
                    print(f"{creature} from {player} attacks {target}.")
                    creature.attack(target)

            player.end_turn()
            if self.check_game_end():
                break

            self.next_turn()

    def check_game_end(self):
        # check if the game has ended
        game_over, winner = self.end_game()
        if game_over:
            if winner:
                print(f"\n{winner} wins the game!")
            else:
                print("\nGame is a draw, no winner.")
        return game_over


