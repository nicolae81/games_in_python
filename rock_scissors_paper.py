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

game_images = [rock, paper, scissors]

user_score = 0
computer_score = 0

while True:
    # display current score
    print(f"Your score: {user_score}\nComputer's score: {computer_score}")

    user_choice = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
              "For quiting the game type 3.\n"))

    # Check if the user wants to quit # Nr. 3 from the keyboard is for quiting the game.
    if user_choice == 3:
        print("Thanks for playing. Final scores:")
        print(f"Your score: {user_score}  Computer score: {computer_score}")
        break

    # Validate user choice
    if user_choice not in [0, 1, 2]:
        print(f"You typed an invalid number. Please choose again.")
        continue

    # Get computer choice    
    computer_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(game_images[computer_choice])

    
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
        
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
        user_score += 1
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
        computer_score += 1
    elif computer_choice > user_choice:
        print("You lose")
        computer_score += 1
    elif user_choice > computer_choice:
        print("You win!")
        user_score += 1
    elif computer_choice == user_choice:
        print("It's a draw")
