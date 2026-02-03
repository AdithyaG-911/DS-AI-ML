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
num=int(floatcomp)
