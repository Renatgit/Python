def pizza(*called):
    print(f'Вы выбрали такую пиццы:')
    for i in called:
        print(f'- {i.title()}')
pizza('gavai')
pizza('paperonni', 'four cheese', 'meat_piz')
