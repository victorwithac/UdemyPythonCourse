#raise - exceptions

# print(123)
# raise ValueError('Error')
# print(456)

def division(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        return n
print(division(8, 0))

