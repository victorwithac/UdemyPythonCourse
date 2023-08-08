# def imprimir(a, b, c):
#     print(a, b, c)
#
# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

#Usando os parametros dentro da função pode-se sempre mudar a função!!!!

# def saudacao(nome='Ninguém'):
#     print(f'Ola, {nome}!')
#
# saudacao('Victor')
# saudacao('Luiz')
# saudacao()


# def imprimir(fechadura):
#     return (fechadura)
# 
# imprimir('chave')


# def saudar(nome='Sem nome'):
#     print(f'O python retornou meu argumento >>> {nome}')
#
# saudar('Victor')
# saudar('Marques')
# saudar('Dos')
# saudar('Santos')
# saudar()

# def function(x='No colour'):
#     print(f'The return of my function is, {x}')
#
# function('Blue')
# function('Black')
# function('White')
# function()


# def sum(x, y, z=0):
#     print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)
#
# # sum(1422, 4542)
# # sum(1, 2)
# # sum(y=2, x=1) #argumentos nomeados, quando eu digo com o '='qual é o meu argumento
#
# sum(1, 2)

def my_function(x, y, z):
    resultado = x + y + z
    print(resultado)

my_function(1, 2, 3)
