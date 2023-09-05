#Generator expression, Iterables and Iterators in Python
import sys

my_list = [n for n in range(10000)]
generator = (n for n in range(10000))
print(generator)
print(next(generator))
for numero in generator:
    print(numero)

# print(my_list)
# print(sys.getsizeof(my_list))
# print(sys.getsizeof(generator))
