print("Welcome To Love Calculator")
print("Enter your name")
name1 = input()
print("Enter your love's name")
name2 = input()

x = name1.lower()
y = name2.lower()

u = name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e") + \
    name2.count("t")+name2.count("r")+name2.count("u")+name2.count("e")
v = name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e") + \
    name2.count("l")+name2.count("o")+name2.count("v")+name2.count("e")

score = str(u)+str(v)

if int(score) < 10 and int(score) > 90:
    print(
        f"Your Score is {score} out of 100 and you both are like coke and mentos")
elif int(score) < 50 and int(score) > 40:
    print(
        f"Your score is {score} out of 100 and you both are alright together")
elif int(score) > 100:
    print(f"Your score is {score} and your love is immense")
else:
    print(f"Your score is {score} out of 100")
