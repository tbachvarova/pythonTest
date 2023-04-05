calculation_unit = 24
unit_name = "hours"

def daysToUnits(numOfDays, customMessage):
    print(f"{numOfDays} days are {numOfDays * calculation_unit} {unit_name}")
    print(customMessage)


daysToUnits(20, "Super!")
daysToUnits(35, "Super custom :)")

userInput = input("Add something: ")
userInputNum = int(userInput)

print(f"User added: {userInputNum}")