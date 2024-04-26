import pygame
from deck import Deck
from button import Button
import random
import constants as co

main_menu = True
game_screen = False
rules_screen = False
players_two = False
players_three = False
players_four = False

def falsifying():
    global main_menu, game_screen, rules_screen, players_four, players_three, players_two
    main_menu = False
    game_screen = False
    rules_screen = False
    players_four = False
    players_three = False
    players_two = False

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

    two_players = Button("2", 37, 200, True, screen, arial_font_small, 150, 300)
    three_players = Button("3", 224, 200, True, screen, arial_font_small, 150, 300)
    four_players = Button("4", 411, 200, True, screen, arial_font_small, 150, 300)
    rules_button = Button("Rules", 250, 525, True, screen, arial_font_small, 100, 50)

    global main_menu, game_screen, players_two, players_three, players_four, rules_screen
    if two_players.check_click():
        falsifying()
        game_screen = True
        players_two = True
    if three_players.check_click():
        falsifying()
        game_screen = True
        players_three = True
    if four_players.check_click():
        falsifying()
        game_screen = True
        players_four = True
    if rules_button.check_click():
        falsifying()
        rules_screen = True
    
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

# write the rules of the game here when i have the chance to do that
def display_rules_screen(screen):
    screen.fill((15, 240, 20))
    pygame.display.flip()

def display_game_screen(screen):
    screen.fill((0, 128, 128))
    arial_font = pygame.font.Font("CARDC___.TTF", 20)

    if players_two:
        title_surface = arial_font.render('P1', 0, (0, 0, 0))
        title_rectangle = title_surface.get_rect(center=(20, 300))
        screen.blit(title_surface, title_rectangle)

        title_surface2 = arial_font.render('P2', 0, (0, 0, 0))
        title_rectangle2 = title_surface.get_rect(center=(580, 300))
        screen.blit(title_surface2, title_rectangle2)
    if players_three:
        title_surface = arial_font.render('P1', 0, (0, 0, 0))
        title_rectangle = title_surface.get_rect(center=(20, 300))
        screen.blit(title_surface, title_rectangle)

        title_surface2 = arial_font.render('P2', 0, (0, 0, 0))
        title_rectangle2 = title_surface.get_rect(center=(580, 300))
        screen.blit(title_surface2, title_rectangle2)

        title_surface3 = arial_font.render('P3', 0, (0, 0, 0))
        title_rectangle3 = title_surface.get_rect(center=(300, 580))
        screen.blit(title_surface3, title_rectangle3)
    if players_four:
        title_surface = arial_font.render('P1', 0, (0, 0, 0))
        title_rectangle = title_surface.get_rect(center=(20, 300))
        screen.blit(title_surface, title_rectangle)

        title_surface2 = arial_font.render('P3', 0, (0, 0, 0))
        title_rectangle2 = title_surface.get_rect(center=(580, 300))
        screen.blit(title_surface2, title_rectangle2)

        title_surface3 = arial_font.render('P4', 0, (0, 0, 0))
        title_rectangle3 = title_surface.get_rect(center=(300, 580))
        screen.blit(title_surface3, title_rectangle3)

        title_surface3 = arial_font.render('P2', 0, (0, 0, 0))
        title_rectangle3 = title_surface.get_rect(center=(300, 20))
        screen.blit(title_surface3, title_rectangle3)

    pygame.display.flip()

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

    # for i in range(len(vctr)):
    #     print(vctr[i].suit, vctr[i].rank, vctr[i].value)

    running = True
    while running:
        if main_menu:
            display_main_menu(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        if rules_screen:
            display_rules_screen(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        if game_screen:
            display_game_screen(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


if __name__ == '__main__':
    main()
