import csv
file=open("students.csv", "r")
reader=csv.reader(file)
for row in reader:
    print(row[0], row[1], row[2])

# Reset the file pointer to the start
file.seek(0)

print("Students name, who passed the exam:")
for row in reader:
    if row[2]=="Pass":
        print(f"{row[0]}")