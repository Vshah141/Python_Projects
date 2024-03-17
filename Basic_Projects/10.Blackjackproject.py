import random

def blackjack():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    game_end = True
    while game_end:
        print("Welcome to Blackjack game")
        c1 = random.choice(cards)
        c2 = random.choice(cards)
        your_cards = [c1, c2]
        print(f"Your 2 cards are : {your_cards}")
        compc1 = random.choice(cards)
        print(f"Computer's first card is: {compc1}")
        print("Type 'y' to get another card and 'n' to pass")
        a = input()
        if a == "y":
            c3 = random.choice(cards)
            your_cards.append(c3)
            print(f"Your cards are : {your_cards}")
        elif a == "n":
            pass

        compc2 = random.choice(cards)
        computer_Cards = [compc1, compc2]
        print(f"Computer's hand is :{computer_Cards}")
        sum = 0
        sum2 = 0
        for item in your_cards:
            sum += item

        for item in computer_Cards:
            sum2 += item

        if sum2 < 16:
            comp3 = random.choice(cards)
            computer_Cards.append(comp3)
            sum2 += comp3

        print(f"Your final hand is :{your_cards} and sum is {sum}")
        print(f"Computer's final hand is :{computer_Cards} and sum is {sum2}")

        if sum <= 21 and sum2 <= 21:
            if sum == sum2:
                print("Draw")
            elif sum > sum2:
                print("You win")
            elif sum < sum2:
                print("You lose")
        elif sum > 21:
            print("You lose")
        elif sum > 21:
            print("You win")

        print("Do you wanna paly game of Black Jack again yes or no?")
        ans = input()
        if ans.lower() == "yes":
            blackjack()
        else:
            print("Thank you for playing")
            exit()


blackjack()
