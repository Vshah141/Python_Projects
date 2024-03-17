import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
           "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "^", "&", "*", "(", ")"]

print("Enter the number of letters you want")
l = int(input())
print("Enter the number of numbers you want")
n = int(input())
print("Enter the number of symbols you want")
s = int(input())
password_list = []
for x in range(0, l):
    password_list.append(random.choice(letters))

for x1 in range(0, n):
    password_list.append(random.choice(numbers))

for x2 in range(0, s):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)
