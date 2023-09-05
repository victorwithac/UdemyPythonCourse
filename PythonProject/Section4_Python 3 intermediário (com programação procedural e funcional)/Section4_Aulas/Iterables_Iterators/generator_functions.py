#Introduction to Generator functions in Python
# generator = (n for n in range(100))

def generator(n=0):
    yield n #pause
    print('Pause')
    yield 11
    print('Here')

gen = generator(10)
print(next(gen))
print(next(gen))

