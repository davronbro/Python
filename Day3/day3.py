# Day 3: Dictionaries

# What Are Dictionaries?

  # A dictionary is a collection of key-value pairs, like a product listing on your e-commerce site. It’s unordered (no fixed position like lists) but lets you look up values using keys.
  # Syntax: my_dict = {"key1": value1, "key2": value2}
  # Example: product = {"name": "Ufc Gloves", "price": 322.22}
  # Why This Matters: Dictionaries are perfect for storing structured data, like a product with a name and price, or a to-do with a task and category. In backend dev, you’ll use them to manage user data, product details, or API responses on your site.

# ---------------------------------------

# Key Dictionary Operations
# Here’s what you can do with dictionaries:


#  1. Accessing Values: Use the key to get the value.
#      product["name"] → "Ufc Gloves"
#      --> .get("key"): Safer way to access (returns None if the key doesn’t exist). Example: product.get("price") → 322.22

#  2. Adding/Updating Keys: Assign a value to a new or existing key.
#      product["stock"] = 10 --> adds or updates the "stock" key.

#  3. Methods:
#      --> .keys(): Get all keys. Example: product.keys() → dict_keys(['name', 'price'])
#      --> .values(): Get all values. Example: product.values() → dict_values(['Ufc Gloves', 322.22])
#      --> .items(): Get all key-value pairs. Example: product.items() → dict_items([('name', 'Ufc Gloves'), ('price', 322.22)])

#  4. Looping: Loop through keys, values, or pairs.
#      for key in product.keys(): --> loops through keys.
#      for value in product.values(): --> loops through values.
#      for key, value in product.items(): --> loops through pairs.

#Why This Matters: For your e-commerce site, dictionaries can store a cart item with name, price, and stock, or a to-do with task and priority.

# ---------------------------------------


# Example Code and Explanations
# Let’s write Python code to show dictionaries in action, using your UFC and car themes!

# Example 1: Creating and Accessing a Dictionary

# Create a dictionary (like a product on your site)
product = {"name": "Ufc Gloves", "price": 322.22, "stock": 10}

# Print the entire dictionary
print(product)  # Output: {'name': 'Ufc Gloves', 'price': 322.22, 'stock': 10}

# Access values by key
print(product["name"])  # Output: Ufc Gloves
print(product.get("price"))  # Output: 322.22

"""
  Breakdown:
    product = {"name": "Ufc Gloves", "price": 322.22, "stock": 10}: Creates a dictionary with 3 key-value pairs. Keys are strings (e.g., "name"), and values can be strings, numbers, etc.
    print(product): Shows the whole dictionary with curly braces {}.
    product["name"]: Gets the value for "name".
    product.get("price"): Safer access method—won’t crash if the key is missing (returns None instead).
    Why?: This is like storing product details on your site.
"""

# ---------------------------------------

# Example 2: Modifying a Dictionary

# Add a new key-value pair
product["category"] = "Sports Gear"
print(product)  # Output: {'name': 'Ufc Gloves', 'price': 322.22, 'stock': 10, 'category': 'Sports Gear'}

# Update an existing key
product["stock"] = 8
print(product)  # Output: {'name': 'Ufc Gloves', 'price': 322.22, 'stock': 8, 'category': 'Sports Gear'}

"""
  Breakdown:
    product["category"] = "Sports Gear": Adds a new key-value pair.
    product["stock"] = 8: Updates the value for an existing key.
    Why?: This is like adding a category to a product or updating stock after a sale.
"""

# ---------------------------------------

# Example 3: Looping Through a Dictionary

# Loop through keys
for key in product.keys():
    print(key)  # Output: name, price, stock, category (one per line)

# Loop through values
for value in product.values():
    print(value)  # Output: Ufc Gloves, 322.22, 8, Sports Gear (one per line)

# Loop through key-value pairs
for key, value in product.items():
    print(f"{key}: {value}")  # Output: name: Ufc Gloves, price: 322.22, stock: 8, category: Sports Gear

