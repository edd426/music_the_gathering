import random
import sys

from card_library import CardLibrary
from game import Game
from ai_player import AIPlayer
from human_player import HumanPlayer


def main():
    # print the game title
    print("Music: The Gathering")

    # set and print random seed
    # seed = random.randrange(sys.maxsize)
    seed = 0
    random.seed(seed)
    print(f"Game seed: {seed}")

    # create a card library
    library = CardLibrary()

    # import cards from a JSON file
    library.import_cards("./card_storage.json")

    # create a deck for each player
    player_1_deck = library.create_deck(  # flying deck
        ["Birds of Paradise", "Pop Pegasus", "Rap Raven",
         "Jazz Sparrow", "Rock Drake",
         "Harmony Angel"])
    player_2_deck = library.create_deck(
        ["Goblin Guide", "Tarmogoyf",
         "Dark Confidant", "Sakura-Tribe Elder", "Birds of Paradise",
         "Eternal Witness"])

    # create players
    player_1 = HumanPlayer("Player 1", player_1_deck, 20)
    player_2 = AIPlayer("Player 2", player_2_deck, 20)

    # create the game
    game = Game([player_1, player_2])

    # run the game
    game.play()

    a = 1


if __name__ == "__main__":
    main()
