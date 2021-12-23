a = int(input('Введите ваш рост: '))
if a > 180:
    print('Мальчик')
elif a<=180 and a>150 :
    print('Девочка')
elif a<1:
    print('Такого роста быть не может!')
else:
    print('Ребенок')
