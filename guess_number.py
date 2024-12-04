import random
chosen_number = random.randint(1, 100)
game_mode = input("Choose game mode: easy or hard: ")
user_picked = int(input("Enter your guess: "))
if game_mode == "easy":
    chosen_number = random.randint(1, 50)
    print("You have 10 attempts to guess the number.")
print(chosen_number)
user_picked = 0



def guess_number():
   if user_picked == chosen_number:
       print("You guessed it right!")
       return
   elif user_picked > chosen_number:
         print("Too high!")
   elif user_picked < chosen_number:
         print("Too low!")