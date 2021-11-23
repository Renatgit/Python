suma=int(input('Введите сумму которую вы хотите положить: '))
procent=int(input('Введите под какой процент вы хотите положить деньги: '))
year=int(input('Введите на сколько лет вы хотите положить: '))
for i in range(year):
    suma=suma+suma*procent/100
    i=i+1
    print(int(suma))
