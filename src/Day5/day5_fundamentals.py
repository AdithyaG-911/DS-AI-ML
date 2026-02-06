def greet():
    print("Hello, welcome to the internship!")
greet()


#Arguments and Parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)

#Variable Scope
x=10
def show_value():
    x=5
    print(x)

show_value()    
print(x)


icecream="vanilla"
def food():
    fruit="apple"
    vegetable="tomato"
    icecream="chocolate"
    print(fruit,"is good for health")
    print(icecream," is my favorite flavor")
food()
print(icecream, " is high rated")
#Error print(vegetable," can be used as source")

import random
print("Random float between 1 and 10:", random.uniform(1,10))
print("Random integer between 1 and 10:", random.randint(1,10))

import utils
result = utils.multiply(4, 5)
print("The result of multiplication is:", result)