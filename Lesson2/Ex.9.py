import math
a = int(input('Сторона: '))
r = int(input('Радиус: '))


b = (r * math.sqrt(3))/6
if b==a :
    print('Yes!')
else:
    print('No!')
