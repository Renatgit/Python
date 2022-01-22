class User:
    def __init__(self, first_name, second_name, age, phone_number, year_of_birth):
        self.first_name=first_name
        self.second_name=second_name
        self.age=age
        self.phone_number=phone_number
        self.year_of_birth=year_of_birth
        self.login_attempts=0
    def desacribe_user(self):
        print(f"Информация о пользователе {self.first_name} {self.second_name}:\n\tИмя: {self.first_name}\n\tФамилия: {self.second_name}\n\tВозраст: {self.age}\n\tНомер телефона: {self.phone_number}\n\tГод рождения: {self.year_of_birth}")
    def greet_user(self):
        print(f"{self.first_name} {self.second_name} приветсвуем!")
    def info_login_attempts(self):
        print(f"Попытки входа: {self.login_attempts}")
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
    
first_name=input("Введите имя: ")
second_name=input("Введите фамилию: ")
age=input("Введите возраст: ")
phone_number=input("Введите номер телефона: ")
year_of_birth=int(input("Введите год рождения: "))
user_1=User(first_name, second_name, age, phone_number, year_of_birth)
user_1.desacribe_user()
user_1.greet_user()

l_a=User(first_name, second_name, age, phone_number, year_of_birth)
l_a.info_login_attempts()
l_a.increment_login_attempts()
l_a.increment_login_attempts()
l_a.increment_login_attempts()
l_a.info_login_attempts()
l_a.reset_login_attempts()
l_a.info_login_attempts()


