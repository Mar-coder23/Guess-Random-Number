#build a Number guessing game, which the user selects a range.
#user selected in range, from A to B which is a int
#random int will  be selected by system and user has to guess that integer in minimum number of guesses.

# Guess a number between 1 and 100
# 45
# answer is higher
# 74 
# answer is lower
# 56 
# DING DING DING, correct

#Imported random library
import random
import sys

# random number function that spits out a number between 1 and 100
def random_num():
    ran_value = random.randint(1, 100)
    return ran_value
random_num()

# function to guess the random number
def guess_num():
    # variable random number is assigned to the random_num() function
    random_number = random_num()
    # variable attempts with the value 10
    attempts = 10
    # While the below statement is true run it
    while True:
        # ask the user for a integer value between 1 and 100
        user_input = int(input("Guess a number between 1 and 100: "))
        # if the input is equal to the same number as the random number, you win
        if user_input == random_number:
            print("Yes, you Nailed it! Good job")
            # since you win, you get asked if you would like to play again
            repeat = input("Would you like to play again? (y/n): ")
            # if you select y, then that means yes and the game will start again
            if repeat == "y":
                guess_num() # restart the guess_num() function
            # else if the answer is n, then say thanks for playing and break out of the while loop
            elif repeat == "n":
                print("Okay, Thanks for playing")
                sys.exit()
            # if the value is not y or n, then print invalid input and ask if you would like to play again
            else:
                print("Invalid input. Try again")
                repeat = input("Would you like to play again? (y/n): ")
            # else if the user input is less than the random number, print Guess higher with the decremented attempts left
        elif user_input < random_number:
            attempts -= 1
            print(f"Guess higher ({attempts} Attempts left)")
            # if its not correct or it is to less, then do else, which is greater than, and says to Guess lower with the decremented attempts left
        else:
            attempts -= 1
            print(f"Guess lower ({attempts} Attempts left)")
            # if the attempts reach from 10 to 0, it means you lose and to call the function again to restart
        if attempts == 0:
                print("You ran out of attempts, you lose")
                guess_num()
        
        
guess_num()


