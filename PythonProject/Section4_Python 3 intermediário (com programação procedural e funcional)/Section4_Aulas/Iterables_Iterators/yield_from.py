#Yield from

def gen1():
    yield 1
    yield 2
    yield 3
    print('Its over')
def gen3():
    yield 10
    yield 20
    yield 30
    print('Its over')
def gen2(gen=None):
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('Its over')

g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
for numero in g2:
    print(numero)
for numero in g3:
    print(numero)
    