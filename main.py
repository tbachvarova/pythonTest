calculation_unit = 24
unit_name = "hours"

def daysToUnits(numOfDays):
    print(f"{numOfDays} days are {numOfDays * calculation_unit} {unit_name}")
    print("Great Job!")


daysToUnits(20)
daysToUnits(35)

userInput = input("Add something: ")
userInputNum = int(userInput)

print(f"User added: {userInputNum}")