import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if 0 <= user_choice <= 2:
    print("You chose:")
    print(options[user_choice])

    computer_choice = random.randint(0,2)
    if user_choice == 2 and computer_choice == 0:
        print("Computer chose:")
        print(options[computer_choice])
        print("You lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("Computer chose:")
        print(options[computer_choice])
        print("You win!")
    elif user_choice > computer_choice:
        print("Computer chose:")
        print(options[computer_choice])
        print("You win!")
    elif user_choice < computer_choice:
        print("Computer chose:")
        print(options[computer_choice])
        print("You lose!")
    elif user_choice == computer_choice:
        print("Computer chose:")
        print(options[computer_choice])
        print("It's a draw!")
else:
    print("You entered invalid choice, You lose!")
