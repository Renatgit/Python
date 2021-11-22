def burger(*components):
    print('Бургер с такими компонентами: ')
    for i in components:
        print(f"- {i.title()}")
        
#  Основная программа
burger('Cheese')
burger('cutlet', 'onion', 'tomato')
burger('cheese', 'tomato', 'salad', 'cutlet', 'ketchup')
