raw_logs=["ID01","ID02","ID01","ID05","ID02","ID08","ID01"]
print(raw_logs)

unique_users=set(raw_logs)
print(sorted(unique_users))

#membership test
print("ID05" in unique_users)

#length of set
print("Number of unique users :",len(unique_users))
