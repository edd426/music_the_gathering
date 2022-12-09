class Player:
    def __init__(self, name, deck, life, attack=0, defense=0):
        self.name = name
        self.deck = deck
        self.life = life
        self.hand = []
        self.mana = 0
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return self.name

    def draw(self):
        # draw a card from the player's deck
        card = self.deck.draw()
        self.hand.append(card)
        return card

    def play(self, card):
        # play a card from the player's hand
        self.hand.remove(card)
        card.play()

    def take_damage(self, amount):
        # reduce the player's life total by the given amount
        self.life -= amount

    def is_dead(self):
        # return True if the player's life total is 0 or less
        return self.life <= 0

    def add_mana(self):
        # add 1 mana to the player's mana pool
        self.mana += 1