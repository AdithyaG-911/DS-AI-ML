print("Split Bills in Restaurant\n")

total=float(input("Enter the Total Bill Amount :"))
people_count=int(input("Enter the number of people in your Friend Group :"))
share_per_person=total/people_count
print(f"Total Bill: {total}. Each person pays: {share_per_person}")

print("\nData types:\n")
print("total :",type(total))
print("people_count :",type(people_count))
print("share_per_person :",type(share_per_person))
