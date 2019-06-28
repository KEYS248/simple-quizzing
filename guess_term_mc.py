import csv
import random

# change filename to whatever you CSV is called (without the file extension)
filename = 'pathology' # input('CSV filename: ')
f = open('{}.csv'.format(filename), encoding='utf8')
data = list(csv.reader(f))
count = len(data)
while True:
    middle = random.randint(2, len(data)-4)
    terms = data[middle-2:middle+4]
    random.shuffle(terms)
    answer = terms[random.randint(0, 5)]
    for i in range(0, 6):
        print('{}: {}'.format(i+1, terms[i][0]))
    if len(answer) > 2:
        def_list = ', '.join(answer[1:])
        def_list = def_list.split(', ')
    else:
        def_list = answer[1].split(', ')
    random.shuffle(def_list)
    print()
    random.shuffle(def_list)
    def_count = 0

    response, prompt, menu_options = 'a', '> Enter # choice, (a)nother hint, (s)kip question, or (q)uit program: ', ['1', '2', '3', '4', '5', '6', 'a', 's', 'q']
    while response == 'a':
        print('--- Hint --- {}'.format(def_list[def_count]))
        def_count += 1
        if def_count >= len(def_list):
            print('Out of hints!')
            prompt, menu_options = '> Enter # choice, (s)kip question, or (q)uit program: ', ['1', '2', '3', '4', '5', '6', 's', 'q']
        response = input(prompt)
        while response not in menu_options:
            response = input(prompt)
    if response == 's':
        print('')
        continue
    elif response == 'q':
        break
    elif terms[int(response)-1][0] != answer[0]:
        print('--- Wrong! --- \nThe right answer was {}\n'.format(answer[0]))
    else:
        print('=== Correct! ===\n')
print('Goodbye!')
f.close()
