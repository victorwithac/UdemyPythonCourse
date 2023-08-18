p1 = {
    'nome': 'Victor',
    'sobrenome': 'Marques'
}

p1.update(idade='25')
p1.update(lista=[0, 1, 2])
del p1['idade']
print(p1.get('endereco', 'Não temos o endereço!'))
salvo = p1.pop('lista')
print(p1)
print(salvo)
# p1.popitem()
print(p1)
p1.update(sobrenome='Santos')
print(p1)

tupla = (('CEP', '91020010'),('Rua', 'Assis Brasil 343'))
p1.update(tupla)
print(p1)


# print(p1.get('nome', 'Não existe'))

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)


# excluido = p1.pop('nome')
# print(excluido)
# print(p1)

# p1.update({
#     'sobrenome': 'Marques',
#     'idade': 25
# })
# print(p1)

# p1.update(nome='João', idade='30', cidade='Porto Alegre')
# print(p1)

# tupla = ('nome', 'José'), ('idade', 27)
# p1.update(tupla)
# print(p1)

