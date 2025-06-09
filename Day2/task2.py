# Task 1: Create a List

cart = ["Ufc Gloves", "Venum Uniform", "BMW"]

print(cart)
print(cart[0])
print(cart[1:3])


# Task 2: Modify the List

cart.append("BYD Chazor")
print(cart)

cart.remove("Ufc Gloves")
print(cart)


# Task 3: Pop an Item

last_item = cart.pop()
print(last_item)
print(cart)


# Task 4: Work with Prices

rates = [ 322.22, 10, 11.11 ]
overall_rate = sum(rates)
overall_length = len(rates)

print(overall_rate, overall_length)