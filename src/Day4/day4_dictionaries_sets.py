student={
    "name": "Amit",
    "age": 21,
    "course": "Engineering"
}

print(student["name"])
student["age"]=22

#.get() used to get value

marks={"math":80,"science":75,"english":85}
print(marks.get("math"))
print(marks.get("history",0))

for subject,score in marks.items():
    print(subject , score)

marks.update({"math":90,"history":70})
print(marks)

#loop
purchases={
    "Alice":250,
    "Bob":400,
    "Charlie":150
    }
for name,amount in purchases.items():
    print(f"{name} lost ₹ {amount} ")

print("Total Customers :",len(purchases))

print("Customer Names :",purchases.keys())

print("Purchase Amounts :",purchases.values())

#Program
#input dictionary from user
n=int(input("Enter number of customers: "))
user_purchases={}

for _ in range(n):
    name=input("Enter customer name: ")
    amount=int(input(f"Enter purchase amount for {name}: "))
    user_purchases[name]=amount

print("Customer Purchase Data :",user_purchases)

top_customer=max(user_purchases, key=user_purchases.get)
print(f"Top Customer: {top_customer} with purchase amount ₹ {user_purchases[top_customer]}")

low_customer=min(user_purchases, key=user_purchases.get)
print(f"Lowest Customer: {low_customer} with purchase amount ₹ {user_purchases[low_customer]}")