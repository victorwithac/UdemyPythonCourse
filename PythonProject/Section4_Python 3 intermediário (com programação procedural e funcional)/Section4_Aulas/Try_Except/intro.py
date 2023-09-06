#Try, except, else and finally


try:
    a = 18
    # b = 0
    c = a / b
    print('Row 1')
    print('Row 2')
except (ZeroDivisionError, NameError) as error:
    print('Can\'t divide by zero or Name is not defined')
    print('MSG', error)
    print('Nome:', error.__class__.__name__)
# except NameError:
#     print('Name is not defined')
# except Exception:
#     print('Unknown Error')
print('Continue')

