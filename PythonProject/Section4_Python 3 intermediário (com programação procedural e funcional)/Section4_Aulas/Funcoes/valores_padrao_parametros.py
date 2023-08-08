#Valor padrão de parâmetro é o valor atribuido a ele na função

# def soma(x, y, z=None):
#     if z is not None:
#         print(f'{x=}, {y=} {z=}', '=', x + y + z)
#     else:
#         print(f'{x=} {y=}', '=', x + y)
#
# soma(1, 2)
# soma(3, 5)
# soma(100, 200)
# soma(5, 3, 0)
# soma(x=3, y= 4, z=4)

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', '|', x + y + z)
    else:
        print(f'{x=} {y=}', '|', x + y)

soma(1, 2, 5)
soma(y=2, z=3, x=4)

