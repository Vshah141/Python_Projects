# def report(Water, Milk, Coffee):
# print(Water)
# print(Coffee)


def espresso(total, Water, water_remaining):
    if Water >= 50 or water_remaining >= 50:
        if total == 15:
            print("Change is 0rs.")
            print("Enjoy your coffee")
        elif total > 15:
            change = total-15
            print(f"Here is your change {change}Rs")
            print("Enjoy your coffee")
        else:
            print("You have not entered sufficient money")
    else:
        print("You dont have enough water")
    return Water-50


def latte(total, Water, water_remaining):
    if Water >= 200 and water_remaining >= 200:
        if total == 20:
            print("Change is 0rs.")
            print("Enjoy your coffee")
        elif total > 20:
            change = total-20
            print(f"Here is your change {change}Rs")
            print("Enjoy your coffee")
        else:
            print("You have not entered sufficient money")
    else:
        print("You dont have enough water")
    return Water-200


def capacuinno(total, Water, water_remaining):
    if Water >= 250 or water_remaining >= 250:
        if total == 30:
            print("Change is 0rs.")
            print("Enjoy your coffee")
        elif total > 30:
            change = total-30
            print(f"Here is your change {change}Rs")
            print("Enjoy your coffee")
        else:
            print("You have not entered sufficient money")
    else:
        print("You dont have enough water")
    return Water-250


def user(choice, total, Water, water_remaining):
    if choice.lower() == "espresso":
        water_remaining = espresso(total, Water, water_remaining)
        print(f"Water remaining is {water_remaining}")
        print("Wanna more cup yes or no??")
        reply = input()
        if reply.lower() == "yes":
            coffee_machine(Water, water_remaining)
        else:
            exit()
    elif choice.lower() == "latte":
        water_remaining = latte(total, Water, water_remaining)
        print(f"Water remaining is {water_remaining}")
        print("Wanna more cup yes or no??")
        reply = input()
        if reply.lower() == "yes":
            coffee_machine(Water, water_remaining)
        else:
            exit()
    elif choice.lower() == "cappacuino":
        water_remaining = capacuinno(total, Water, water_remaining)
        print(f"Water remaining is {water_remaining}")
        print("Wanna more cup yes or no??")
        reply = input()
        if reply.lower() == "yes":
            coffee_machine(Water, water_remaining)
        else:
            exit()
    return water_remaining


def coffee_machine(Water, water_remaining):
    while stop:
        print("Welcome to coffee machine")
        print("Menu\n")
        print("1. Espresso: 15rs\nWater needed : 50ml\nCoffee needed:18g")
        print("2. Latte: 20rs\nWater needed : 200ml\nCoffee needed:24g")
        print("3. Cappucuino 30rs\nWater needed : 250ml\nCoffee needed:24g")
        print("What would you like to have")
        print("Espresso/Latte/Cappacuino")
        choice = input()
        if choice.lower() == "report":
            # report(Water, Milk, Coffee)
            print("Wanna more cup yes or no??")
            reply = input()
            if reply.lower() == "yes":
                coffee_machine(Water, water_remaining)
            else:
                exit()
        else:
            print("Please insert coins")
            coin1 = int(input("Any 5 rupee coins?\n"))
            coin2 = int(input("Any 10 rupee coins?\n"))
            coin3 = int(input("Any 20 rupee coins?\n"))
            amt1 = coin1*5
            amt2 = coin2*10
            amt3 = coin3*20
            total = amt1+amt2+amt3
            user(choice, total, Water, water_remaining)


water_remaining = 300
Water = 300
# Milk = 200
# Coffee = 100
# Money = 0
stop = True
coffee_machine(Water, water_remaining)
