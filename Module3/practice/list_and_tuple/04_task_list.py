# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
import random

numbers = []
n = int(input("n:"))  # колличество
i = 0
while i < n:
    number = random.randint(-10,10)  # Диапозон произвольных чисел.
    numbers.append(number)
    i += 1
print(numbers)

for el in numbers:
    if el > 0:
        el+=el
print(el)
