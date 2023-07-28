


pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Marques',
    'sobrenome2': 'Santos'
}
print(pessoa)
print(len(pessoa))
print(pessoa.__len__())

print(list(pessoa.keys()))
print(list(pessoa.values()))
print(pessoa.items())

for chave in pessoa.keys():
    print(chave)

for valor in pessoa.values():
    print(valor)

for itens in pessoa.items():
    print(itens)

for chave, valor in pessoa.items():
    print(chave, valor)
pessoa.setdefault('idade', 25)
print(pessoa['idade'])
print(pessoa)

