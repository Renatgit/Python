people={
    'Renat':{
        'first_name':'Renat',
        'last_name':'Bershadskiy',
        'age':14,
        'city':'Krivoy Rog'
        },
    'Kirill':{
        'first_name':'Kirill',
        'last_name':'Antonov',
        'age':15,
        'city':'Krivoy Rog'
        },
    'Vania':{
        'first_name':'Vania',
        'last_name':'Thsurkan',
        'age':15,
        'city':'Krivoy Rog'
        }
    }

for k, v in people.items():
    print("-"*30)
    print(f"Информация об {k}: ")
    user_info=f"{v['first_name']} {v['last_name']}"
    age=f"{v['age']}"
    city=f"{v['city']}"
    print(f"\tИмя фамилия: {user_info.title()}")
    print(f"\tВозраст: {age}")
    print(f"\tГород: {city}")
