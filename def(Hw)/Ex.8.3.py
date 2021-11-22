def make_shirt(size, text):
    print(f'Принято! \nФутболка с размером: {size.title()} \nС надписью: {text}')

#Основной код
s=input('Введите размер футболки: ')
t=input('Введите текст, который будет изображен на футболке: ')
make_shirt(s, t)
