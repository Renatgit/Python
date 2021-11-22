name_user={
    'Ivan':15,
    'Kirill':49,
    'Renat':14,
    'Den':24,
    'Nella':18
    }

user_auto={
    'Jigul':1990,
    'Ferrari':2021,
    'BMW':2020
    }
about_life=[name_user, user_auto]
print(about_life)

for i in about_life:
    print(i)

empty=[]
for x in range(30):
    new_item={
        'Color':'grey',
        'Speed':50,
        'Temp':-10
        }
    empty.append(new_item)
    print(empty)
for f in empty[:10]:
    if f['Color']=='grey':
        f['Color']='black'
        f['Speed']=100
        f['Temp']=0
        
for y in empty:
    print(y)
