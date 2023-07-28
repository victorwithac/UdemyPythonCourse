import os
lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao in 'Ii':
        os.system('cls')
        lista.append(input('Valor: '))
    elif opcao in 'Aa':
            try:
                indice = int(input('Indice: '))
                del lista[indice]
            except:
                print('Não foi possível apagar esse índice.')

    elif opcao in 'Ll':
        os.system('cls')
        for indice, item in enumerate(lista):
            print(indice, item)

    else:
        print('Opção inválida')


