print("Welcome to Treasure island game")
print("Whats your name?")
name = input()
print("Welcome Captian "+name)
print("Where do you wanna go left or right?")
dir = input()
if dir.lower() == "left":
    print("You have to go into an island")
    print("Will you swim or go by making a boat?")
    method = input()
    if method.lower() == "swim":
        print("You are courageous but the crocodiles near the island are more courageous")
        print("Sorry you are dead")
        print("Game over")
    elif method.lower() == "boat":
        print("Ok so you are hard working too!!")
        print("Your boat is ready and we are good to go to the island")
        print("here you come to the island")
        print("There is a small house at the island which have three doors\n choose one of them ")
        door = int(input())
        if door == 1:
            print(
                "You entered a door having treasure\n Congratulations you have found the treasure")
        elif door == 2:
            print("You have entered a door having nothing inside it\n Sorry you lost")
        elif door == 3:
            print("You have entered door full of bees\n Sorry you lost ")
else:
    print("You have entered the forest")
    print("Due to animals you cant go Sorry you have lost")
