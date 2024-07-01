print('Welcome to the treasure island. Your mission is to find the treasure')
choice1 = input("Do you want to go to the left or right?")
if choice1.lower() == 'right':
    print('Game Over!')
elif choice1.lower() == 'left':
    choice2 = input("Do you want to swim or wait?")
    if choice2.lower() == 'swim':
        print('Game Over')
    elif choice2.lower() == 'wait':
        choice3 = input("which door?")
        if choice3.lower() == 'red':
            print('Game Over!')
        elif choice3.lower() == 'blue':
            print ('Game Over!')
        elif choice3.lower() == 'yellow':
            print ('You Win!')



