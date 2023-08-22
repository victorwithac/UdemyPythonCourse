lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
# lista = ['s' ,'e' ,'t', 'a', 'k', 'm', 'o']


# def ordena(item):
#     return item['nome']
# lista.sort(key=ordena)

def exibir(lista):
    for item in lista:
        print(item)
    print()
#lambda
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
