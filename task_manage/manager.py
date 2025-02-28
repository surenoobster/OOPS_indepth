 # manager.py
from user import User
from task import Task

class TaskManager:
    """Manages users and their tasks."""

    def __init__(self):
        self.users = []
        self.tasks = []
        self.next_task_id = 1  # Auto-increment task ID

    def add_user(self, user: User):
        """Adds a user to the system."""
        self.users.append(user)

    def create_task(self, description: str, user_id: int):
        """Creates a new task and assigns it to a user."""
        task = Task(self.next_task_id, description)
        self.tasks.append(task)
        self.next_task_id += 1

        user = self.find_user(user_id)
        if user:
            user.add_task(task)
            print(f"Task '{description}' assigned to {user.name}.")
        else:
            print("User not found!")

    def find_user(self, user_id: int):
        """Finds a user by ID."""
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def display_users(self):
        """Displays all users and their tasks."""
        print("\nAll Users:")
        for user in self.users:
            print(user)

    def display_tasks(self):
        """Displays all tasks."""
        print("\nAll Tasks:")
        for task in self.tasks:
            print(task)
