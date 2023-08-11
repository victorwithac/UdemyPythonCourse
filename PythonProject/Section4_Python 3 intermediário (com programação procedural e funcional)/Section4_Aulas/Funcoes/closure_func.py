# #Closure

def maior(saudacao):
    def menor(nome):
        return f'{saudacao}, {nome}'
    return menor

falar_bom_dia = maior('Bom dia')
falar_boa_noite = maior('Boa noite')

print(falar_bom_dia('Victor'))
print(falar_boa_noite('Victor'))


for nome in ['Maria', 'José', 'João']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))


# def funcao(x):
#     def nova_funcao():
#         print('this')
#         return 'and this'
#     return nova_funcao
#
# var = funcao(2)
# print(var())
# # print(type(var))
