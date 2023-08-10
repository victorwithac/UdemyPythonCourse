#HIGHER ORDER FUNCTIONS
#FUNÇÕES DE PRIMEIRA CLASSE

# def saudation(x, y):
#     return x, y
#
# def executa(funcao, *args):
#     return funcao(*args)
#             # saudation('oi', 'hello')
#
#
# v = executa(saudation,'oi', 'hello')
# print(v)
#





# def executa(funcao, msg):
#     return funcao(msg)
#
# var = executa(saudacao, 'bom dia')
# print(var)

def saudar(msg, nome):
    return f'{msg} {nome}'

def executar(funcao, *args):
    return funcao(*args)

print(executar(saudar, 'Boa noite', 'Victor'))