todos = [{"task": "Work Hard and Buy BMW", "category": "Goal"}, {"task": "Get ticket to fly Dubai", "category": "Travel"}]
print(todos)

todos[0]["priority"] = "High"
print(todos)
print(todos[0])
print(todos[0]["category"])
print(todos[0].get("task"))
print(todos[0].get("price", todos[0]["priority"]))
print(todos[1].get("price", "Not Available"))
print(todos[0].get("price", todos[1]))
print(todos[0].get("price", todos[1]["category"]))
print(f"Your first {todos[0]["category"]} is to {todos[0]["task"]} after that {todos[1]["category"]}")


todos[0]["category"] = "Great Goal"
print(todos)


todos[1]["book"] = "5 star Hotel"
print(todos)
print(todos[1])
print(todos[1]["book"])
print(todos[1].get("task"))
print(todos[1].get("color", todos[1]["category"]))
print(todos[1].get("color", "Not Available"))
print(todos[1].get("color", todos[0]["category"]))
print(f"Your second {todos[0]["category"]} is to {todos[1]["task"]} and book {todos[1]["book"]}")

todos[1]["category"] = "Amazing travel"
print(todos)

for key in todos[0].keys():
  print(key)
for value in todos[0].values():
  print(value)
for key in todos[1].keys():
  print(key)
for value in todos[1].values():
  print(value)
for key, value in todos[0].items():
  print(f"{key}: {value}") 
for key, value in todos[1].items():
  print(f"{key}: {value}") 


#----------------------------


todos_int = [{"Work Hard and Buy BMW": 1, "Get ticket to fly Dubai": 2 }, {"Travel days": 10, "Buy gifts": 15 }]
print(todos_int)

total_itmes1 = sum(todos_int[0].values())
total_itmes2 = sum(todos_int[1].values())

overall = total_itmes1 + total_itmes2
print(overall)

todos_int[0]["Work Hard and Buy BMW"] = 5
todos_int[0]["Get ticket to fly Dubai"] = 10
todos_int[1]["Travel days"] = 20
todos_int[1]["Buy gifts"] = 30

for key in todos_int[0].keys():
  print(key)
for value in todos_int[0].values():
  print(value)
for key in todos_int[1].keys():
  print(key)
for value in todos_int[1].values():
  print(value)
for key, value in todos_int[0].items():
  print(f"{key}: {value}") 
for key, value in todos_int[1].items():
  print(f"{key}: {value}") 
