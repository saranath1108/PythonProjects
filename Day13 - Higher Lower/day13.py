import art
import random
import game_data


def get_name(obj):
    return obj["name"]


def get_description(obj):
    return obj["description"]


def get_country(obj):
    return obj["country"]


def get_follower_count(obj):
    return obj["follower_count"]


def compare_follower_count(guess, ffc, sfc):
    if ffc > sfc:
        return guess == "A"
    else:
        return guess == "B"


def format_data(obj):
    name = obj["name"]
    description = obj["description"]
    country = obj["country"]
    return f"{name}, a {description}, from {country}"


def higher_lower():
    # should_continue is a flag that determine, if game should be continued or stopped
    should_continue = True
    print(art.logo)
    # number of times user guess the right option.
    hit_count = 0
    first_choice_data = random.choice(game_data.data)
    second_choice_data = random.choice(game_data.data)
    while should_continue:
        if hit_count > 0:
            print(f"You're right! Current score: {hit_count}")
            first_choice_data = second_choice_data
            second_choice_data = random.choice(game_data.data)

        print(f"Compare A: {format_data(first_choice_data)}")
        print(art.vs)
        print(f"Against B: {format_data(second_choice_data)}")
        first_choice_follower_count = get_follower_count(first_choice_data)
        secnd_choice_follower_count = get_follower_count(second_choice_data)

        choice = input('''Who has more followers? Type either 'A' or 'B' to guess or press 'E' to exit the game: ''')

        print("\n"*20)
        print(art.logo)

        if choice == "E":
            should_continue = False
            print(f"Thank you playing the game. Your score is {hit_count}")
        elif choice != "A" and choice != "B":
            should_continue = False
            print(f"Sorry, that's wrong. Your score is : {hit_count}")
        elif choice == "A" or choice == "B":
            should_continue = compare_follower_count(choice, first_choice_follower_count, secnd_choice_follower_count)
            if should_continue:
                hit_count += 1
            else:
                print(f"Sorry, that's wrong. Your score is : {hit_count}")
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Your score is : {hit_count}")


higher_lower()
