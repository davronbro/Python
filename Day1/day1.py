# Day 1: Variables and Basic Data Types (Strings, Integers, Floats)

# Variables: Think of a variable as a labeled box where you store stuff (data).


# Data Types: The kind of data you store in a variable. Today, we’re focusing on:
  # Strings: Text, like product names or descriptions (e.g., "iPhone"). Always in quotes ("" or '').
  # Integers: Whole numbers, like quantities in a cart (e.g., 5 for 5 items). No decimal point.
  # Floats: Numbers with decimals, like prices (e.g., 999.99 for $999.99).


# Basic Operations:
  # For numbers (integers/floats): Add (+), subtract (-), multiply (*), divide (/).
  # For strings: Combine them (concatenation, e.g., "iPhone" + " Case").
  # You can’t mix types directly (e.g., "iPhone" + 999.99 will crash unless you convert the number to a string).

# Create variables for a product (like on your e-commerce site)
product_name = "iPhone 14"  # String: the product's name
price = 999.99  # Float: the price with decimals
quantity = 3  # Integer: number of items in stock

# Print the variables to see their values
print(product_name)  # Output: iPhone 14
print(price)  # Output: 999.99
print(quantity)  # Output: 3

"""
  Breakdown:
    product_name = "iPhone 14": Creates a variable product_name and stores the string "iPhone 14". Strings need quotes.
    price = 999.99: Stores a float (decimal number) in price. No quotes needed for numbers.
    quantity = 3: Stores an integer (whole number) in quantity.
    print(): A Python function that displays stuff in the terminal. We pass the variable names to show their values.

"""
#------------------------------

# Calculate the total cost of items
total_cost = price * quantity
print (total_cost)

# Create a message by combining strings
message = product_name + " costs $" + str(total_cost)
print (message)

#------------------------------

# Example

  # This will crash!
  # bad_code = product_name + price  # Trying to add a string and a float

# Fix it with type conversion
fixed_code = product_name + " costs $" + str(price)
print(fixed_code)  # Output: iPhone 14 costs $999.99

"""
 Breakdown:

  product_name + price: This crashes because you can’t add a string ("iPhone 14") and a float (999.99). Python throws a TypeError.
  str(price): Converts the float to a string ("999.99"), so now you can concatenate.
  Why?: Shows why type conversion matters. You’ll hit errors like this in backend dev, so we’ll learn to fix them.

"""