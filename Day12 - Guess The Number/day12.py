import random
import art

print(art.logo)

random_number = random.randint(1,100)

def guess_the_number():
    print("Welcome the Number Guessing game!!!")
    print("I am thinking of number between 1 and 100")
    choice = input('''Choose a difficulty. Type 'easy' or 'hard': ''').lower()

    if choice == "easy":
        number_of_choices = 10
    elif choice == "hard":
        number_of_choices = 5
    else:
        print("Invalid choice!")
        return

    while number_of_choices > 0:
        print(f"You have {number_of_choices} attempts remaining to guess the number")
        guess_number = int(input("Make a guess: "))
        if guess_number > random_number:
            print("Too high!!!")
            print("Guess Again")
        elif guess_number < random_number:
            print("Too Low!!!")
            print("Guess Again")
        elif guess_number == random_number:
            print(f"You got it! The answer was {random_number}")
            return
        number_of_choices -=1
    if number_of_choices == 0:
        print("You've run out of guesses, you lose.")


guess_the_number()