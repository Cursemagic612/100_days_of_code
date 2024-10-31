#My personal capstone project for Blackjack game.
#It does not follow all the rules but some of it.
#Any comments or feedback are welcomed. (I know the code are not optimized and only a few have input error checks)
'''
Our Blackjack Game House Rules:

The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer.
'''

import art
import random
import os

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_card():
    card_selected = cards[random.randint(0, 12)]
    return card_selected

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 100)

def win_or_lose(total_sum_player, total_sum_computer, round_number):
    if total_sum_player > 21:
        return "lose"
    elif total_sum_player < 21 and total_sum_computer > 21:
        return "win"
    elif total_sum_player <= 21 and total_sum_computer < 21 and round_number == 1:
        return "continue"
    elif total_sum_player <=21 and total_sum_computer <= 21 and total_sum_computer < total_sum_player:
        return "higher_win"
    elif total_sum_computer <=21 and total_sum_player <= 21 and total_sum_computer > total_sum_player:
        return "lower_lose"
    elif total_sum_computer <=21 and total_sum_player <= 21 and total_sum_computer == total_sum_player:
        return "draw"


def print_result(decision):
    if decision == "lose":
        print("You went over. You lose")
    elif decision == "win":
        print("Computer went over. You win")
    elif decision == "draw":
        print("It is a draw. NO ONE WINS.")
    elif decision == "continue":
        return
    elif decision == "higher_win":
        print("You have higher numbers. You win")
    elif decision == "lower_lose":
        print("Computer have higher numbers. You lose")

while play == "y":
    eleven_counter = 0
    player = []
    computer = []
    confirm = 0
    continue_statement = "y"
    draw_decision = "continue"
    round_number = 0
    print(art.logo)

    comp_card = get_card()
    computer.append(comp_card)
    computer_counter = 1

    total_value = 0
    alt_total_value = 0

    player_counter = 0
    while player_counter < 2:
        player_card = get_card()
        player.append(player_card)
        player_counter += 1

    round_number = 1
    #If player get two aces in a row for first 2 cards
    if player[0] == 11:
        if player[1] == 11:
            player[1] = 1
    player_value = ", ".join(map(str, player))
    total_sum_player = sum(player)
    total_sum_computer = sum(computer)
    print(f"Your cards: {player_value}, current score: {total_sum_player}")
    print(f"Computer's first card: {computer[0]}")
    decision = win_or_lose(total_sum_player, total_sum_computer,round_number)

    while draw_decision == "continue":
        if decision == "continue":
            continue_statement = input("Type 'y' to get another card, type 'n' to pass: ")
            while continue_statement != "y" and continue_statement != "n":
                continue_statement = input("Invalid choice! \n Type 'y' to get another card, type 'n' to pass: ")

            if continue_statement == "y":
                player_card = get_card()
                player.append(player_card)

                for values in player:
                    total_sum_player = sum(player)
                    if player_counter >= 2 and values == 11 and total_value > 21:
                        player[player_counter] = 1
                    player_counter += 1

                player_value = ", ".join(map(str, player))
                total_sum_player = sum(player)
                print(f"Your cards: {player_value}, current score: {total_sum_player}")
                print(f"Computer's first card: {computer[0]}")
                decision = win_or_lose(total_sum_player, total_sum_computer, round_number)

            elif continue_statement == "n":
                draw_decision = "dont_continue"
                while total_sum_computer < 17:
                    comp_card = get_card()
                    computer.append(comp_card)

                    for values in player:
                        if computer[0] == 11:
                            if computer[1] == 11:
                                computer[1] = 1
                        total_sum_computer = sum(computer)
                        if computer_counter >= 2 and values == 11 and total_value > 21:
                            player[player_counter] = 1
                        computer_counter += 1


                    computer_value = ", ".join(map(str, computer))
                    total_sum_computer = sum(computer)
                print(f"Your cards: {player_value}, current score: {total_sum_player}")
                print(f"Computer's cards: {computer_value}, final score: {total_sum_computer}")
                draw_decision = "dont_continue"
        elif decision == "lose":
            draw_decision = "dont_continue"

        round_number += 1



    if draw_decision == "dont_continue":
        decision = win_or_lose(total_sum_player, total_sum_computer,round_number)
        print_result(decision)
        if decision=="higher_win" and total_sum_player == 21:
            print("Black Jack!")

    while confirm < 1:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play == "y" or play == "n":
            confirm = 1
    if play == "y":
        clear_screen()
        counter = 0
