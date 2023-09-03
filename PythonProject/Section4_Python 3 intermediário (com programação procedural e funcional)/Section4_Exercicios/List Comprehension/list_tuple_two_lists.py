# Create a List of Tuples from Two Lists:
# Given two lists, create a new list that contains tuples with corresponding elements from both lists.

names = ['Victor', 'Matheus', 'Filipe']
ages = [25, 25, 25]
list_with_tuples = [(name, age) for name, age in zip(names, ages)]
print(list_with_tuples)

