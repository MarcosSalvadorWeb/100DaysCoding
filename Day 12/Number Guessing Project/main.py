from random import randint

print("Welcome to the Number Guessing Project")
print("I am thinking of a number between 1 and 100")


def difficulty(chose):
    if chose == "easy":
        return 10
    elif chose == "hard":
        return  5

def check_guess(guess,number,lives):
    if guess < number:
        print("Too low")
        return (lives-1)
    elif guess > number:
        print("Too high")
        return (lives-1)



def game():
    chose = str(input("Chose a difficulty level. Type 'easy' or 'hard': "))
    number = randint(1,100)
    print(f"The number is {number}")
    lives = difficulty(chose)
    guess = int(input("Guess the number"))

    while guess != number:
        print(f"you have {lives-1} lives left")
        lives = check_guess(guess,number, lives)
        guess = int(input("Guess the number"))
        if lives == 1:
            break

    if lives == 1:
        print("You lost")
    elif lives != 1:
        print("You won")

game()