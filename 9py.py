def sum(n):
    sum = 0
    while n > 0:
        r = n % 10
        if r % 2 != 0:
            sum = sum + r
        n = int(n / 10)
    print('Сумма нечетных цифр числа равна', sum)
flag = True
while flag:
    try:
        n = int(input('Введите натуральное число'))

    except ValueError:
        print('Ошибка. Проверьте введённые данные и повторите попытку')
    else:
        flag = False
if n <= 0:
    print ('Ошибка. Проверьте введённые данные и повторите попытку')
else:
    sum(n)