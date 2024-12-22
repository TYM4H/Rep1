from math import *
from datetime import *

print(sqrt(36))

now = datetime.now()

print(f'Текущий год: {now.year}')
print(f'Текущий месяц: {now.month}')
print(f'День {now.day}')
print(f'Время: {now.strftime("%H:%M")}')