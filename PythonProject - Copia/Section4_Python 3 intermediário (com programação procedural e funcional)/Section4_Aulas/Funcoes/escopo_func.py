

x = 1

def escopo():

    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)
    outra_funcao()

    print(x)
    x = 5

print(x)
escopo()
print('*-*' * 15)
print(x)




