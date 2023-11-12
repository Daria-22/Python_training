import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    while True:
        # Get user input
        user_guess = int(input("Enter your guess (between 1 and 100): "))

        # Compare user's guess with the secret number
        if user_guess == secret_number:
            print("Success! You got it.")
            break
        elif user_guess < secret_number:
            print("Too low. Try a bigger number.")
        else:
            print("Too high. Try something smaller.")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? Type 'yes' to play again, or '0' to exit: ")

    if play_again.lower() == 'yes':
        guess_the_number()
    elif play_again == '0':
        print("Thanks for playing. Goodbye!")
    else:
        print("Invalid input. Exiting the game.")

# Start the game
guess_the_number()
 
 #I did not think that I could just make a function and call it after the loop is over and after I ask the 
 #user for input

    