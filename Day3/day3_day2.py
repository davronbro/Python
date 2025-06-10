

### **Question 1: Curly Braces `{}` vs. Square Brackets `[]`**
#  You noticed I used `products = {"name": "BMW", "price": 55000, "discount": 5}` with curly braces in Day 3, but we used `cart = ["chair", "table", "lamp"]` with square brackets in Day 2. What’s the difference?

  # Square Brackets `[]` (Lists)**:
      # - Used to create a **list**, which is an ordered collection of items.
      # - Example: `cart = ["chair", "table", "lamp"]` stores items in a sequence (index 0, 1, 2).
      # - You access items by index (e.g., `cart[0]` → `"chair"`) and can modify them (e.g., `.append()`, `.remove()`).
      # - Great for a simple list of things like a shopping cart or to-dos.


  # Curly Braces `{}` (Dictionaries)**:
      # - Used to create a **dictionary**, which is an unordered collection of **key-value pairs**.
      # - Example: `products = {"name": "BMW", "price": 55000, "discount": 5}` stores data as pairs (key: `"name"`, value: `"BMW"`).
      # - You access values by key (e.g., `products["name"]` → `"BMW"`) and can add/update pairs (e.g., `products["stock"] = 10`).
      # - Perfect for structured data like product details or to-do categories.


  # Key Difference**:
      # - Lists use indices (numbers) to access items; dictionaries use keys (usually strings) to access values.
      # - Lists are for sequences; dictionaries are for mappings (key to value).
      # - In Day 2, we focused on lists for basic collections. In Day 3, we’re stepping up to dictionaries for more complex data.

  # Why Here?**: The `products` dictionary lets you store a product’s name, price, and discount together, which is more organized than a list like `["BMW", 55000, 5]` where you’d have to remember the order (index 0 = name, index 1 = price, etc.).

#------------------------------------------


### Question 2: What’s `print(f"{key}: {value}")`?**
  # You saw this in the loop `for key, value in products.items(): print(f"{key}: {value}")`—let’s unpack it!

  # What It Does**:
      # - products.items(): Returns a view of the dictionary’s key-value pairs as tuples (e.g., `("name", "BMW")`, `("price", 55000)`).
      # - for key, value in products.items(): Loops through each pair, unpacking the tuple into `key` and `value` variables. For `{"name": "BMW", "price": 55000}`, the first loop sets `key = "name"`, `value = "BMW"`, then `key = "price"`, `value = 55000`.
      # - print(f"{key}: {value}"): Prints each pair in the format `"key: value"`. The `f` before the string makes it an **f-string**, a modern Python way to embed variables inside `{}`. So, it outputs `"name: BMW"` and `"price: 55000"`.

  # Breakdown of `f"{key}: {value}"`**:
      # - f"...": Tells Python it’s an f-string, so it evaluates expressions in `{}`.
      # - {key}: Inserts the value of `key` (e.g., `"name"`).
      # - : A literal colon separator.
      # - {value}: Inserts the value of `value` (e.g., `"BMW"`).
      # - Result: Combines them into a neat string like `"name: BMW"`.

    # Why Use It?**: It’s a clean way to format output. Without f-strings, you’d write `print(key + ": " + str(value))`, which works but is less readable. F-strings are faster and more intuitive.

  # Example Output** (for -> products = {"name": "BMW", "price": 55000} <- ):
"""
  name: BMW
  price: 55000

"""

#------------------------------------------


### Question 3: Curly Braces in `todos = [{"task": "Work Hard and Buy BMW", "category": "Goal"}, {"task": "Get ticket to fly Dubai", "category": "Travel"}]`**
  # You’re spot on noticing curly braces inside square brackets—let’s dive in!

  # What’s Happening?**:
      # - `todos` is a **list** (square brackets `[]`) containing multiple **dictionaries** (curly braces `{}`).
      # - Each dictionary inside the list represents one to-do, with keys like `"task"` and `"category"`, and their values.
      # - Example: `[{"task": "Work Hard and Buy BMW", "category": "Goal"}, {"task": "Get ticket to fly Dubai", "category": "Travel"}]`
      # - First dictionary: `{"task": "Work Hard and Buy BMW", "category": "Goal"}`
      # - Second dictionary: `{"task": "Get ticket to fly Dubai", "category": "Travel"}`

#--------------

### Is It a List?: Yes! The outer `[]` makes `todos` a list. The inner `{}` are dictionaries inside that list. This is called a **list of dictionaries**—a common way to store multiple related items with structured data.

  # Can You Get Values and Names?**:
      # - Yes! Since it’s a list, use an index to access a dictionary, then a key to get a value.
      # - Example: `todos[0]` gives the first dictionary `{"task": "Work Hard and Buy BMW", "category": "Goal"}`.
      # - Then, `todos[0]["task"]` gives `"Work Hard and Buy BMW"`, and `todos[0]["category"]` gives `"Goal"`.
      # - For the second item: `todos[1]["task"]` → `"Get ticket to fly Dubai"`, `todos[1]["category"]` → `"Travel"`.

  # Can You Add a Category?**:
      # - Yes! You can add a new key-value pair to any dictionary in the list.
      # - Example: To add a `"priority"` to the first to-do:

"""
  todos[0]["priority"] = "High"
  print(todos[0])  # Output: {'task': 'Work Hard and Buy BMW', 'category': 'Goal', 'priority': 'High'}

"""  
  # - This modifies the existing dictionary at index 0. You can do this for any item in the list (e.g., `todos[1]["priority"] = "Medium"`).
  # Why Use This?**: A list of dictionaries lets you store multiple to-dos, each with its own details (task, category, priority, etc.). It’s more powerful than a simple list of strings like in Day 2.

# Example:

"""
    todos = [{"task": "Work Hard and Buy BMW", "category": "Goal"}, {"task": "Get ticket to fly Dubai", "category": "Travel"}]
    print(todos[0]["task"])  # Output: Work Hard and Buy BMW
    todos[1]["priority"] = "Medium"
    print(todos[1])  # Output: {'task': 'Get ticket to fly Dubai', 'category': 'Travel', 'priority': 'Medium'}
"""

### Quick Recap
    # - `{}` vs. `[]`**: Dictionaries (`{}`) store key-value pairs; lists (`[]`) store ordered items. Day 3 uses dictionaries for structured data, Day 2 used lists for sequences.
    # - `f"{key}: {value}"`**: An f-string to format key-value pairs in a loop—clean and modern.
    # - List of Dictionaries**: `todos` is a list (`[]`) of dictionaries (`{}`), letting you access values with indices and keys, and add new key-value pairs.
