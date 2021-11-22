favorite_numbers={
    'Kirill':[8, 88, 888],
    'Ivan':[7, 17, 71],
    'Den':[24,42],
    'Nella':15,
    'Dana':[99, 40],
    'Yarick':55,
    'Renat':3,
    'Misha':[11, 111],
    'Timur':[100, 94],
    'Artem':69,
    'Vlad(Oleg)':1,
    'Vlad':[0, 789]
    }

for k, v in favorite_numbers.items():
    print('-'*30)
    print(f'У {k.title()} любимые числа ---> {v}')
