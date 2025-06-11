# Day 4: Loops and Conditionals**

# What Are Loops and Conditionals?**
    # - Loops** let you repeat code, like showing all items in your e-commerce cart or listing to-dos. The main types are `for` (for a set number of iterations) and `while` (until a condition fails).
    # - Conditionals** (`if`, `elif`, `else`) let you make decisions, like checking if a product is in stock or if a to-do is urgent.
    #- Why This Matters**: These are the backbone of dynamic websites—updating cart totals, filtering products, or prioritizing tasks in your CLI.

# Key Concepts**
    # - **For Loop**: Iterates over a sequence (e.g., list, dictionary keys).
        # - Example: `for item in cart: print(item)`
    # - **While Loop**: Runs while a condition is true.
        # - Example: `while stock > 0: print("In stock!")`
    # - *If Statement**: Executes code if a condition is true.
        # - Example: `if price < 500: print("Affordable!")`
    # - **Else and Elif**: Add alternatives or multiple conditions.
      #  - Example: `if price < 500: print("Cheap") else: print("Expensive")`
# Why This Matters**: For your site, loops can display all products, and conditionals can show “Out of Stock” alerts.


# -------------------------------------

# Example 1: For Loop with a List

cart = ["Ufc Gloves", "BMW", "Venum Uniform"]
for item in cart:
    print(f"Item: {item}")

# Output:
# Item: Ufc Gloves
# Item: BMW
# Item: Venum Uniform

# - **Breakdown**: Loops through each item in `cart` and prints it with an f-string.


# -------------------------------------

# Example 2: While Loop with a Counter

stock = 3
while stock > 0:
    print(f"Gloves left: {stock}")
    stock -= 1
# Output:
# Gloves left: 3
# Gloves left: 2
# Gloves left: 1

# - **Breakdown**: Runs until `stock` hits 0, decreasing by 1 each time.

# -------------------------------------

# Example 3: If-Else Conditional

price = 322.22
if price < 500:
    print("Affordable gear!")
else:
    print("Premium price!")
# Output: Affordable gear!

# - **Breakdown**: Checks the condition and prints accordingly.

# -------------------------------------

# Example 4: If-Elif-Else with Multiple Conditions

discount = 10
if discount > 20:
    print("Big sale!")
elif discount > 5:
    print("Small discount!")
else:
    print("No discount.")
# Output: Small discount!

# - **Breakdown**: Tests conditions in order, stops at the first true one.

# -------------------------------------

# Example 5: Combining Loops and Conditionals
cart = {"Ufc Gloves": 322.22, "BMW": 55000}
for item, price in cart.items():
    if price > 1000:
        print(f"{item} is expensive!")
    else:
        print(f"{item} is a deal!")
# Output:
# Ufc Gloves is a deal!
# BMW is expensive!

# - **Breakdown**: Loops through `cart` items and checks prices with an `if`.

# -------------------------------------

# Tips and Debugging**
  # - **Common Errors**:
      # - Infinite `while` loop: Forget to update the condition (e.g., `stock -= 1`). Fix: Ensure the loop ends.
      # - `IndentationError`: Misaligned code blocks. Fix: Use 4 spaces or a tab.
  # - **Debugging**: Print variables (e.g., `print(stock)`) to track changes.
  # - **Keep It Fun**: Add your UFC or car flair to the tasks!


# Day 4 Cheatsheet: Loops and Conditionals**

# For Loop:
    # - Syntax: `for item in sequence:`
    # - Example: `for item in ["a", "b"]: print(item)`

# While Loop:
    # - Syntax: `while condition:`
    # - Example: `while x < 3: print(x); x += 1`

# If Statement:
    # - Syntax: `if condition:`
    # - Example: `if x > 0: print("Positive")`

# Else and Elif:
    # - Syntax: `else:` or `elif condition:`
    # - Example: `if x > 0: print("Positive") else: print("Negative")`

# Combining:
    # - Example: `for x in range(5): if x % 2 == 0: print(f"{x} is even")`

# Mini-Project Note:
    # - Added numbered to-do list with priority check.
    # - Next: Add user input to add tasks.
