produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco':produto['preco'] * 2}
    for produto in produtos
]
print(*novos_produtos, sep='\n')

