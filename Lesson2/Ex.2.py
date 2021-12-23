num = int(input('Сумма: '))
p = int(input('Процент: '))
a = int(input('Через сколько месяцев хотите забрать сумму: '))
if a > 12 :
    num2 = num +num * (p/100)
    print(num2)
else:
     print(num)
