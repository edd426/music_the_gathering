import json

from card_library import CardLibrary
from game import Game
from ai_player import AIPlayer
from human_player import HumanPlayer


def main():
    # create a card library
    library = CardLibrary()

    # import cards from a JSON file
    library.import_cards("./card_storage.json")

    # create a deck for each player
    player_1_deck = library.create_deck(
        ["Goblin Guide", "Tarmogoyf",
         "Dark Confidant", "Sakura-Tribe Elder", "Birds of Paradise",
         "Eternal Witness"])
    player_2_deck = library.create_deck(
        ["Goblin Guide", "Tarmogoyf",
         "Dark Confidant", "Sakura-Tribe Elder", "Birds of Paradise",
         "Eternal Witness"])

    # create players
    player_1 = AIPlayer("Player 1", player_1_deck, 20)
    player_2 = AIPlayer("Player 2", player_2_deck, 20)

    # create the game
    game = Game([player_1, player_2])

    # run the game
    game.play()

    # determine the winner
    winner = game.get_victorious_player()
    print(f"{winner} wins!")


if __name__ == "__main__":
    main()
