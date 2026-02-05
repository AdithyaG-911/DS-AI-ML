friend_a={"Python","Cooking","Hiking","Movies"}
friend_b={"Hiking","Gaming","Photography","Python"}

print("All interests both friends share :",friend_a | friend_b)
print("Common Interests :",friend_a & friend_b)
print("Unique Interests of Friend A :",friend_a - friend_b)
print("Unique Interests of Friend B :",friend_b - friend_a)