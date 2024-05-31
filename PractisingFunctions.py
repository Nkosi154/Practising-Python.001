# On this mini project I am practising Functions

'''# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()'''

def nameandsurname():
    name = input("What is your name: ")
    surname = input("What is your surname: ")
    space = " "
    both = name +space+ surname
    return both
print(nameandsurname())

def yearcalculator():
    BirthYear = int(input("What is your birth Year: "))
    CurrentYear = int(input("What is the current year: "))

    YourAge= CurrentYear - BirthYear
    return YourAge

print("Your are " + str(yearcalculator()) + " years old")

def numbers(num1,num2):
    if num1 > num2:
        print(False)
    elif num2 > num1:
        print("Five is greater than Three")
print(numbers(3,5))

