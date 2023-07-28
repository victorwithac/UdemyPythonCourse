questions = [
    {
        'Question': 'What is the result of 2+2',
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
    print('Question:', c['Question'])

    for i, v in enumerate(c['Options']):
        print(f'{i+1}) {v}')
