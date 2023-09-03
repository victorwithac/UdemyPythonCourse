# Given a list that contains a variety of data types
# (integers, strings, floats, etc.), create a function
# called check_types that iterates through the list and
# identifies the data types of elements present in the list.
# The function should return a dictionary where the keys are
# the data types found, and the values are the counts of each type.

#Answer
def check_types(x):
    counter_types = {}
    for item in my_list:
        for type in (int, str, float, list, dict):
            if isinstance(item, type):
                if type in counter_types:
                    counter_types[type] += 1
                else:
                    counter_types[type] = 1
    return counter_types

my_list = [1, "hello", 3.14, 42, "world", [1, 2, 3], {"nome": "Alice"}]
print(check_types(my_list))

