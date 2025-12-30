import random

def check_guess(guess, actual):
    if guess > actual:  
        return "TOO HIGH! TRY AGAIN!"
    elif guess < actual: 
        return "too low! try again!"
    else:
        return "CORRECTTTTTTTTTTTTTT"
    

print("""WELCOME TO NUMBER GUESSING GAME!
HERE YOU HAVE TO GUESS ANY NUMBER BETWEEN 1-20 
AND YOU'LL HAVE ONLY 5 LIVES""")

actual_num = random.randint(1, 20)
count = 0

while True:
    user_guess = int(input("What's your guess? "))
    result = check_guess(user_guess, actual_num)
    print(result)
    count += 1
    print(f"You have {5 -count} lives left.")
   
    if result == "CORRECTTTTTTTTTTTTTT":
        print(f"You guessed it right in {count} guesses.")
        break
    if count == 5:
        print("YOU LOSE")
        break
    
