# #Closure

def maior(saudacao):
    def menor(nome):
        return f'{saudacao}, {nome}'
    return menor

falar_bom_dia = maior('Bom dia')
falar_boa_noite = maior('Boa noite')

print(falar_bom_dia('victor'))
print(falar_boa_noite('victor'))

for nome in ['Maria', 'José', 'João']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))



