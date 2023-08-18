questions = [
    {
        'Question': 'What is the result of 2+2?',
        'Options': ['1','3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'What is the result of 5*5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'What is the result of 10/2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]









for c in questions:
    print(c['Question'])
    resposta = 0
    options = c['Options']
    for x, y in enumerate(options):
        print(f'{x}) {y}')
    resposta = input('Choose an Option: ')
    qtd_options = len(options)
    acertou = False
    if resposta.isdigit():
        resposta_int = int(resposta)

    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_options:
            if options[resposta_int] == c['Answer']:
                acertou = True

    if acertou:
        print('Acertou')
    else:
        print('Errou')


