print("SIMPLE CALCULATOR")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
choice=int(input("Enter your choice:"))
if choice==1:
    print("Addition of two numbers are:",num1+num2)
elif choice==2:
    print("Subtraction of two numbers are:",num1-num2)
elif choice==3:
    print("Multiplication of two numbers are:",num1*num2)
elif choice==4:
    print("Division of two numbers are:",num1/num2)
else:
    print("Invalid choice, enter number from 1 to 4")
