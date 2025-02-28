# main.py
from user import User
from manager import TaskManager

# Create a Task Manager
manager = TaskManager()

# Add users
user1 = User(1, "Alice")
user2 = User(2, "Bob")

manager.add_user(user1)
manager.add_user(user2)

# Create tasks and assign them to users
manager.create_task("Complete project report", 1)
manager.create_task("Prepare presentation slides", 2)
manager.create_task("Submit code review", 1)

# Display users and their tasks
manager.display_users()
manager.display_tasks()

# Users complete tasks
user1.complete_task(1)
user2.complete_task(2)

# Display updated task list
manager.display_users()
