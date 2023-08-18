


pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Marques',
    'sobrenome2': 'Santos'
}
# print(pessoa)
# print(len(pessoa))
# print(pessoa.__len__())
#
#
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(pessoa.items())

for chave in pessoa.keys():
    print(chave)
print()

for valor in pessoa.values():
   print(valor)
print()
for itens in pessoa.items():
    print(itens)
print()
for chave, valor in pessoa.items():
    print(chave, valor)
print()
# pessoa.setdefault('idade', 25)
# print(pessoa['idade'])
# print(pessoa)

print(pessoa.get('sobrenome3', 'retorna isso'))

pessoa.setdefault('idade', 25)
print(pessoa['idade'])

