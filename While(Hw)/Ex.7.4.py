while True:
    q=input('Введите ``add`` если хотите что-то добавить! \nВведите ``quit`` если вы добавили всё что хотели! ')
    if q=='add':
        addition=input('Что бы вы хотели добавить в пиццу: ')
        print(f'Мы добавили в пиццу {addition}')
    elif q=='quit':
        print('Ваш заказ принят!')
        break
    else:
        continue
    
    
