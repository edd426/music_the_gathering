import json

from card_library import CardLibrary
from game import Game
from player import Player

def main():
    # create a card library
    library = CardLibrary()

    # import cards from a JSON file
    library.import_cards("./card_storage.json")

    # create a deck for each player
    player_1_deck = library.create_deck(["Lightning Bolt", "Goblin Guide", "Blood Moon", "Tarmogoyf", "Dark Confidant", "Sakura-Tribe Elder"])
    player_2_deck = library.create_deck(["Lightning Bolt", "Goblin Guide", "Blood Moon", "Tarmogoyf", "Dark Confidant", "Sakura-Tribe Elder"])

    # create players
    player_1 = Player("Player 1", player_1_deck, 20)
    player_2 = Player("Player 2", player_2_deck, 20)

    # create the game
    game = Game([player_1, player_2])

    # run the game
    while not game.is_over():
        game.play_turn()

    # determine the winner
    winner = game.get_winner()
    print(f"{winner} wins!")

if __name__ == "__main__":
    main()
