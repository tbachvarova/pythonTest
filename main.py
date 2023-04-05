calculation_unit = 24
unit_name = "hours"

def daysToUnits(numOfDays):
    if(numOfDays > 0):
        print(f"{numOfDays} days are {numOfDays * calculation_unit} {unit_name}")
    else:
        print("Number must be Grater than 0")

userInput = input("Add some number for days: ")

daysToUnits(int(userInput))

# print(type(1))