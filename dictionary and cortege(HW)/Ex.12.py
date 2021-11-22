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
        },
    'Hum Hum':{
        'country':'Croatia',
        'population':28,
        'fact':'Город с самым мвленьким населением на планете'
        }
    }

print(f'Выберите город о котором хотите узнать информацию:\n\t-Krivoy Rog\n\t-Tokyo\n\t-Monaco\n\t-Hum Hum')
u_city=input('Напишите город который вы выбрали(без орфографических ошибок!) ==> ')
for k,v in cities.items():
    if k==u_city:
        for k_1, v_1 in v.items():
            country=f"\n\tГород находится в стране: {v['country']}"
            population=f"\n\tНаселение города: {v['population']} человек"
            fact=f"\n\tИнтересный факт: {v['fact']}"
        print(f'Информация об городе {k}:{country}{population}{fact}')
    
        
