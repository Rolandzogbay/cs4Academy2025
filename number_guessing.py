import random

def user_guess_input():
    def guess_game():
        while True:
            try:
                # Prompt user for a guess
                user_guess = int(input("Hi, can you guess the number I'm thinking about between 1-10? "))
                GUESS_VALUE = random.randint(1, 10)  # Generate a random number between 1 and 10

                if user_guess == GUESS_VALUE:
                    print(f"Kudos👍! Your guess was right.")
                    break  # Exit the loop if the guess is correct
                
                else:
                    print(f"Oops😒! Your guess was {user_guess}, but I was thinking of {GUESS_VALUE}.")

                # Ask if the user wants to try again
                while True:
                    retry = input("Do you want to try again? Type 'y' for yes and 'q' to quit the game: ").lower()
                    if retry == 'q':
                        print("Goodbye! See you another day! 🙌")
                        return  # Exit the game
                    elif retry == 'y':
                        break  # Continue the game
                    else:
                        print("Invalid input. Please enter 'y' to play again or 'q' to quit.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")

    guess_game()

# Start the game
user_guess_input()