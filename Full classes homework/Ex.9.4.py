class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}\nКухня: {self.cuisine_type}\nКоличество обслуженный поситителей: {self.number_served}")
    def open_restaurant(self):
        print(f"Ресторан открыт!")
    def set_number_served(self, n):
        self.number_served=n
    def increment_number_served(self):
        self.number_served+=1

name=input("Ввод названия: ")
cuisine=input("Ввод типа кухни: ")
r_i=Restaurant(name, cuisine)
r_i.describe_restaurant()
r_i.open_restaurant()

n=int(input("Введите количество обслуженный поситителей: "))
r_i.set_number_served(n)
r_i.describe_restaurant()
r_i.increment_number_served()
r_i.describe_restaurant()
