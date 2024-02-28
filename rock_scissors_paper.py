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

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

def display_choices(choices):
    for key, value in choices.items():
        print(f"Type {key} for {value}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "You lose"

choices = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

user = Player("User")
computer = Player("Computer")

while True:
    print(f"{user.name}'s score: {user.score}\n{computer.name}'s score: {computer.score}")
    
    display_choices(choices)
    
    user_choice = int(input("What do you choose? Type the corresponding number. Type 3 to quit.\n"))
    
    if user_choice == 3:
        print("Thanks for playing. Final scores:")
        print(f"{user.name}'s score: {user.score}  {computer.name}'s score: {computer.score}")
        break

    if user_choice not in choices:
        print(f"You typed an invalid number. Please choose again.")
        continue

    print(f"{user.name} chose: {choices[user_choice]}")
    print(game_images[user_choice])
    
    computer_choice = random.randint(0, 2)
    print(f"{computer.name} chose: {choices[computer_choice]}")
    print(game_images[computer_choice])
    result = determine_winner(user_choice, computer_choice)
    print(result)

    if "win" in result:
        user.score += 1
    elif "lose" in result:
        computer.score += 1