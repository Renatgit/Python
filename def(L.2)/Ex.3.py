def pizza(size, *called):
    print(f'Вы выбрали такие пиццы с размером {size}:')
    for i in called:
        print(f'- {i.title()}')
#Оснавная программа
l=str(input('Введите размер пиццы: '))
pizza(l, 'gavai')
pizza(l, 'paperonni', 'four cheese', 'meat_piz')
