def greet_user(username, surname):
    print(f'Hello, {username.title()} {surname.title()}')
name=input('Введите имя: ')
name_user=input('Введите Фамилию: ')
greet_user(name, name_user)

