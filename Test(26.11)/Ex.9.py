n=int(input('Введите степегь в которую нужно возвести значение: '))
t_key=['Renat', 'Kirill', 'Den', 'Ivan', 'Timur', 'Artem']
t_value=[4, 9, 15, 3, 1, 7]
s=zip(t_key, t_value)
dct={k:[v**n] for k, v in s}
for key, value in dct.items():
    print(f'Я знаю твой ключ --> {key} его значение является -->{value}')

                
