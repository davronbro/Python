# Task 1: For Loop with a List

brands = ["UFC", "Venom", "BMW", "Exel"]
for brand_name in brands:
  print(f"Brand name: {brand_name}")


# Task 2: While Loop with a Condition

discount = 11
while discount > 0:
  print(f"Discount days left: {discount}")
  discount -= 1

# Task 3: If-Else Conditional

price = 100
if price < 200:
  print("cheap")
else:
  print("pricey")

# Task 4: Combine Loop and Conditional

products = {"burger": 50, "car": 6000, "market": 12900}
for item, price in products.items():
  if price < 1000:
    print(f"{item}: {price} -> Affordable")
  else:
    print(f"{item}: {price} -> Luxury")