class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}\nКухня: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"Ресторан открыт!")


name=input("Ввод названия: ")
cuisine=input("Ввод типа кухни: ")
r_i=Restaurant(name, cuisine)
r_i.describe_restaurant()
r_i.open_restaurant()
