# Day 2: Lists and Basic List Operations

# What Are Lists?
  # A list is a collection of items, like a shopping cart on your e-commerce site. It’s ordered (items have a position, starting at index 0) and mutable (you can change it after creating it).
  # Syntax:  my_list = ["item1, item2, item3]   <----
  # Eaxmple: cart = ["chair", "table", "lamp"]  <----
  # Why?: Lists are perfect for storing multiple products, to-dos, or prices. You’ll use them a ton in backend dev (e.g., to store all products in a database query).

# Key List Operations
  # Indexing: Access an item by position (starts at 0).
    # cart[0] → "chair"
  # Slicing: Get a subset of the list.
    # cart[1:3] → ["table", "lamp"]
  # Methods:
    # .append(item): Add an item to the end.
    # .remove(item): Remove the first occurrence of an item.
    # .pop(index): Remove and return an item at an index (default is last).
  # Length: len(cart) → 3 (number of items). Length: len(list) gives the number of items.
  # Sum: sum(list) adds up numbers in a list (if the list contains numbers).
# Why This Matters: For your e-commerce site, you’ll use lists to manage a user’s cart (e.g., ["chair", "table"]), calculate totals (e.g., [300.99, 150.50]), or store to-dos for your CLI app.

#---------------------------------------------


# Example 1: Creating and Accessing a List

# Create a list (like a cart on your site)
cart = ["chair", "table", "lamp"]

# Print the entire list
print(cart)  # Output: ['chair', 'table', 'lamp']

# Access items by index
print(cart[0])  # Output: chair (first item, index 0)
print(cart[2])  # Output: lamp (third item, index 2)

# Slice the list
print(cart[1:3])  # Output: ['table', 'lamp'] (items from index 1 to 2)

"""
Breakdown:
  cart = ["chair", "table", "lamp"]: Creates a list with 3 strings. Lists use square brackets [], and items are separated by commas.
  print(cart): Shows the whole list. Python prints lists with brackets and quotes for strings.
  cart[0]: Accesses the first item (index 0). Indexing starts at 0, so cart[2] is the third item.
  cart[1:3]: Slices the list from index 1 to 2 (includes 1 and 2, excludes 3). So, it gives ["table", "lamp"].
  Why?: This is like showing a user’s cart on your site or grabbing specific items to display.

"""
#---------------------------------------------

# Example 2: Modifying a List

# Add an item to the cart
cart.append("sofa")
print(cart)  # Output: ['chair', 'table', 'lamp', 'sofa']

# Remove an item from the cart
cart.remove("table")
print(cart)  # Output: ['chair', 'lamp', 'sofa']

# Pop the last item
last_item = cart.pop()
print(last_item)  # Output: sofa
print(cart)  # Output: ['chair', 'lamp']

"""
Breakdown:
  .append("sofa"): Adds "sofa" to the end of the list. Think of it like a user adding a product to their cart.
  .remove("table"): Removes the first occurrence of "table" from the list. It’s like a user removing an item from their cart.
  .pop(): Removes and returns the last item ("sofa"). You can store it in a variable (last_item) to use later. If you want to pop a specific index, use .pop(index), like .pop(0) to remove the first item.
  .Why?: This is how you’d let users add or remove products in a cart on your site.
"""
#---------------------------------------------

# Example 3: Working with Numbers in a List

# List of prices
prices = [300.99, 150.50, 75.25]

# Calculate total
total = sum(prices)
print(total)  # Output: 526.74

# Get the number of items
num_items = len(prices)
print(num_items)  # Output: 3

"""
Breakdown:
  prices = [300.99, 150.50, 75.25]: A list of floats (like product prices).
  sum(prices): Adds all numbers in the list.
  len(prices): Returns the number of items.
  Why?: Useful for calculating a cart total or counting items.
"""
#---------------------------------------------

# Example 4: What Happens with Errors?

# This will crash!
# print(cart[5])  # IndexError: list index out of range (cart only has 3 items now)

# This will crash!
# cart.remove("xyz")  # ValueError: list.remove(x): x not in list (xyz isn't in cart)

# Fix by checking first
if "xyz" in cart:
    cart.remove("xyz")
else:
    print("Item not in cart!")  # Output: Item not in cart!

"""
Breakdown:
  .cart[5]: Tries to access index 5, but cart only has items at indices 0, 1, and 2 (after modifications). This crashes with an IndexError.
  .cart.remove("xyz"): Tries to remove "xyz", which isn’t in the list, so it crashes with a ValueError.
  ."xyz" in cart: Checks if "xyz" is in the list before removing. If not, we print a message instead of crashing.
  .Why?: Errors like these happen in backend dev (e.g., a user tries to access an item that doesn’t exist). We’ll learn more about error handling later.
"""

#----------------------------------------

"""
Tips and Debugginghoe

  .Common Errors:
      .IndexError: Accessing an index that doesn’t exist (e.g., cart[5] when the list has 3 items).
        .Fix: Check the length with len(cart) and use valid indices (0 to len(cart) - 1).
      .ValueError: Removing an item that’s not in the list (e.g., cart.remove("xyz")).
        .Fix: Check if the item exists with if "xyz" in cart: before removing.
      .Forgetting brackets: cart = "chair", "table" crashes (fix: cart = ["chair", "table"]).
  .Debugging:
      .If you get an error, read the message—it’ll tell you the problem (e.g., IndexError: list index out of range).
      .Print the list at different steps to see how it changes (e.g., print(cart) after .append()).
      .If stuck, share your code or error with me, and I’ll help!
  .Keep It Fun:
      .Use products you like (e.g., Khamzat merch: ["Khamzat tee", "UFC gloves"]).
      .Imagine you’re building a cart feature for your e-commerce site.

"""

#----------------------------------------

# Day 2 Cheatsheet: Lists and Basic List Operations

# Lists:
  # Definition: Ordered, mutable collection of items.
  # Syntax: my_list = [item1, item2, item3]
  # Example: cart = ["chair", "table", "lamp"]

# Accessing Items:
  # Index: list[index] (starts at 0)
    # Example: cart[0] → "chair"
  # Slice: list[start:end]
    # Example: cart[1:3] → ["table", "lamp"]

# Modifying Lists:
  # Add: .append(item)
    # Example: cart.append("sofa")
  # Remove: .remove(item)
    # Example: cart.remove("table")
  # Pop: .pop(index) (default: last item)
    # Example: cart.pop() → removes and returns "sofa"

# Useful Functions:
  # Length: len(list)
    # Example: len(cart) → 3
  # Sum: sum(list) (for numbers)
    # Example: sum([1, 2, 3]) → 6

# Common Errors:
  # IndexError: Accessing invalid index (e.g., cart[5] when length is 3).
    # Fix: Check len(cart) and use valid indices.
  # ValueError: Removing item not in list (e.g., cart.remove("xyz")).
    # Fix: Check if item exists with if "xyz" in cart.

# Mini-Project Note:
  # Updated todo.py to use a list: todos = ["Work hard and buy BMW", "Order chair"].
  # Next: Add loops to print to-dos with numbers.