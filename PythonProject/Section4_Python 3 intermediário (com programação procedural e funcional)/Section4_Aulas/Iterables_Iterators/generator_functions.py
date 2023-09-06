#Introduction to Generator functions in Python
# generator = (n for n in range(100))

def generator(n=0):
    yield n #pause
    print('Pause')
    yield 11
    print('Here')
    yield 12
    return
# gen = generator(10)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return


gen = generator(n=0, maximum=50)
for n in gen:
    print(n)
    