from card_value_calculator import CardValueCalculator
from card_library import CardLibrary

# create a card library
library = CardLibrary()

# import cards from a JSON file
library.import_cards("./card_storage.json")

card_calc = CardValueCalculator(ability_weight=0)

# create a deck for each player
player_1_deck = library.create_deck(
    ["Goblin Guide", "Tarmogoyf",
        "Dark Confidant", "Sakura-Tribe Elder", "Birds of Paradise",
        "Eternal Witness"])
player_2_deck = library.create_deck(
    ["Goblin Guide", "Tarmogoyf",
        "Dark Confidant", "Sakura-Tribe Elder", "Birds of Paradise",
        "Eternal Witness"])

for card in library.cards:
    card.print_stats()
    print(f"card value: {card_calc.calculate_value(card)}")

