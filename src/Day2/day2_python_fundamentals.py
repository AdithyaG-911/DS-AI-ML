age=21
print(type(age))

height=5.8
print(type(height))

name="Shreyas"
print(type(name))

is_student=True
print(type(is_student))

name=input("Enter Your Name :")
age=25

print("Hello ",name,"!")
print("Hello " +name+ "!")

print(f"Hello {name} !")

# Using % operator (old style)
print("My name is %s and I'm %d years old" % (name, age))
# Using str.format()
print("My name is {} and I'm {} years old".format(name, age))

floatcomp=complex(5.4)
print(floatcomp)
#Error num=int(floatcomp)

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
