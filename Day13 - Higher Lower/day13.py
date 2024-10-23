import art
import random
import game_data

print(art.logo)


def get_name(obj):
    return obj["name"]


def get_description(obj):
    return obj["description"]


def get_country(obj):
    return obj["country"]


def get_follower_count(obj):
    return obj["follower_count"]


def higher_lower():
    first_choice_data = random.choice(game_data.data)
    second_choice_data = random.choice(game_data.data)
    # should_continue is a flag that determine, if game should be continued or stopped
    should_continue = True
    # number of times user guess the right option.
    hit_count = 0
    print(
        f"Compare A: {get_name(first_choice_data)}, a {get_description(first_choice_data)}, from {get_country(first_choice_data)}")
    print(art.vs)
    print(
        f"Compare B: {get_name(second_choice_data)}, a {get_description(second_choice_data)}, from {get_country(second_choice_data)}")
    first_choice_follower_count = get_follower_count(first_choice_data)
    secnd_choice_follower_count = get_follower_count(second_choice_data)
    while should_continue:
        if hit_count > 0:
            print(f"You're right! Current score: {hit_count}")
        choice = input('''Who has more followers? Type either 'A' or 'B' to guess or press 'E' to exit the game: ''')

        if choice == "E":
            should_continue = False
            print(f"Thank you playing the game. Your score is {hit_count}")
        elif choice != "A" and choice != "B":
            should_continue = False
            print(f"Sorry, that's wrong. Your score is : {hit_count}")
        else:
            if choice == "A" and first_choice_follower_count >= secnd_choice_follower_count:
                hit_count += 1
                second_choice_data = random.choice(game_data.data)
            elif choice == "B" and secnd_choice_follower_count >= first_choice_follower_count:
                hit_count += 1
                first_choice_data = second_choice_data
                second_choice_data = random.choice(game_data.data)
            else:
                should_continue = False
                print(f"Sorry, that's wrong. Your score is : {hit_count}")


higher_lower()
