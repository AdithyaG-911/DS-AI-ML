name=input("Enter your name: ")
goal=input("What is your goal for today? ")

with open("journal.txt", "a") as file:  # w mode will overwrite the file, a mode will append to the file
    file.write(f"{name} - {goal}\n")
print("Your goal has been saved to the journal.")
