# Code to square numbers greater than 50 in a range using list comprehension
numbers = range(1, 11)

squared_numbers = [x ** 2 for x in numbers]
filter_squared_numbers = [x ** 2 if x ** 2 > 50 else 0 for x in numbers]

print(squared_numbers)
print("-----------")
print(filter_squared_numbers)