"""
  Breakdown:
  .keys(): Returns all keys as a view.
  .values(): Returns all values.
  .items(): Returns key-value pairs as tuples, which we unpack into key and value in the loop.
  f"{key}: {value}": Uses an f-string to format the output cleanly.
  Why?: Useful for displaying all product details or generating a report.
"""

# ---------------------------------------

# Example 4: Dictionary with a Cart

# A cart as a dictionary (item: quantity)
cart = {"Ufc Gloves": 2, "BMW": 1}

# Calculate total items
total_items = sum(cart.values())
print(total_items)  # Output: 3 (2 gloves + 1 BMW)

"""
  Breakdown:
  product["color"]: Crashes with a KeyError if "color" isn’t a key.
  product.get("color"): Returns None if the key is missing—safer.
  "color" in product: Checks if the key exists before accessing.
  Why?: Errors like this happen in backend dev (e.g., missing product data). We’ll dive deeper into error handling later.
"""

# ---------------------------------------

# Example 5: What Happens with Errors?

# This will crash!
# print(product["color"])  # KeyError: 'color' (key doesn't exist)

# Fix with .get()
color = product.get("color")
print(color)  # Output: None (safe, no crash)

# Check before accessing
if "color" in product:
    print(product["color"])
else:
    print("Key not found!")  # Output: Key not found!

"""
  Breakdown:
    product["color"]: Crashes with a KeyError if "color" isn’t a key.
    product.get("color"): Returns None if the key is missing—safer.
    "color" in product: Checks if the key exists before accessing.
    Why?: Errors like this happen in backend dev (e.g., missing product data). We’ll dive deeper into error handling later.
"""

# ---------------------------------------

# Tips and Debugging

  # Common Errors:
    # KeyError: Accessing a missing key (e.g., product["color"]). Fix: Use .get("color") or check with if "color" in product.
    # TypeError: Using a list as a key (e.g., {"[1, 2]": 3}). Fix: Keys must be immutable (use strings or numbers).
  # Debugging:
    # If you get an error, read the message (e.g., KeyError: 'color').
    # Print the dictionary at each step (e.g., print(product) after updates).
    # Ask me if you’re stuck!
  # Keep It Fun:
    # Use your UFC or car themes (e.g., {"name": "Khamzat Tee", "price": 50}).
    # Imagine managing a store inventory or to-do list.

# ---------------------------------------

# Day 3 Cheatsheet: Dictionaries

  # Dictionaries:
    # Definition: Collection of key-value pairs.
    # Syntax: my_dict = {"key1": value1, "key2": value2}
    # Example: product = {"name": "Ufc Gloves", "price": 322.22}

  # Accessing Values:
    # By key: dict["key"]
      # .Example: product["name"] → "Ufc Gloves"
    # Safer: .get("key")
      # .Example: product.get("price") → 322.22

  # Modifying Dictionaries:
    # Add/Update: dict["key"] = value
      # Example: product["stock"] = 10

  # Methods:
    # Keys: .keys()
      # Example: product.keys() → dict_keys(['name', 'price'])
    # Values: .values()
      # Example: product.values() → dict_values(['Ufc Gloves', 322.22])
    # Items: .items()
      # Example: product.items() → dict_items([('name', 'Ufc Gloves'), ('price', 322.22)])

  # Looping:
    # Keys: for key in dict.keys():
    # Values: for value in dict.values():
    # Pairs: for key, value in dict.items():

  # Common Errors:
    # KeyError: Accessing missing key. Fix: Use .get() or check if "key" in dict.
    # TypeError: Unhashable key type. Fix: Use immutable keys (strings, numbers).
    
  # Mini-Project Note:
    # Updated todo2.py to use a list of dictionaries: [{"task": "...", "category": "..."}].
    # Next: Add loops to print to-dos with numbers.