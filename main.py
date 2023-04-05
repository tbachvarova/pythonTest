# https://www.youtube.com/watch?v=t8pPdKYpowI
# time:

calculation_unit = 24
unit_name = "hours"


def daysToUnits(numOfDays):
   return f"{numOfDays} days are {numOfDays * calculation_unit} {unit_name}"
  #  print(type(conditionCheck))


def validationAndExecute():

   try:
        userInputNum = int(userInput)

        if userInputNum > 0:
           calcValue = daysToUnits(userInputNum)
           print(calcValue)

        elif userInputNum == 0:
            print("It must be grater the 0")

        else:
            print("Number must be Grater than 0")


   except ValueError:
        print("Try again with number!")



print(type(1))
print(type(33.99))
print(type("alabala"))
print(type(9 > 0))

userInput = input("Add some number for days: ")
validationAndExecute()
