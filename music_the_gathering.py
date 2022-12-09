import argparse
from player import Player
from deck import Deck
from game import Game
from card import Card


def create_deck():
    # define the cards in the deck
    cards = [
        Card("Lightning Bolt", "Instant", ["Deal 3 damage to target creature or player"], 1),
        Card("Goblin Guide", "Creature", ["Whenever Goblin Guide attacks, defending player reveals the top card of their library. If it's a land card, that player puts it into their hand"], 1),
        Card("Blood Moon", "Enchantment", ["Nonbasic lands are Mountains"], 2),
    ]

    # create the player's deck
    deck = Deck(cards)
    return deck


# define the command line arguments and options
parser = argparse.ArgumentParser()
parser.add_argument("--player1", help="name of player 1", default="Player 1")
parser.add_argument("--player2", help="name of player 2", default="Player 2")

# parse the command line arguments
args = parser.parse_args()

# create the players
player1 = Player(args.player1, create_deck(), life=20)
player2 = Player(args.player2, create_deck(), life=20)

# create and start the game
game = Game([player1, player2])
game.play()
