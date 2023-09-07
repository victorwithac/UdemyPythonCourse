#try, except, else and finally

try:
    print('Open file')
    8/0
except ZeroDivisionError as error:
    division_error = error.__class__.__name__
    print(division_error)
else:
    print('No error occurred')
finally:
    print('Close file')

