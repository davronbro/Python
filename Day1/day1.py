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

# Example 1: Storing and Printing Product Data
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
    Why?: This is like storing data for a product on your site (name, price, stock).
"""
#--------------------------------------------

# Example 2: Basic Operations (Math and Concatenation)
  # Calculate the total cost of items
total_cost = price * quantity
print (total_cost)

# Create a message by combining strings
message = product_name + " costs $" + str(total_cost)
print (message)

"""
  Breakdown:
    total_cost = price * quantity: Multiplies price (999.99) by quantity (3) to get 2999.97. You can use +, -, *, / with integers and floats.
    message = product_name + " costs $" + str(total_cost):
    Concatenates (joins) strings using +.
    str(total_cost) converts the float 2999.97 to a string ("2999.97") because you can’t add a number to a string directly.
    The result is one big string: "iPhone 14 costs $2999.97".
    print(message): Shows the message in the terminal.
    Why?: This is like calculating a cart total or displaying a product summary on your site.
"""
#---------------------------------------------

# Example 3: What Happens with Errors?

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

#------------------------


# Day 1 Cheatsheet: Variables and Basic Data Types

# Variables:
    # Definition: A name that stores data (like a labeled box).
    # Syntax: variable_name = value
    # Example: product_name = "iPhone", price = 999.99
    # Tip: Names are case-sensitive (Price ≠ price).

# Data Types:
    # String: Text, in quotes.
        # Syntax: "text" or 'text'
        # Example: name = "Samsung Galaxy"
    # Integer: Whole number, no quotes.
        # Syntax: number
        # Example: quantity = 5
    # Float: Decimal number, no quotes.
        # Syntax: number.decimal
        # Example: price = 799.99

# Basic Operations:
    # Numbers (int/float):
        # Add: + (e.g., price + 10)
        # Subtract: - (e.g., quantity - 1)
        # Multiply: * (e.g., price * quantity)
        # Divide: / (e.g., price / 2)
   # Strings:
        # Concatenate: + (e.g., "Buy " + name)
        # Tip: Convert numbers to strings with str() (e.g., str(price)).

# Printing:
        # Syntax: print(value)
        # Example: print(name) → Samsung Galaxy
        # Tip: Use commas for multiple values: print(name, price) → Samsung Galaxy 799.99

# Type Conversion:
        # Convert number to string: str(999.99) → "999.99"
        # Why? Needed for concatenation (e.g., name + str(price)).

# Common Errors:
      # TypeError: Mixing types (e.g., "text" + 5).
          # Fix: Convert types (e.g., "text" + str(5)).
      # NameError: Using undefined variable (e.g., print(Price) when it’s price).
          # Fix: Check spelling and case.

# Mini-Project Note:
      # Started todo.py with a simple print("Buy Samsung Galaxy").
      # Next: Add lists to store multiple to-dos.


#---------------------------
