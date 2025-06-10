# Task 1: Create a Dictionary

products = {"name": "BMW", "price": 55000, "discount": 5}

print(products)
print(products["name"])
print(products.get("discount"))
print(products.get("color", products["price"]))


# Task 2: Modify the Dictionary

products["category"] = "Premium Class"
print(products)

products["discount"] = 10
products["price"] = 52250
print(products)


# Task 3: Loop Through the Dictionary

for key in products.keys():
  print(key)
for value in products.values():
  print(value)
for key, value in products.items():
  print(f"{key}: {value}") 


# Task 4: Cart Dictionary

order = {"BMW": 5, "Premium Class": 2, "Not Premium": 3}

total_items = sum(order.values())
print(total_items)

# My personal example

color = order.get("color")
print(color)

if "color" in order:
  print(order["color"])
else:
  print("Key not found!")