# a, b = 1, 2
# a, b = b, a
# # print(a, b)
#
# pessoa = {
#     'nome': 'Victor',
#     'sobrenome': 'Marques',
# }
# a, b = pessoa.values()
# print(a, b)
# a, b = pessoa.items()
# print(a, b)
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Marques',
}

dados_pessoa = {
    'idade': 25,
    'altura': 1.8,
}

# print(pessoa, dados_pessoa)

pessoas_completa = {**pessoa,'chave': 5, **dados_pessoa, 'nova_chave': 4}
# print(pessoas_completa)

#args e kwargs

def mostro_argumentos_nomeados(*args, **kwargs):
    print(args)
    print()
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(1, 2, x=2, nome='Joana', qlq=123, y=5)

configuracoes = {
    'arg1':1,
    'args2':2,
    'arg3':3,
    'arg4':4,
}
mostro_argumentos_nomeados(**configuracoes)