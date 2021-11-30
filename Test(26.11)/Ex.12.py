import random

n=int(input('Введите количество строк: '))
m=int(input('Введите количество столбцов: '))
k=int(input('Введите столбец, которую вы хотите вывести: '))
p=int(input('Введите строка, который вы хотите вывести: '))
r=int(input('Введите столбец: '))
t=int(input('Введите строка: '))
em_k=[]
matrix=[[random.randint(0, 9) for g in range(m)] for i in range(n)]

for i in matrix:
    print(f'|{i}|')
d=[matrix[i][g] for i in range(n) for g in range(m) if i==g]
print(f'Главная диагональ: {d}')

stroka=[matrix[p-1][g] for g in range(m)]
print(stroka)

stolbetc=[matrix[i][k-1] for i in range(n)]
print(stolbetc)
asdf=matrix[r-1][t-1]
print(asdf)


