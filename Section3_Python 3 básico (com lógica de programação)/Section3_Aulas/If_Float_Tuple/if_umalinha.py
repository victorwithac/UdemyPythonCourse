# Operação ternária (condicional de uma linha)
# <valor> if <condição> else <outro valor>

condiçao = 10 == 11
variavel = 'Variavel' if condiçao else 'Outro valor'
print(variavel)
digito = 9
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)
print('Valor' if False else 'Outro valor' if True else 'Fim')
