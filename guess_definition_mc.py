import csv
import random

# change filename to whatever you CSV is called (without the file extension)
filename = 'pathology' # input('CSV filename: ')
f = open('{}.csv'.format(filename), encoding='utf8')
data = list(csv.reader(f))

count = len(data)
while True:
    random.shuffle(data)
    answer, terms = data[0], data[0:4]
    random.shuffle(terms)
    for i in range(0, 4):
        if len(answer) > 2:
            def_list = ', '.join(terms[i][1:])
            def_list = def_list.split(', ')
        else:
            def_list = terms[i][1].split(', ')
        random.shuffle(def_list)
        print('{}: {}'.format(i+1, def_list[0]))

    print('Hint: {}'.format(answer[0]))
    response = ''
    while (not response.isdigit()) and (response not in ['s', 'q']):
        response = input('> Enter # choice, (s)kip question, or (q)uit program: ')
    if response == 's':
        print('')
        continue
    elif response == 'q':
        break
    elif terms[int(response)-1][0] == answer[0]:
        print('Correct!\n')
    else:
        for i in range(0, 4):
            if terms[i][0] == answer[0]:
                print('Wrong! The right answer was {}'.format(i+1))
        if len(answer) > 2:
            definition = ', '.join(answer[1:])
        else:
            definition = answer[1]
        print('\tFull description: {}\n'.format(definition))

print('Goodbye!')
f.close()
