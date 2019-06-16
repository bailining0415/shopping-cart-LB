# shopping_cart.py

#from pprint import pprint

import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# pprint(products)

# TODO: write some Python code here to produce the desired output

import pprint
products_dict = dict([(prod['id'], prod) for prod in products])

is_done = False
item_numbers = []
while not is_done:
    item_number = input("Please input a product identifier: ")
    
    if item_number == 'DONE':
        is_done = True
    else:
        try:
            item_number = int(item_number)
            if item_number >= 0 and item_number <= 20:
                invalid_input = False
            else:
                invalid_input = True
        except ValueError:
            invalid_input = True

        if invalid_input:
            print('Hey, are you sure that product identifier is correct? Please try again!')
        else:
            item_numbers.append(item_number)

print("SHOPPING CART ITEM IDENTIFIERS INCLUDE:", item_numbers)

# https://stackoverflow.com/questions/311627/how-to-print-a-date-in-a-regular-format

header = """
#> ---------------------------------
#> Lining Bai GROCERY
#> WWW.Lining-Bai-GROCERY.COM
#> ---------------------------------
#> CHECKOUT AT: {}
#> ---------------------------------
#> SELECTED PRODUCTS:
"""

footer = """
#> ---------------------------------
#> SUBTOTAL: ${:.2f}
#> TAX: ${:.2f}
#> TOTAL: ${:.2f}
#> ---------------------------------
#> THANKS, SEE YOU AGAIN SOON!
#> ---------------------------------
"""
print(header.format(datetime.datetime.now()))

total = 0.0

for item_number in item_numbers:
    prod = products_dict[item_number]
    print("#> ... {} (${:.2f})".format(prod['name'], prod['price']))
    total += prod['price']

tax = total * 0.0875

print(footer.format(total, tax, total + tax))

