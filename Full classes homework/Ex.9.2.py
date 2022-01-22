class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}\nКухня: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"Ресторан открыт!")


name_1=input("Ввод названия: ")
cuisine_1=input("Ввод типа кухни: ")
r_i_1=Restaurant(name_1, cuisine_1)
r_i_1.describe_restaurant()
r_i_1.open_restaurant()

name_2=input("Ввод названия: ")
cuisine_2=input("Ввод типа кухни: ")
r_i_2=Restaurant(name_2, cuisine_2)
r_i_2.describe_restaurant()
r_i_2.open_restaurant()

name_3=input("Ввод названия: ")
cuisine_3=input("Ввод типа кухни: ")
r_i_3=Restaurant(name_3, cuisine_3)
r_i_3.describe_restaurant()
r_i_3.open_restaurant()
