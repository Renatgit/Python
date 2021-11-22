cities={
    'Krivoy Rog':{
        'country':'Ukraine',
        'population':634780,
        'fact':'Самый длинный город в Европе'
        },
    'Tokyo':{
        'country':'Japan',
        'population':34500000,
        'fact':'Город с наибольшим количеством населения'
        },
    'Monaco':{
        'country':'Monaco',
        'population':39244,
        'fact':'Город с наибольшей ожидаемой продолжительностью жизни'
        }
    }

for k,v in cities.items():
    print('-'*30)
    for k_1, v_1 in v.items():
        country=f"\n\tГород находится в стране: {v['country']}"
        population=f"\n\tНаселение города: {v['population']} человек"
        fact=f"\n\tИнтересный факт: {v['fact']}"
    print(f'Информация об городе {k}:{country}{population}{fact}')
