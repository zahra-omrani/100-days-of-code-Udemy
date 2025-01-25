from game_data import data
import random
#pick two random data 


def game_choices():
    SCORE = 0
    round = 0
#show the description of the choices as A and B
    while True:
        if round == 0:
            INDEX_A = random.randint(0,49)
            INDEX_B = random.choice(list(filter(lambda ele: ele != INDEX_A, range(0,50))))
        else:
            INDEX_B = random.choice(list(filter(lambda ele: ele != INDEX_A, range(0,50))))
        print("A: the first choice is " + data[INDEX_A]["name"]+" which is a "+ data[INDEX_A]['description']+" from "+ data[INDEX_A]['country'])
        print("B: the second choice is " + data[INDEX_B]["name"]+" which is a "+ data[INDEX_B]['description']+" from "+ data[INDEX_B]['country'])

        print(data[INDEX_A]['follower_count'])
        print(data[INDEX_B]['follower_count'])

        user_choice = input("Which one do you think have more followers A or B?")
        #other_choice_index =0
        

        if user_choice == 'A':
            user_choice_index = INDEX_A
            other_choice_index = INDEX_B
        else :
            user_choice_index = INDEX_B 
            other_choice_index = INDEX_A
        

        # print(user_choice_index)
        # print(other_choice_index)

        if  data[user_choice_index]['follower_count'] < data[other_choice_index]['follower_count']:
            print(f"Sorry you lost, Your Score is: {SCORE}")
            break
        else:
            SCORE+=1
            INDEX_A = user_choice_index
            round+=1
            print(f"It is correct. Your Final Score is: {SCORE}")
            continue
        
game_choices()
#ask the user to guess which one has more followers
#compare the follower of the user choice with the other choice
#if the user is right, add 1 to the score and show the next two choices
#else show the score and end the game