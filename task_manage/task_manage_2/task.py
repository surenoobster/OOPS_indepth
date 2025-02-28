 

from datetime import datetime

class Task:
    """Represents a task in the system."""

    task_list = []  # Class-level list to store all tasks

    def __init__(self, title, description, due_date, assigned_to):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.assigned_to = assigned_to
        self.completed = False

    def mark_completed(self):
        """Marks the task as completed."""
        self.completed = True

    @classmethod
    def create_task(cls, title, description, due_date, assigned_to):
        """Creates and stores a task."""
        task = cls(title, description, due_date, assigned_to)
        cls.task_list.append(task)
        return task

    @classmethod
    def get_all_tasks(cls):
        """Returns all tasks."""
        return cls.task_list
