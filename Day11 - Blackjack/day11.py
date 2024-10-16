from operator import contains

import art
import random

initial_choice = input('''Do you want to play a game of Blackjack? Type 'y' or 'n': ''').lower()

cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def is_ace(input_list):
    return contains(input_list, 11)


def is_blackjack(input_list):
    return is_ace(input_list) and contains(input_list, 10)


def deal_card(cards):
    return random.choice(cards)


def adjust_for_ace(hand, total):
    """ Adjust the value of Aces in the hand if the total is over 21 """
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1  # Replace one Ace from 11 to 1
        total -= 10
    return total


def play_blackjack(cards):
    if initial_choice == "y":
        print(art.logo)
        initial_numbers = random.choices(cards, k=2)
        com_initial_numbers = random.choices(cards, k=2)
        user_sum = -1
        com_sum = -1
        if is_blackjack(initial_numbers):
            print("You have Blackjack. You Win!!!")
            return
        elif is_blackjack(com_initial_numbers):
            print("Computer has Blackjack. You Lose!!!!")
            return
        should_continue = "y"
        while should_continue == "y":
            user_sum = sum(initial_numbers)
            com_sum = sum(com_initial_numbers)
            print(f"Your cards: {initial_numbers}, current score: {user_sum}")
            print(f"Computer's first card is {com_initial_numbers[0]}")
            if user_sum > 21:
                user_sum = adjust_for_ace(initial_numbers, user_sum)
            if user_sum > 21:
                print(f"Your total went overboard with {initial_numbers}. You lose!!!")
                break
            should_continue = continue_game(cards, initial_numbers, user_sum)

        if should_continue == "n":
            while com_sum < 17:
                com_new_card = deal_card(cards)
                com_initial_numbers.append(com_new_card)
                com_sum += com_new_card
            com_sum = adjust_for_ace(com_initial_numbers, com_sum)  # Adjust dealer's hand if needed
            compare_result(com_initial_numbers, com_sum, initial_numbers, user_sum)


def continue_game(cards, initial_numbers, user_sum):
    should_continue = input('''Type 'y' to get another card, type 'n' to pass: ''').lower()
    if should_continue == "y":
        user_new_card = deal_card(cards)
        initial_numbers.append(user_new_card)
        user_sum += user_new_card
        return should_continue
    else:
        return "n"


def compare_result(com_initial_numbers, com_sum, initial_numbers, user_sum):
    print(f"Your final hand: {initial_numbers}, final score: {user_sum}")
    print(f"Computer's final hand: {com_initial_numbers}, final score: {com_sum}")
    if com_sum > 21:
        print(f"Computer has gone overboard with {com_initial_numbers}. You Win!")
        return "n"
    else:
        if com_sum > user_sum:
            print(f"Computer total is more than yours {com_initial_numbers}. You lose!!!")
            return "n"
        elif com_sum == user_sum:
            print(
                f"Game is draw!!!. Computer have {com_initial_numbers} and You have {initial_numbers}")
            return "n"
        else:
            print(f"You win the game having {initial_numbers}!!!")
            return "n"


play_blackjack(cards=cards_list)
