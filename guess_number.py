import random
chosen_number = random.randint(1, 100)
atempts = 0
print(chosen_number)
print("Welcom to the Number Guessing Game!"+"\n"+"I'm thinking of a number between 1 and 100.")
game_mode = str(input("Choose a difficulty: 'easy' or 'hard': "))

def guess_number():
   if user_picked == chosen_number:
       print("You guessed it right!")
       return True
   elif user_picked > chosen_number:
         print("Too high!"+ "\n" + "Guess again.")
   elif user_picked < chosen_number:
         print("Too low!"+ "\n" + "Guess again.")
         return False

if game_mode == 'easy':
    atempts = 10
else:
    atempts = 5
    for i in range(1, atempts+1):
        print(f"You have {atempts-1} attempts to guess the number.")
        user_picked = int(input("Make a guess: "))
        if guess_number():
             break 
        else: print("You've run out of guesses. You lose!")
    



