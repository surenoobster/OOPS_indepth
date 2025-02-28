 # user.py
from task import Task

class User:
    """Represents a user who manages tasks."""

    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name
        self.tasks = []  # List of assigned tasks

    def add_task(self, task: Task):
        """Assigns a task to the user."""
        self.tasks.append(task)

    def complete_task(self, task_id: int):
        """Marks a task as completed."""
        for task in self.tasks:
            if task.task_id == task_id:
                task.complete()
                print(f"{self.name} completed task {task_id}.")
                return
        print(f"Task {task_id} not found.")

    def __str__(self):
        """Returns user details."""
        task_list = "\n  ".join([str(task) for task in self.tasks]) or "No tasks assigned."
        return f"User: {self.name} (ID: {self.user_id})\nTasks:\n  {task_list}"
