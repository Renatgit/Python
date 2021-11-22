while True:
    yo=int(input('Введите возраст: '))
    if yo<0:
        print('Возраст не может быть меньше 0')
    elif (yo>=0) and (yo<3):
        print('Билет бесплатный!')
    elif (yo>=3) and (yo<12):
        print('Стоимость билета 10$')
    else:
        print('Стоимость билета 15$')
