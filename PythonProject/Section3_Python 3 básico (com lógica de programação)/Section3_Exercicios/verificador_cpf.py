# cont = 10
# soma = 0
# multiplicacao = 0
# soma_total = 0
# multi_dez = 0
# resto_divisao = 0
# digito = 0
#
# lista = input('Digite seu CPF: ')
# lista = list(lista)
# valor_guardado = int(lista[-2])
#
# if len(lista) > 9:
#     del lista[-1]
#     del lista[-1]
# if '.' in lista:
#     del lista[3]
#     del lista[6]
# if '-' in lista:
#     del lista[-1]
#
# for c in lista:
#     multiplicacao = int(c) * cont
#     soma_total += multiplicacao
#     cont -= 1
# multi_dez = soma_total * 10
# resto_divisao = multi_dez % 11
# digito = resto_divisao
#
# if resto_divisao > 9:
#     digito = 0
# else:
#     digito = resto_divisao
#
# if digito == valor_guardado:
#     print('\033[1;32mCPF Válido\033[m')
# else:
#     print('\033[1;31mCPF Inválido\033[m')

# Código do professor
# import re
# import sys
#
# entrada = '861.646.190-68'.replace('.', '').replace('-', '')


#método sub (substituir)
# cpf = re.sub(r'[^0-9]',
#              '',
#              entrada
#              )
# print(cpf)
#
# entrada_e_sequencial = entrada == entrada[0] * len(entrada)
#
# print(entrada_e_sequencial)

# nove_digitos = cpf[:9]
# contador_regressivo_1 = 10
#
# resultado_digito_1 = 0
# for digito_1 in nove_digitos:
#     resultado_digito_1 += int(digito_1) * contador_regressivo_1
#     contador_regressivo_1 -= 1
# digito_1 = (resultado_digito_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0
#
# #Código para segundo dígito do CPF
#
# dez_digitos = cpf[:10]
# contador_regressivo = 11
# resultado_digito_2 = 0
#
# for digito in dez_digitos:
#     resultado_digito_2 += int(digito) * contador_regressivo
#     contador_regressivo -= 1
# digito_2 = (resultado_digito_2 * 10) % 11
# digito_2 = digito_2 if digito_2 < 9 else 0
#
# cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
# if cpf == cpf_gerado_pelo_calculo:
#     print('\033[1;32mCPF Válido\033[m')
# else:
#     print('\033[1;31mCPF Inválido\033[m')

# if int(cpf[-1]) == resultado:
#     print('\033[1;32mCPF Válido\033[m')
# else:
#     print('\033[1;31mCPF Inválido\033[m')




