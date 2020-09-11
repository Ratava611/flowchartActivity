numbers = []
while len(numbers) != 12:
    userInput = input("Enter number " + str(len(numbers) + 1) + ":    ")
    try:
        userInput = int(userInput)
        numbers.append(userInput)
    except ValueError:
        print("Input not recognized")
        print(type(userInput))

product = 1
for x in numbers:
    product *= x
print("Your product is:    " + str(product))
