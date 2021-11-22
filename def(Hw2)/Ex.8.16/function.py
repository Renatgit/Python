def pizza(size, *called):
    print(f'Вы выбрали такие пиццы с размером {size}:')
    for i in called:
        print(f'- {i.title()}')
