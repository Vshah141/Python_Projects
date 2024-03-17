import os


def add(n1, n2):
    p = n1+n2
    return p


def sub(n1, n2):
    p = n1-n2
    return p


def mul(n1, n2):
    p = n1-n2
    return p


def div(n1, n2):
    p = n1/n2
    return p


def clear():
    os.system('cls')


def calculator():
    print("Welcome to Calculator")
    print("Choose first number")
    n1 = float(input())
    print("Coose the operation")
    print("+\n-\n*\n/\n")

    is_finished = True
    while is_finished:
        print("Coose the operation")
        x = input()
        print("Choose NEXT number")
        n2 = float(input())

        if x == "+":
            answer = add(n1, n2)

        elif x == "-":
            answer = sub(n1, n2)

        elif x == "*":
            answer = mul(n1, n2)

        else:
            answer = div(n1, n2)

        print(answer)
        print("Type y to continue calculating or type n to start a new calculator or any other letter to end")
        a = input()
        if a.lower() == "y":
            n1 = answer
        elif a.lower() == "n":
            clear()
            calculator()
        else:
            is_finished = False


calculator()
