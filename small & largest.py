def smallerlarger(a, b):
    if a < b:
        print("Smaller number:", a)
        print("Larger number:", b)
    elif a > b:
        print("Smaller number:", b)
        print("Larger number:", a)
    else:
        print("Both numbers are equal.")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

smallerlarger(num1, num2)