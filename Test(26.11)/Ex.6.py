my_favorite=['pizza', 'falafel', 'carrot cake']
friend_favorite=my_favorite[:]
ice_cream=input('Введите мороженое которое любит друг: ')
friend_favorite.append(ice_cream)

print(f'Мои любимые блюда: ')
for i in my_favorite:
    print(f'---{i}')

print(f'Любимые блюда друга: ')
for i in friend_favorite:
    print(f'---{i}')
    


    
