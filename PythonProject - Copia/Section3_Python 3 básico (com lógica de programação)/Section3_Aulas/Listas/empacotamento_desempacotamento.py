nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
print(type(nome3))
print(type(nomes))
#
# Código acima igual ao código abaixo

#A variável nome vai pegar o primeiro elemento da lista
#enquanto que o resto da lista independente do número de
#elementos que nela tenha irá ficar com o "*resto".
nome, *resto = ['Maria', 'Helena']
print(type(resto))
print(type(nome))

# ou

# Como convenção se usa o underline para mostrar que
# o resto da lista não será usada, que não importa...
nome, *_ = ['Maria', 'Helena']
print(type(_))
print(type(nome))

_, _, nome, *_ = ['Maria', 'Helena', 'Luiz']
print(nome)
print(_)
