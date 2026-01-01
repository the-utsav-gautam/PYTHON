import random

try:
    with open("rps_highscore.txt", "r") as f:
        high_score = int(f.read())
except:
    high_score = 0

print(f"--- ROCK PAPER SCISSORS: 10 ROUND CHALLENGE ---")
print(f"--- THE CURRENT RECORD IS: {high_score} WINS ---")

options = ["rock", "paper", "scissors"]
user_wins = 0

for round_num in range(1, 11):
    print(f"\nROUND {round_num}")
    
    computer_choice = random.choice(options)
    
    try:
        user_choice = input("Pick Rock, Paper, or Scissors: ").lower()
        if user_choice not in options:
            print("That's not a valid move! Skipping this round.")
            continue
    except:
        continue

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You won this round!")
        user_wins += 1
    else:
        print("Computer wins this round!")

print("\n" + "="*30)
print(f"GAME OVER! You won {user_wins} rounds.")

if user_wins > high_score:
    print(f"NEW RECORD! You beat the old score of {high_score}!")
    with open("rps_highscore.txt", "w") as f:
        f.write(str(user_wins))
else:
    print(f"The record stays at {high_score}. Better luck next time!")
