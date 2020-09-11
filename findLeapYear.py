userInput = input("Enter year:    ")
while type(userInput) == str:
    try:
        userInput = int(userInput)
    except ValueError:
        print("Input not recognized")
        print(type(userInput))

year = userInput
if year % 4 != 0:
    print(str(year) + " is not a leap year.")
elif year % 100 != 0:
    print(str(year) + " is a leap year!")
elif year % 400 != 0:
    print(str(year) + " is not a leap year.")
else:
    print(str(year) + " is a leap year!")
