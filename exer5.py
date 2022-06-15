def main():
    contList = []
    try:
        f = open("exer5.txt", "r")
        for line in f:
            contList.append(line[:-1])
    except Exception as err:
        print(err)
    finally:
        f.close()

    contList.append(input("Enter string 1: "))
    contList.append(input("Enter string 2: "))
    contList.append(input("Enter string 3: "))
    contList.sort()

    try:
        userInput = open("exer5.txt", "w")
        for word in contList:
            userInput.write(word + "\n")
    except Exception as err:
        print(err)
    finally:
        userInput.close()
        
main()