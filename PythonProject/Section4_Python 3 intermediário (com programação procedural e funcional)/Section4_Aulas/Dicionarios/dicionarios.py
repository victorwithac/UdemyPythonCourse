pessoa = {}

chave = 'nome'
pessoa[chave] = 'Victor'

pessoa['sobrenome'] = 'Marques'
pessoa['idade'] = 25

del pessoa['sobrenome']


# print(pessoa[chave])
# print(pessoa)
print(pessoa.get('sobrenome', None))

if pessoa.get('sobrenome') is not None:
    print(pessoa['sobrenome'])
else:
    print('Não existe')


