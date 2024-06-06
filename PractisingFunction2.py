def name(first_name, last_name):
    id_names = first_name + " " + last_name
    return id_names
print("My names are: " ,name("Linda", "Nkosi"))

#Declare a function add_two_numbers. It takes two parameters and it returns a sum

def function(num1,num2):
    sum = num1 + num2
    return sum
print(function(4,5))

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def add_two_numbers(radius):
    PieValue = 3.14159
    Area = PieValue * radius * radius
    return Area
print(add_two_numbers(4))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.


def add_all_nums(*args):
    try:
        return sum(args)
    except TypeError:
        return "Error: All items must be numbers."
print(add_all_nums(5,6,78,"Linda"))

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F,
# convert_celsius_to-fahrenheit.

def temperature(celsius):
    Fahrenheit = celsius * 9/5 + 32
    return Fahrenheit
print(temperature(celsius= 56))

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if month in ["December","January","February"]:
        print("Summer")
    elif month in ["March","April","May"]:
        print("Autumn")
    elif month in ["June","July","August"]:
        print("Winter")
    elif month in ["September","October","November"]:
        print("Spring")
months = input("Enter Month: ")
print(check_season(months))

#Write a function called calculate_slope which return the slope of a linear

def calculate_slope(*args):

      Gradient = (y2-y1) / (x2-x1)
      return Gradient

y2 = int(input("Enter the value of y2: "))
y1 = int(input("Enter the value of y1: "))
x1 = int(input("Enter the value of x1: "))
x2 = int(input("Enter the value of x2: "))


print("The slope of this line is: " , calculate_slope(y2,y1,x1,x2))

#Quadratic equation is calculated as follows: ax² + bx + c = 0.
#Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(*args):
    x1 = (-(b) + ((b ** 2) - 4 * (a * c)) ** (1 / 2)) / (2 * a)
    x2 = (-(b) - ((b ** 2) - 4 * (a * c)) ** (1 / 2)) / (2 * a)
    return x1
    return x2
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

print(solve_quadratic_eqn(a,b,c))
print(solve_quadratic_eqn(a,b,c))

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_List(*args):
    List = []
    for list in args:
        List.append(list)
    return List

print(print_List(1,2,3,4,5,6,7))

#Declare a function named reverse_list.
# It takes an array as a parameter and it returns the reverse of the array (use loops)

def reverse_list(arr):
    reversed_list = []
    for List in range(len(arr) - 1, -1, -1):
        reversed_list.append(arr[List])
    return reversed_list


print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

#Declare a function named capitalize_list_items.
#It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(*items):
    capitalized_items = []
    for item in items:
     capitalized_items.append(item.upper())
    return capitalized_items
print(capitalize_list_items("linda","Radolf","Nkosi"))

#Declare a function named add_item. It takes a list and an item parameters.
#It returns a list with the item added at the end.

def add_item(food_staff,*item):
   result = list(food_staff)
   print(food_staff)
   for items in item:
        result.append(items)
   return result

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff,'Meat'))

def remove_item(numbers,*item):
    Outcome = list(numbers)
    for number in item:
        Outcome.append(number)
    return Outcome

numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))
def add_intergers(List_of_numbers,*intergers):
    Total = list(List_of_numbers)
    for number in intergers:
        Total.append(number)
    return Total
List_of_numbers = [1,2,3,4,5,6,7,8]
print(add_intergers(List_of_numbers,65,87,54,43))

#Declare a function named sum_of_numbers.
#It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(num):
    total = 0
    for num in range(1, num+1):
        total += num
    return total

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#Declare a function named sum_of_odds.
#It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(odd):
    total = 0
    for num in range(1,odd+1):
        if num % 2 != 0:
         total += num
    return total
print(sum_of_odds(10))

#Declare a function named sum_of_even.
#It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(even):
    total = 0
    for num in range(1,even+1):
        if num % 2 == 0:
            total += num
    return total
print(sum_of_even(10))

#Exercises: Level 2

#Declare a function named evens_and_odds .
#It takes a positive integer as parameter and it counts number of evens and odds in the number.

def even_and_odds(number):
    count_even = 0
    count_odd = 0
    for numbers in range(0, number + 1):
        if numbers % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    return count_even, count_odd
print(even_and_odds(100)

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(number):

 return 1 if number == 1 or number == 0 else  number * factorial(number - 1)

print("The factorial of number: ", 20,"is",factorial(20))

def factorial(n):
    return 1 if n == 1 else n * factorial(n-1)
print("The factorial of number: ", 7,"is",factorial(7))

#Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(parameter):
    if not parameter:
        return True
    else:
        return False

print(is_empty([]))

#Write different functions which take lists.
#They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def calculate_mean(numbers):
    List = list(numbers)

    mean = sum(List)/len(List)
    return mean

numbers = [4,5,7,11,16,46,3,9]
print(calculate_mean(numbers))
import statistics


def calculate_median(numbers):
    List = list(numbers)
    median = statistics.median(List)
    return median

numbers = [4,5,7,11,16,46,3]
print(calculate_median(numbers))
import statistics

def calculate_mode(numbers):
    List = list(numbers)
    mode = statistics.mode(List)
    return mode
numbers = [4,5,7,11,16,46,3]
print(calculate_mode(numbers))

def calculate_range(numbers):
    List = list(numbers)
    minimum = min(List)
    maximum = max(List)
    print(minimum,maximum)

numbers = [4,5,7,11,16,46,3]
print(calculate_range(numbers))

import statistics

def calculate_varience(numbers):
    List = list(numbers)
    varience = statistics.variance(List)
    return varience
numbers = [4,5,7,11,16,46,3]
print(calculate_varience(numbers))
import statistics


def calculate_dev(numbers):
    List = list(numbers)
    deviation = statistics.stdev(List)
    return deviation
numbers = [4,5,7,11,16,46,3]
print(calculate_dev(numbers))

#Exercises: Level 3

#Write a function called is_prime, which checks if a number is prime.

import math

def is_prime(number):

    if number <= 1:
        return False
    for num in range(2, int(math.sqrt(number)) + 1):
        if number % num == 0:
            return False
    return True
number = 3
print(is_prime(number))

#Write a functions which checks if all items are unique in the list.

def check_number(number):
    return len(number) == len(set(number))
numbers = [4,5,7,11,16,46,3]
print(numbers,": ",check_number(numbers))

def check_item(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j] :
              return False
    return True
numbers = [4,5,7,11,16,46,3]
print(check_item(numbers))

#Write a function which checks if all the items of the list are of the same data type.

def check_type(items):
    if not items:
        return True
    first_type = type(items[0])
    for item in items:
        if type(item) != first_type:
            return False
    return True

numbers = [4, 5, 7, 11, 16, 46, "Linda"]
print(numbers, ": ", check_type(numbers))


def check_function(*items):
    #Checking if the items List is empty.
    if not items:
        return True
    #Checks the data type of the first term on the list
    data_type = type(items[0])
    #checking if the type of each items is the same or different from the one on the first item
    for item in items:
        if type(item) != data_type:
            return False
    return True
print(check_function(6,7,5,3,8,4))

#Write a function which check if provided variable is a valid python variable

def check_var(variable):
  return not isinstance(variable ,type)

variable = input("Enter a variable: ")
print(check_var(variable))



