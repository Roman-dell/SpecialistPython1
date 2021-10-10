# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")

max_emp = staff[0]
for emp in staff:
    if emp["salary"] > max_emp["salary"]:
        max_emp =emp
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")
print(f"{max_emp['name']} {max_emp['surname']}")


print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

max_emp = staff[0]
for emp in staff:
    if emp["salary"] < max_emp["salary"]:
        max_emp = emp
print("Имя и Фамилию сотрудника с самой низкой зарплатой:")
print(f"{max_emp['name']} {max_emp['surname']}")


print("Среднеарифметическую зарплату всех сотрудников")

count = 0
sum_zp = 0
for emp in staff:
    sum_zp = sum_zp + emp['salary']
    count += 1
print("Среднеарифметическую зарплату всех сотрудников")
print(int(sum_zp / count))


print("Количество однофамильцев в организации")

# TODO: your code here

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

# TODO: your code here
