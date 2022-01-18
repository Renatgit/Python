class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name=shop_name
        self.store_type=store_type
        self.number_of_units=0
    def describe_shop(self):
        print(f"Info about shop:\n\tShop: {self.shop_name}\n\tType: {self.store_type}\n\tNumber of units: {self.number_of_units}")
    def open_shop(self):
        print(f"\tМагазин открыт!")
    def set_number_of_units(self):
        n=int(input("Введите количество видов товара: "))
        self.number_of_units=n
    def increment_number_of_units(self):
        self.number_of_units+=1200

class Discount(Shop):
    def get_discount_products(self, d):
        print("Discount prodicts: ")
        for i in d:
            print(f"---{i}")
