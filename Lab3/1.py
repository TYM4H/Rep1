def reading(f, type='1'):
    if type == '1':
        with open(f, 'r') as file:
            content = file.read()
            return content
    else:
        with open(f, 'r') as file:
            return [line for line in file]

f = input(f'Введите название файла: ')
type = input(f'Выберите тип чтения (1/2): ')

try:
    print(reading(f, type))
except FileNotFoundError:
    print('Такого файла не существует(')
