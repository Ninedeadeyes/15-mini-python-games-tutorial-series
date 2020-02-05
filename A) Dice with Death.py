import random   


# A function is a block of organized,
# reusable code that is used to perform a single,
# related action

# A function will need to be 'called' before it does anything
# eg: intro()


def intro():
    print("You are playing dice with death")
    print("Win and live another day, lose and your soul is doomed")

    input("press enter to continue")

def game():
    print("death rolls first")
    death_roll=random.randint(1,12)   # 'randint' is an inbuilt method of random
    print( "death rolls",death_roll)  # A method is a function that is tied
    input("press enter to continue")  # to an object 
    your_roll=random.randint(1,12)
    print("you roll",your_roll)
    input("press enter to continue")

    while death_roll == your_roll:
        print("you will need to play again")
        game()


    if death_roll>your_roll:
        print("You lose the game and your life")
        input("press enter to play again")
        intro()
        game()

    if your_roll>death_roll:
        print("You win and live another day")
        input("press enter to play again")
        intro()
        game()

intro()
game()
    
