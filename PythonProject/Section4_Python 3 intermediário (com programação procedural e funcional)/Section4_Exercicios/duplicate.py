#Duplicate elements in a list:
#Given a list of numbers, create a new list that contains each number duplicated.

#Answer

list_numbers = [1, 2, 3, 4, 5]
new_list = [number * 2 for number in list_numbers]
print(new_list)