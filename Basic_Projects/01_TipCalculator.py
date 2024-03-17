print("Welcome to the Tip Calculator")
print("What is the total bill?")
a = float(input())
print("How much tip you would like to give?")
x = int(input())
print("In how many perons you have to split the bill?")
z = int(input())
total_bill_with_tip = a+x
print("Per person you have to pay"+ str(total_bill_with_tip/z))
