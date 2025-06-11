todos = [{"task": "Work Hard and Buy BMW", "category": "Great Goal", "priority": "High"}, 
         {"task": "Get ticket to fly Dubai", "category": "Amazing travel", "book": "5 star Hotel",}]

# Numbered to-do list with priority check
for index, todo in enumerate(todos, start=1):
    priority_text = " (URGENT)" if "priority" in todo and todo["priority"] == "High" else ""
    print(f"{index}. {todo['task']} ({todo['category']}){priority_text}")


# todos = [{"task": "Work Hard and Buy BMW", "category": "Great Goal", "priority": "High"}, 
#          {"task": "Get ticket to fly Dubai", "category": "Amazing travel", "book": "5 star Hotel", "priority": "Small"}]

# # Numbered to-do list with priority check
# for index, todo in enumerate(todos, start=1):
#     priority_text = f" (Priority: {todo.get('priority', 'N/A')})" if "priority" in todo else ""
#     print(f"{index}. {todo['task']} ({todo['category']}){priority_text}")
