# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321
def palindrome(number):
    r_number = number
    result = 0

    while number != 0:
        digit = number % 10
        result = result * 10 + digit
        number = int(number / 10)

    return result == r_number
