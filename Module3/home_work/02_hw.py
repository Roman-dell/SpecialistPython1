# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here


n = int(input("n:"))  # колличество
i = 0
while i < n:
    number = random.randint(-100,100)  # Диапозон произвольных чисел.
    numbers.append(number)
    i += 1
print(numbers)
