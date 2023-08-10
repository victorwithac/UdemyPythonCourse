# x = 1#
# def escopo():
#     x = 10
#     def outra_funcao():
#         global x
#         x = 11
#         y = 2
#         print(x, y)
#     outra_funcao()
#     print(x)
#     x = 5#
# print(x)
# escopo()
# print('*-*' * 15)
# print(x)


# def escopo(x):
#     # x = 10
#     def outra_funcao(y):
#         # y = 2
#         print(x, y)
#     outra_funcao(3)
#     return 'this'
#
# variavel = escopo(5)
# print(variavel)

# def  soma(x, y):
#     if x > 10:
#         return 10
#     return x + y
#
# soma1 = soma(11, 2)
# soma2 = soma(3, 3)
# print(soma1 + soma2)