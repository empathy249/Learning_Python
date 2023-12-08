import random
import my_functions

deck_of_cards = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
player_cards = []
computer_cards = []

def array_to_string(card_array):
    text = ""
    i = 0 
    for card in card_array:
        if i == 0:
            text += card
            i += 1
        else: 
            text += ", "
            text += card
            i += 1
    return text

def show_cards_and_points():
    print(f"Player cards: {array_to_string(player_cards)} with {get_total_points_from(player_cards)} points")
    print(f"Computer cards: {array_to_string(computer_cards)} with {get_total_points_from(computer_cards)} points")


def get_total_points_from(player_card_array):
    point = 0 
    for card in player_card_array:
        if card == "ace":
            point += 11
        elif card == "king" or card == "queen" or card == "jack":
            point += 10
        else:
            if int(card) <11 and int(card) > 1:
                point += int(card)
            else: 
                return point
    return point

def deal_single_card_for(player):
    """Returns card as string, card points as int"""
    if player == "user":
        random_number = random.randint(0, 12)
        random_card = deck_of_cards[random_number]
        player_cards.append(random_card)
    elif player == "computer":
        random_number = random.randint(0, 12)
        random_card = deck_of_cards[random_number]
        computer_cards.append(random_card)

def win_or_lose_checker(player_cards, computer_cards):
    player_points = get_total_points_from(player_cards)
    computer_points = get_total_points_from(computer_cards)
    if player_points == 21:
        show_cards_and_points()
        print("Player wins")
    elif player_points > computer_points and player_points <22 and computer_points <22: 
        show_cards_and_points()
        print("Player wins!")
    elif computer_points > player_points and player_points <22 and computer_points <22:
        show_cards_and_points()
        print("Computer wins!")
    elif player_points > 21:
        show_cards_and_points()
        print(f"That's a bust with {array_to_string(player_cards)} ({computer_points} points). You lose!")
    elif computer_points > 21:
        show_cards_and_points()
        print(f"Computer got {computer_points} points. That's a bust! You win!")

def ask_stay_or_hit():
    choice = input("Would you like to stay or hit: ")
    if choice == "stay":
        print("You picked stay, computer shows second card")
        deal_single_card_for("computer")
        computer_points = get_total_points_from(computer_cards)
        if computer_points == 21: 
            win_or_lose_checker(player_cards, computer_cards)
        elif computer_points > 21: 
            win_or_lose_checker(player_cards, computer_cards)
        elif computer_points > get_total_points_from(player_cards):
            win_or_lose_checker(player_cards, computer_cards)
        else:
            show_cards_and_points()
            while computer_points <22 and computer_points <= get_total_points_from(player_cards):
                print("Computer draws another card")
                deal_single_card_for("computer")
                show_cards_and_points()
                computer_points = get_total_points_from(computer_cards)
            win_or_lose_checker(player_cards, computer_cards)

    elif choice == "hit":
        deal_single_card_for("user")
        show_cards_and_points()
        if get_total_points_from(player_cards) == 21:
            print(f"You hit Black Jack with {array_to_string(player_cards)}. You win!")
        elif get_total_points_from(player_cards) > 21:
            print(f"That's a bust with {array_to_string(player_cards)}. You lose!")
        elif get_total_points_from(player_cards) < 21:
            ask_stay_or_hit()


continue_game = True
play_game = input("Do you want to play blackjack? Y or N: ").lower()

while continue_game == True: 
    deal_single_card_for("user")
    deal_single_card_for("user")
    deal_single_card_for("computer")
    show_cards_and_points()
    player_points = get_total_points_from(player_cards)
    computer_points = get_total_points_from(computer_cards)

    if player_points == 21: 
        print(f"You hit blackjack with {array_to_string(player_cards)}. You win!")
        continue_game = False
    else: 
        ask_stay_or_hit()
    continue_game = False







    



    