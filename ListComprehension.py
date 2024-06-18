# List Comprehension
# Exercises: Day 13

#Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
List = [ i for i in numbers if i <= 0]
print(List)

#Flatten the following list of lists of lists to a one dimensional list :

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [item for sublist in list_of_lists for subsublist in sublist for item in subsublist]
print(flattened_list)

#Using list comprehension create the following list of tuples:

result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)

#Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

ListCountries = [[country.upper(), country[:3].upper(), city] for sublist in countries for (country, city) in sublist]

print(ListCountries)

#Write a lambda function which can solve a slope or y-intercept of linear functions.

print((lambda m,y,x : m*x + y)(4,2,0))



