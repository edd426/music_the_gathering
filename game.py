import random


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
        if len(alive) == 1:
            return alive[0]
        return None

    def get_attackable_targets(self, attacking_player):
        other_players = [p for p in self.players
                         if p != attacking_player]
        opposing_creatures = [c for p in other_players for c in p.creatures]

        return other_players + opposing_creatures

    def choose_target(self, targets):
        return random.choice(targets)

    def choose_card(self, player):
        print("Your hand:")
        for i, card in enumerate(player.hand):
            print(f"{i + 1}. {card}")
        choice = input("Enter the number of the card you want to play: ")
        try:
            # convert the user's input to an index in the player's hand
            card_index = int(choice) - 1
            return player.hand[card_index]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            return self.choose_card(player)

    def play(self):
        # main game loop
        while True:
            player = self.players[self.current_player]

            # generate mana
            player.generate_mana()
            print(f"\n{player} begins their turn. "
                  + f"They have {player.mana_available} mana.")

            # draw a card
            drawn_card = player.draw()
            print(f"{player} draws {drawn_card}.")

            chosen_card = self.choose_card(player)
            # check if the player can play the card
            if player.mana_available >= chosen_card.mana_cost:
                player.play(chosen_card)
                player.mana_available -= chosen_card.mana_cost
                print(f"{player} plays {chosen_card}.")

            for creature in player.get_untapped_creatures():
                targets = self.get_attackable_targets(player)
                target = self.choose_target(targets)
                print(f"{creature} from {player} attacks {target}.")
                creature.attack(target)

            player.end_turn()
            # check if the game has ended
            winner = self.end_game()
            if winner is not None:
                print(f"{winner} wins the game!")
                break

            self.next_turn()