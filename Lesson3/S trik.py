a=int(input('Введите сторону треугольника: '))
if a<=0:
    print('Сторона треугольника не может быть меньше или равна 0')
else:
    h=int(input('Введите высоту треугольника: '))
if h<=0:
    print('Высота треугольника не может быть меньше или равна 0')
else:
    s=a*h/2
    print('Площадь треугольника равна: ', s)
