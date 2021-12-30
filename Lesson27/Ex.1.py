class Human:
    def __init__(self,  name, age, surname, country_of_birth, time, time_now):
        self.name=name
        self.age=age
        self.surname=surname
        self.country_of_birth=country_of_birth
        self.time=time
        self.time_now=time_now
        print(f'Human created!!!\n')
    def info(self):
        print(f'Human({self.name}):\n\tName: {self.name}\n\tSurname: {self.surname}\n\tAge: {self.age}\n\tCountry of birth: {self.country_of_birth}\n\tStuding place: KPL')
    def study(self):
        return self.time_now-self.time
        

name=input('Введите ваше имя: ')
surname=input('Введите вашу фамилию: ')
age=int(input('Введите ваш возраст: '))
country_of_birth=input('Введите страну рождения: ')
time=int(input('Введите с какого года вы обучаетесь в КПЛ: '))
time_now=int(input('Введите год, который есть на данный момент: '))
hum=Human(name, age, surname, country_of_birth, time, time_now)
hum.info()
print(f'Время обучения в лицее: {hum.study()}')
