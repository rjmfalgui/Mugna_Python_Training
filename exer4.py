inp = input("Enter String: ").lower()
i = inp.replace(".", "").replace("?", "").replace("!", "").replace(",", "").replace(":", "").replace(";", "").replace("#", "").replace("@", "").replace("&", "").replace("*", "").replace("-", "")

words = i.split()
container = {}

for word in words:
    if word in container:
        container[word] += 1
    else:
        container[word] = 1
print(container)