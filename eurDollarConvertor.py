result = input("How much EUR would you like to convert into DOLLAR? ")

rate = 1.14

if result.isdigit():
    euro = int(result)
    dollar = euro * rate
    print("{} EURO is {} $".format(euro, dollar))
else:
    print("That's not a number I don't understand...")
