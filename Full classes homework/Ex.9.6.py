class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}\nКухня: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"Ресторан открыт!")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        Restaurant.__init__(self, restaurant_name, cuisine_type)
        self.flavors=["Chocolate", "Fruits", "Ice", "Milk"]
    def flavors_info(self):
        f=self.flavors
        print(f"Мороженое в наличии: ")
        for i in f:
            print(f"~{i}")


name=input("Ввод названия: ")
cuisine=input("Ввод типа кухни: ")
r_i=Restaurant(name, cuisine)
r_i.describe_restaurant()
r_i.open_restaurant()

i_c_s=IceCreamStand("Iceman", "IceCream")
i_c_s.describe_restaurant()
i_c_s.flavors_info()
