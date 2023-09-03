#Filter even numbers:
#Given a list of numbers, create a new list that contains only the even numbers.

#Answer
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in list_numbers if number % 2 == 0]
print(even_numbers)