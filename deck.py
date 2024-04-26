from cards import Card

class Deck:
    def __init__(self):
        self.deck = []
        self.size = 0

    def populate_deck(self):
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"] 
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        for s in suits:
            for r in range(len(ranks)):
                self.deck.append(Card(s, ranks[r], values[r], False))

        self.size = 52

    def turn_suit_master(self, suit):
        for i in range(len(self.deck)):
            if self.deck[i].suit is suit:
                self.deck[i].turn_master() 

    # probably same with this
    def find_card(self, suit, value) -> Card:
        for c in range(self.size):
                if self.deck[c].value == value and self.deck[c].suit == suit:
                    return self.deck[c]

    # for some reason doesn't work               
    def card_remove(self, suit, value):
        for c in range(self.size):
                if self.deck[c].value == value and self.deck[c].suit == suit:
                    del self.deck[c]

        self.size -= 1