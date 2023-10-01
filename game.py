import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < 10:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number - 10:
                print("Too low. Try again.")
            elif guess > secret_number + 10:
                print("Too high. Try again.")
            elif abs(guess - secret_number) <= 10:
                print("You're close!")

            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break

            if attempts == 10:
                print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    guess_the_number()
