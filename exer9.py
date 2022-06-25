class Error(Exception):
    pass

class HexFormatError(Error):
    """
    Will send error report if string does not fit with the format for hexadecimal
    """
    pass

class HexMemoryError(Error):
    """ 
    Will send error report if input is more than 8 digits
    """
    pass

def hex_to_deci(userInput):
    length = len(userInput) - 1
    deci = 0

    hexadeci = ['0123456789ABCDEF']
    hex_value = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }

    try:
        if len(userInput) > 8:
            raise HexMemoryError
        for character in userInput:
            if character not in hexadeci:
                raise HexFormatError

        for character in userInput:
            deci += hex_value[character] * (16**length)
            length -= 1

    except HexMemoryError:
        print("Error1")
    except HexFormatError:
        print("Error2")
    return deci

def main():
    userInput = input("Enter 4-byte (8 digits) hexadecimal value: ").upper()
    deci = hex_to_deci(userInput)
    print(deci)

main()