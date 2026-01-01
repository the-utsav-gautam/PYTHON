import random

try:
    with open("highscore.txt", "r") as f:
        best_score = int(f.read())
except:
    best_score = 0

def check_guess(guess, actual):
    if guess > actual:
        return "TOO HIGH! TRY AGAIN!"
    elif guess < actual:
        return "too low! try again!"
    else:
        return "CORRECTTTTTTTTTTTTTT"

print(f"""WELCOME TO NUMBER GUESSING GAME!
-----------------------------------
CURRENT HIGH SCORE: {best_score} guesses
-----------------------------------
HERE YOU HAVE TO GUESS ANY NUMBER BETWEEN 1-20
AND YOU'LL HAVE ONLY 5 LIVES""")

actual_num = random.randint(1, 20)
count = 0

while True:

    try:
        user_guess = int(input("What's your guess? "))
    except ValueError:
        print("Invalid input! Please enter a number (digits only).")
        # Continue the loop to allow the user to enter a valid guess
        continue

    result = check_guess(user_guess, actual_num)
    print(result)
    count += 1

    if result == "CORRECTTTTTTTTTTTTTT":
        print(f"You guessed it right in {count} guesses.")

        
        if best_score == 0 or count < best_score:
            print(f"NEW HIGH SCORE! You beat the old record of {best_score}!" if best_score != 0 else "NEW HIGH SCORE!")
            with open("highscore.txt", "w") as f:
                f.write(str(count))
            best_score = count # Update best_score in memory for current session
        break

    if count == 5:
        print(f"YOU LOSE! The number was {actual_num}")
        break

    print(f"You have {5 - count} lives left.")
