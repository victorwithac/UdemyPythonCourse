product = {
    'name': 'Blue Pen',
    'price': 2.5,
    'category': 'Office',
}
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in product.items()
    if chave != 'categoria'
}
# print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

print(dict(lista))

