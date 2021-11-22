def make_album(exeсutor, alb, num):
    if num>0:
        print(f'\nИсполнитель: {exeсutor.title()} \nАльбом: {alb.title()} \nКоличество дорожек в альбоме: {num}')
    else:
       print(f'\nИсполнитель: {exeсutor.title()} \nАльбом: {alb.title()} \nКоличество дорожек в альбоме: Неизвестно!') 

    
#Основной код
while True:
    ex=input('Введите исполнителя, если вы уже внесли всех желаемых исполителей введите `q` для завершения: ')
    if ex=='q':
        break
    al=input('Введите название альбома: ')
    n=int(input('Введите количество дорожек в альбоме, если не знаете введите `0`: '))
    make_album(ex, al, n)
