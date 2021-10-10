# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    our_number = str(number)
    return our_number == our_number[::-1]

def numbers_palindromes(a, b):
    num_palindromes = 0
    for i in range(a, b):
        if palindrome(i):
            num_palindromes += 1
    return num_palindromes
print(numbers_palindromes(10, 20))
