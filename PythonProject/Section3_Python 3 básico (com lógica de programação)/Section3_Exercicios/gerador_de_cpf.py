palavra_secreta = 'perfume'
letras_acertadas = ''  #GUARDAR OS VALORES QUE O USUÁRIO DIGITAR, JÁ QUE O WHILE SEMPRE QUE RECOMEÇA APAGA A VARIÁVEL...
numero_tentativas = 0
while True:
    digit_usuar = input('Digite uma letra: ')
    numero_tentativas += 1
    if len(digit_usuar) > 1:
        print('Digite apenas uma letra')
        continue
    if digit_usuar in palavra_secreta: #toda vez que letra que o usuário digitar estiver na palavra secreta
        letras_acertadas += digit_usuar #a letra acertada irá para a variavel onde são guardadas as letras acertadas

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
             palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU!! PARABÉNS!')
        print(f'Total de {numero_tentativas} tentativas.')
        break

string = 1
print('Hello World')
if 0>0:
    print('Hello World'

if 0>0:
    print('Hello World')