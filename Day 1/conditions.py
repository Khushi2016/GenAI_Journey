num = int(input("Enter a number :"))

if num %2 == 0:
    print("even")
else:
    print("odd")


a = int(input("Enter a number : "))

if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")


num1 = int(input("Enter a number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter a third number : "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is : ",num)
elif num2 >= num3 and num2 >= num1:
    print("Largest number is : ",num2)
else:
    print("Largest number is : ",num3)