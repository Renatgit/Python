class Car:
    def __init__(self,mark, model, year):
        self.mark=mark
        self.model=model
        self.year=year
        self.adometr=0

    def get_discript_name(self):
        print("-"*40)
        print(f"Информация о новой машине:\n\tМарка:{self.mark} \n\tМодель: {self.model} \n\tГод: {self.year}")
    def read_adometr(self):
        print(f"\tПробег машины: {self.adometr} miles")
    def update_adometr(self, n):
        if n<self.adometr:
            print(f"Пробег скинуть невозможно!")
        else:
            self.adometr=n
    def increment_adometr(self, m):
        self.adometr+=m

class Petrolcar(Car):
    def __init__(self,mark, model, year, petrol):
        Car.__init__(self,mark, model, year)
        self.petrol=petrol
    def get_discript_name(self):
        Car.get_discript_name(self)
        print(f"\tОбъём бака: {self.petrol} liters")
    def costs(self, cost):
        print(f"\tЦена автомобиля: {cost} dollars")


while True:
    n=int(input('Введите пробег машины: '))
    if n>=0:
        break
    else:
        print(f"Пробег не может быть меньше нуля!")
my_new_car=Car('Audi', 'R7', '2021')
my_new_car.get_discript_name()
my_new_car.adometr=23
my_new_car.update_adometr(n)
my_new_car.read_adometr()
while True:
    m=int(input('Введите сколько миль вы проехали: '))
    if n>=0:
        break
    else:
        print(f"Расстояние не может быть меньше нуля!")
my_new_car.get_discript_name()
my_new_car.increment_adometr(m)
my_new_car.read_adometr()
while True:
    petrol=int(input('Введите объём бензобака: '))
    if petrol>=40 and petrol<=100:
        break
    elif petrol<40:
        print(f"Слишком маленький бак для легкового автомобиля!")
    elif petrol>100:
        print(f"Слишком большой бак для легкового автомобиля!")
my_new_car_with_tank=Petrolcar('Audi', 'R7', '2021', petrol)
my_new_car_with_tank.get_discript_name()
while True:
    cost=int(input('За сколько вы хотите купить машину: '))
    if cost>=1000000:
        break
    else:
        print(f"Слишком маленькая цена за этот автомобиль!")
my_new_car_with_tank.get_discript_name()
my_new_car_with_tank.costs(cost)
