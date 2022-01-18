from shop import *
store=Shop("Rozetka", "ishop")
x=store.__dict__
for i in x.values():
    print(i)
store.describe_shop()
store.open_shop()
store.set_number_of_units()
store.describe_shop()
store.increment_number_of_units()
store.describe_shop()

store_1=Shop("Sinsay", "clothing store")
store_1.describe_shop()

discount_products=["monitors", "keyboards", "loudspeakers"]
store_discount=Discount("", "")
store_discount.get_discount_products(discount_products)

