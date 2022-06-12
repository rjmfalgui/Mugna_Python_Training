#Count the occurences of words from a given string and store the words and corresponding count as key value pairs in a dictionary
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