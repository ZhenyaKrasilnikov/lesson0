print('Нет равных чисел. Вывод:0')
first = int(input('введите число: '))
second = int(input('введите число: '))
third = int(input('введите число: '))

if first != second != third != first:
    print(0)
else:
    print('Введите другое число')

print('Два равных числа из трех. Вывод:2')
first = (input('введите число: '))
second = (input('введите число: '))
third = (input('введите число: '))
if first == second != third:
    print(2)
elif first != second == third:
    print(2)
elif first != second != third == first:
    print(2)
else:
    print('Введите другое число')

print('Три равных числа. Вывод:3')
first = (input('введите число: '))
second = (input('введите число: '))
third = (input('введите число: '))
if first == second == third == first:
    print(3)
else:
    print('Введите другое число')
