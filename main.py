calculation_unit = 24
unit_name = "hours"

def daysToUnits(numOfDays):
    if numOfDays > 0:
        print(f"{numOfDays} days are {numOfDays * calculation_unit} {unit_name}")
    elif numOfDays == 0:
        print("It must be grater the 0")
    else:
        print("Number must be Grater than 0")


userInput = input("Add some number for days: ")

if userInput.isdigit():
    daysToUnits(int(userInput))
else:
    print("Try again with number!")

# print(type(1))