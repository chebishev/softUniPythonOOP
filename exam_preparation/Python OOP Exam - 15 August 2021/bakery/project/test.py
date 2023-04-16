from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.bakery import Bakery


bakery = Bakery("Bakery")
print(bakery.add_food("Cake", "Tiramisu", 5.80))
print(bakery.add_food("Bread", "Pan", 5))
print(bakery.add_drink("Water", "Table water", 500, "Hisar"))
print(bakery.add_drink("Tea", "Nestea", 500, "Coca cola"))
print(bakery.add_table("InsideTable", 12, 8))
print(bakery.add_table("OutsideTable", 52, 20))
print(bakery.reserve_table(12))
print(bakery.order_food(12, "Pan", "Мусака", "Шопска салата", "Тирамису", "Tiramisu"))
print(bakery.order_drink(12, "Nestea", "Ракия", "Пепси", "Table water"))
print(bakery.leave_table(12))
# bakery.add_table("InsideTable", 1, 20)
# bakery.add_table("InsideTable", 2, 10)
# bakery.add_table("OutsideTable", 51, 10)
# bakery.add_table("OutsideTable", 53, 10)
print(bakery.get_free_tables_info())
print(bakery.get_total_income())