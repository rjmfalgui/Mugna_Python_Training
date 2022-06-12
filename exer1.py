i = input("Please input a number: ")
inp = int(i)

if inp >= 60 and inp < 75:
    print("Derp!")
elif inp >= 75 and inp < 85:
    print("Good")
elif inp >= 85 and inp < 94:
    print("Very Good")
elif inp >= 95 and inp <= 100:
    print("Excellent!")
else:
    print("Invalid Value")