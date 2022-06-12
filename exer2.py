#Write a program that prints all multiples of 7 that are below 100

i = input("Input Range: ")
inp = int(i)
for num in range(inp):
    total = num*7
    if total < 100:
        print(total)

""" tama na answer ni but mas better and specific ang taas
for num in range(15):
    print(num*7)
"""