questions = [
    {
        'questions_key': 'What is the result of 2+2?',
        'options_key': ['1','3', '4', '5'],
        'answers_key': '4',
    },
    {
        'questions_key': 'What is the result of 5*5?',
        'options_key': ['25', '55', '10', '51'],
        'answers_key': '25',
    },
    {
        'questions_key': 'What is the result of 10/2?',
        'options_key': ['4', '5', '2', '1'],
        'answers_key': '5',

    },
]
qtd_acertos = 0
for question in questions:
    print('Question:',question['questions_key'])
    print()

    options = question['options_key']
    for index, option in enumerate(options):
        print(f'{index + 1}) {option}')
    print()

    # print(options)
    # print(question)
    # print(question['answers_key'])
    choice = input('Choice a option: ')

    acertou = False
    choice_int = None
    qtd_option = len(options)

    if choice.isdigit():
        choice_int = int(choice) - 1
    # print(options[choice_int], question['answers_key'] )
    # print(choice_int)

    print()

    if choice_int is not None:
        if choice_int >= 0 and choice_int <= qtd_option:
            if options[choice_int] == question['answers_key']:
                acertou = True

    if acertou:
        print('\033[1;32mAcertou!\033[m')
        qtd_acertos += 1
    else:
        print('\033[1;31mErrou!\033[m')
    print()

print(f'Você acertou {qtd_acertos} perguntas!')
