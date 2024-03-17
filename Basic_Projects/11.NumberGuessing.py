import random
def toohigh():
    print("Too high")
    print("Guess Again")
def toolow():
    print("Too low")
    print("Guess Again")
hard = 5
easy = 10
def check_answer(guess, x, turns):

    if guess == x:
        print("Correct")
        exit()
    elif guess > x:
        toohigh()
        return turns-1

    elif guess < x:
        toolow()
        return turns-1

def set_difficulty():
    diff = input("Easy or hard?")
    if diff == "easy":
        return easy
    else:
        return hard


def game():
    print("Welcome to number guessing Game")
    print("Think a number from 1 to 100")
    x = random.randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != x:
        print(f"Tou have {turns} left")
        guess = int(input("Guess\n"))
        turns = check_answer(guess, x, turns)
        if turns == 0:
            print("You have got 0 chances")
            exit()


game()
