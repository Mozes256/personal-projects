import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards_list):
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)

def deal_card():
    return random.choice(cards)

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "Computer has Blackjack. You lose"
    elif player_score == 0:
        return "You have Blackjack. You win"
    elif player_score > 21:
        return "You went over 21. You lose"
    elif computer_score > 21:
        return "Computer went over 21. You win"
    elif player_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)

    player_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to get another card, 'n' to pass: ")
            if choice == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()
