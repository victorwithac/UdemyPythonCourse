import random


nove_digitos = ''
for i in range(9):
    nove_digitos = nove_digitos + str(random.randint(0, 9))


# cpf = '861.646.190-68'.replace('.', '').replace('-', '')

contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

#Código para segundo dígito do CPF

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 < 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if dez_digitos == cpf_gerado_pelo_calculo:
    print('\033[1;32mCPF Válido\033[m')
else: 
    print('\033[1;31mCPF Inválido\033[m')
print(cpf_gerado_pelo_calculo)