import random
from dataclasses import dataclass
from enum import IntEnum
from collections import defaultdict
from tabulate import tabulate

class Vegetable(IntEnum):
    # Enum representing different vegetable types
    Tomato = 1
    Potato = 2
    Cucumber = 3
    Pumpkin = 4
    Corn = 5

@dataclass
class Product:
    # Data structure for a Product containing an ID, type, and price 
    product_id: int
    product_type: Vegetable
    product_price: float

def generate_products(num_items=75_000):
    for product_id in range(1, num_items + 1):
        product_type = random.choice(list(Vegetable))
        product_price = round(random.uniform(0.10, 2.15), 2)
        yield Product(product_id, product_type, product_price)

def calculate_average_price(products):
    price_sum = defaultdict(float)
    count = defaultdict(int)

    for product in products:
        price_sum[product.product_type] += product.product_price
        count[product.product_type] += 1

    return {veg.name: round(price_sum[veg] / count[veg], 2) for veg in price_sum}

def display_statistics(avg_prices):
    table_data = [[veg, price] for veg, price in avg_prices.items()]
    print(tabulate(table_data, headers=["Product", "Average Price"], tablefmt="grid"))

if __name__ == "__main__":
    products = generate_products()
    avg_prices = calculate_average_price(products)
    display_statistics(avg_prices)
