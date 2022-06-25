name1, name2 = input("enter name 1: ").lower(), input("enter name 2: ").lower()
n1 = name1.replace(" ", "")
n2 = name2.replace(" ", "")

count = 0
for letter in n1:
    if letter in n2:
        count += 1


for letter in n2:
    if letter in n1:
        count +=1

totalCount = count % 6

if totalCount == 1:
    print("Friends")
elif totalCount == 2:
    print("Lovers")
elif totalCount == 3:
    print("Acquaintances")
elif totalCount == 4:
    print("Marriage")
elif totalCount == 5:
    print("Enemies")
elif totalCount == 0:
    print("Siblings")
else:
    pass

print(count)