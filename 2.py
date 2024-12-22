def reading(f, type='1'):
    if type == '1':
        with open(f, 'r') as file:
            content = file.read()
            return content

def writing(t):
    with open('user_input', 'w') as file:
        file.write(t)

def adding(t):
    with open('user_input', 'a') as file:
        file.write(t)

x = input('Записать тест в новый файл(1) или добавить к текущему(2)?: ')

if x == '1':
    t = input(f'Введите текст: ')
    writing(t)
else:
    t = input(f'Введите текст: ')
    adding(t)

print(f'Ваш файл: {reading('user_input')}')