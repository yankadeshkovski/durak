class Card:
    def __init__(self, suit, rank, value, master):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.master = master

    def turn_master(self):
        self.master = True
        self.value += 13

    def card_value(self):
        return self.value
    
    def card_rank(self):
        return self.rank
    
    def card_suit(self):
        return self.suit
