#dir

my_list = [1, 2, 3]
print(dir(my_list))

#hasattr

my_list = [1, 2, 3]
has_append = hasattr(my_list, "append")
print(has_append)

#getattr

person = {"name": "Alice", "age": 30}
name = getattr(person, "name", "Name not specified")
age = getattr(person, "age", "Age not specified")
print("Name:", name)
print("Age:", age)