import random

wins = 0
draw = 0
losses = 0

options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Choose your weapon: Rock/Paper/Scissors/ or Q to quit ")
    if user_input.lower() == "q":
        print("Thanks for playing")
        break

    if user_input.lower() not in options:
        print("Please choose, Rock, Paper or Scissors")
        continue
    
    random_number = random.randint(0, 2)
    # rock is 0, paper is 1, and scissors is 2
    computer_guess = options[random_number]
    print(f"Computer picked {computer_guess}")

    if user_input == "rock" and computer_guess == "scissors":
        print("You win!")
        wins += 1
    elif user_input == "paper" and computer_guess == "rock":
        print("You win!")
        wins += 1
    elif user_input == "scissors" and computer_guess == "paper":
        print("You win!")
        wins += 1
    elif user_input == computer_guess:
        print("It's a draw!")
        draw += 1
    else:
        print("You lose!")
        losses += 1

print(f"The final score is Computer {losses} to You {wins} and {draw} draws!")
print("See you next time!")