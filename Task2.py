def calculator():
    num1=int(input("Enter the first number"))
    num2=int(input("Enter the second number"))
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exponent\n6.Floor Division")
    choice=int(input("Enter your choice"))
    if choice==1:
        print(f"the sum of num1 and num2 is {num1+num2}")
    elif choice==2:
        print(f"the difference of num1 and num2 is {num1-num2}")
    elif choice==3:
        print(f"the product of num1 and num2 is {num1*num2}")
    elif choice==4:
        print(f"the division of num1 and num2 is {num1/num2}")
    elif choice==5:
        print(f"the exponent of num1 and num2 is {num1**num2}")
    elif choice==6:
        print(f"the floor division of num1 and num2 is {num1//num2}")
    else:
        print("you enter Invalid choice")
    
calculator()
