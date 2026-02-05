contacts={
    "Adithya G": 8762116456,
    "Dhanush H": 9876543210,
    "Bhavish Kumar": 9123456780,
}
# Simple Printing with no formatting
# print(contacts)

contacts.update({"Amit Kumar": 9876543210})
contacts.update({"Dhanush H":8395002781})
print(contacts)

print(contacts.get("Adithya G","Contact Not Found"))

for name,phone in contacts.items():
    print(f"Contact: {name} | Phone :{phone}")
