soum=int(input('Укажите количество денег на счету: '))
percent=int(input('Укажите процент: '))
year=int(input('Укажите месяц снятия: '))
if (year>11) and (year<24):
    soum_one_year=soum+soum*(percent/100)
    print('Ваша сумма равна: ', soum_one_year)
elif (year>23) and (year<37):
    soum_one_year_1=soum+soum*(percent/100)
    soum_two_year=soum_one_year_1+soum_one_year_1*(percent/100)
    print('Ваша сумма равна: ', soum_two_year)
elif (year>36) and (year<49):
    soum_one_year_1=soum+soum*(percent/100)
    soum_one_year_2=soum_one_year_1+soum_one_year_1*(percent/100)
    soum_three_year=soum_one_year_2+soum_one_year_2*(percent/100)
    print('Ваша сумма равна: ', soum_three_year)
else:
    print('Ваша сумма равна: ', soum)
    

