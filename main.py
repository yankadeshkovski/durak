import pygame
from deck import Deck
from button import Button
import random

main_menu = True
player1 = False
player2 = False
player3 = False
player4 = False

def display_main_menu(screen):
    screen.fill((0, 128, 128))

    arial_font = pygame.font.SysFont("arialblack", 40)
    arial_font_small = pygame.font.SysFont("arialblack", 20)

    title_surface = arial_font.render("DURAK", 0, (0, 0, 0))
    title_rectangle = title_surface.get_rect(center=(600 // 2, 600 // 2 - 200))
    screen.blit(title_surface, title_rectangle)

    subtitle_surface = arial_font_small.render("Select number of players!", 0, (0, 0, 0))
    subtitle_rectangle = subtitle_surface.get_rect(center=(600 // 2, 600 // 2 - 170))
    screen.blit(subtitle_surface, subtitle_rectangle)

    two_players = Button("2", 37, 200, True, screen, arial_font_small)
    three_players = Button("3", 224, 200, True, screen, arial_font_small)
    four_players = Button("4", 411, 200, True, screen, arial_font_small)

    pygame.display.flip()

def choose_master_suit(deck):
    suit_num = random.randrange(1, 4, 1)
    if suit_num == 1:
        suit_name = "Spades"
    elif suit_num == 2:
        suit_name = "Clubs"
    elif suit_num == 3:
        suit_name = "Hearts"
    else:
        suit_name = "Diamonds"
    
    deck.turn_suit_master(suit_name)
    return suit_name

def transfer_card(deck, vector):
    ran_num = random.randrange(0, len(deck.deck))
    vector.append(deck.deck[ran_num])
    deck.card_remove(deck.deck[ran_num].card_suit, deck.deck[ran_num].card_value)

    return vector

def shuffle_deck(deck, master_suit):
    value_num = random.randrange(15, 27, 1)
    vctr = []
    vctr.append(deck.find_card(master_suit, value_num))
    deck.card_remove(master_suit, value_num)

    for i in range(51):
        vctr = transfer_card(deck, vctr)

    return vctr
    

def main():
    pygame.init()
    screen = pygame.display.set_mode([600, 600])
    pygame.display.set_caption("Durak")

    deck = Deck()
    deck.populate_deck()
    master_suit = choose_master_suit(deck)

    # for i in range(len(deck.deck)):
    #     print(deck.deck[i].suit, deck.deck[i].rank, deck.deck[i].value)

    vctr = shuffle_deck(deck, master_suit)

    for i in range(len(vctr)):
        print(vctr[i].suit, vctr[i].rank, vctr[i].value)

    running = True
    while running:
        if main_menu:
            display_main_menu(screen)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False


if __name__ == '__main__':
    main()
