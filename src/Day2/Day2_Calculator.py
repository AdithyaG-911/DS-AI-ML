while(1):
    print("Simple Calculator:\n")
    a=int(input("Enter Number 1:"))
    b=int(input("Enter Number 2:"))
    print("Number 1:",a)
    print("Number 2:",b)
    print("\n Addition :+\n Substraction :-\n Product :*\n Division :/\n Power :**\n Floor Division ://\n")
    ch=input("Enter the operation:\n")
    if ch=='+':
        print("Addition: ",a+b)
    elif ch=='-':
        print("Substraction: ",a-b)
    elif ch=='*':
        print("Product: ",a*b)
    elif ch=='/':
        print("Division: ",a/b)
    elif ch=='**':
        print("Power: ",a**b)
    elif ch=='//':
        print("Floor Division: ",a//b)
    else:
        print("Wrong Choice")
        break
