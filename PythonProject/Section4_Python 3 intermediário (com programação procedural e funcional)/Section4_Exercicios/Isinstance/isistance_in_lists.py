#Check types of elements in a list:
#Given a list that contains a variety of data type(int, str, float, etc),
#create a function that iterates through the list and identifies how many
#elements are integers.

#Answer

def integer_counter(x):
    counter = 0
    for item in list:
        if isinstance(item, int):
            counter += 1
    return counter


list = [1, "hello", 3.14, 42, "world"]
print(integer_counter(list))