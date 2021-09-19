# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here
mount = int(input())

if mount == 1 and 1 <= mount <= 12:
    print('Январь')
elif mount == 2 and 1 <= mount <= 12:
    print('Февраль')
elif mount == 3 and 1 <= mount <= 12:
    print('Март')
elif mount == 4 and 1 <= mount <= 12:
    print('Апрель')
elif mount == 5 and 1 <= mount <= 12:
    print('Май')
elif mount == 6 and 1 <= mount <= 12:
    print('Июнь')
elif mount == 7 and 1 <= mount <= 12:
    print('Июль')
elif mount == 8 and 1 <= mount <= 12:
    print('Август')
elif mount == 9 and 1 <= mount <= 12:
    print('Сентябрь')
elif mount == 10 and 1 <= mount <= 12:
    print('Октябрь')
elif mount == 11 and 1 <= mount <= 12:
    print('Ноябрь')
elif mount == 12 and 1 <= mount <= 12:
    print('Декабрь')
