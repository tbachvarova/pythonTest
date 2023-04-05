calculation_unit = 24
unit_name = "hours"

def daysToUnits(numOfDays):
    print(f"{numOfDays} days are {numOfDays * calculation_unit} {unit_name}")


userInput = input("Add some number for days: ")
userInputNum = int(userInput)

print(f"User added: {userInputNum} days")
daysToUnits(userInputNum)