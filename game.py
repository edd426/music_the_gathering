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

    def play(self):
        # main game loop
        while True:
            player = self.players[self.current_player]

            # draw a card
            card = player.draw()
            print(f"{player} draws {card}.")

            # check if the player can play the card
            if player.mana >= card.mana_cost:
                player.play(card)
                player.mana -= card.mana_cost
                print(f"{player} plays {card}.")

            # check if the game has ended
            winner = self.end_game()
            if winner is not None:
                print(f"{winner} wins the game!")
                break

            self.next_turn()