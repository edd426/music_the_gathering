class CardValueCalculator:
    def __init__(self, attack_weight=1, defense_weight=1, ability_weight=1,
                 cost_weight=-2):
        self.attack_weight = attack_weight
        self.defense_weight = defense_weight
        self.ability_weight = ability_weight
        self.cost_weight = cost_weight

    def calculate_value(self, card):
        score = self.attack_weight * card.attack_value + \
                self.defense_weight * card.defense_value + \
                self.ability_weight * len(card.abilities) + \
                self.cost_weight * card.mana_cost
        return score