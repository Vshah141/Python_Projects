import random
print("Heyy Welcome to Stone Papaer Scissors game")

print("Choose 0 for stone, 1 for paper and 2 for scissors")
x = int(input())
if x == 0:
    print("You choose 🪨")
elif x == 1:
    print("You choose 🗏")
elif x == 2:
    print("You choose ✂️")
y = random.randint(0, 2)
if y == 0:
    print("Computer choose 🪨")
elif y == 1:
    print("Computer choose 🗏")
elif y == 2:
    print("Computer choose ✂️")
if x == 0 and y == 0:
    print("Neutral")
elif x == 0 and y == 1:
    print("You lose")
elif x == 0 and y == 2:
    print("You win")
elif x == 1 and y == 0:
    print("You win")
elif x == 1 and y == 1:
    print("Neutral")
elif x == 1 and y == 2:
    print("You win")
elif x == 2 and y == 0:
    print("You lose")
elif x == 2 and y == 1:
    print("You lose")
elif x == 2 and y == 2:
    print("Neutral")
