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

def play_blackjack(cards):
    if initial_choice == "y":
        print(art.logo)
        initial_numbers = random.choices(cards, k=2)
        com_initial_numbers = random.choices(cards, k=2)
        should_continue = "y"
        user_sum = sum(initial_numbers)
        com_sum = sum(com_initial_numbers)
        print(f'''       Your cards: {initial_numbers}, current score: {user_sum}''')
        print(f'''       Computer's first card is {com_initial_numbers[0]}''')
        while should_continue == "y":
            if is_blackjack(com_initial_numbers) or is_blackjack(initial_numbers):
                if is_blackjack(com_initial_numbers):
                    print("Computer has Blackjack. You Lose!!!!")
                    should_continue = "n"
                elif is_blackjack(initial_numbers) and not is_blackjack(com_initial_numbers):
                    print("You have Blackjack. You Win!!!")
                    should_continue = "n"
            else:
                if user_sum > 21:
                    if not is_ace(initial_numbers):
                        print(f"Your total went overboard with {initial_numbers}. You lose!!!")
                        should_continue = "n"
                    else:
                        if 11 in initial_numbers:
                            initial_numbers.remove(11)
                            initial_numbers.append(1)
                            user_sum-=10
                        if user_sum > 21:
                            print(f"Your total went overboard with {initial_numbers}. You lose!!!")
                            should_continue = "n"
                        else:
                            should_continue = continue_game(cards, com_initial_numbers, com_sum, initial_numbers,
                                                            user_sum)
                else:
                    should_continue = continue_game(cards, com_initial_numbers, com_sum, initial_numbers, user_sum)


def continue_game(cards, com_initial_numbers, com_sum, initial_numbers, user_sum):
    should_continue = input('''Type 'y' to get another card, type 'n' to pass: ''').lower()
    if should_continue == "y":
        user_new_card = deal_card(cards)
        initial_numbers.append(user_new_card)
        user_sum += user_new_card
        return should_continue
    else:
        while com_sum < 17:
            com_new_card = deal_card(cards)
            com_initial_numbers.append(com_new_card)
            com_sum += com_new_card
        return compare_result(com_initial_numbers, com_sum, initial_numbers, user_sum)



def compare_result(com_initial_numbers, com_sum, initial_numbers, user_sum):
    if com_sum > 21:
        print(f"Computer has gone overboard with {com_initial_numbers}. You Win!")
        return "n"
    else:
        if com_sum > user_sum:
            print(f"You went overboard with {initial_numbers}. You lose!!!")
            return "n"
        elif com_sum == user_sum:
            print(
                f"Game is draw!!!. Computer have {com_initial_numbers} and You have {initial_numbers}")
            return "n"
        else:
            print(f"You win the game having {initial_numbers}!!!")
            return "n"


play_blackjack(cards=cards_list)
