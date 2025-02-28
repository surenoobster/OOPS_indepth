# task.py
class Task:
    """Represents a single task in the system."""

    def __init__(self, task_id: int, description: str):
        self.task_id = task_id
        self.description = description
        self.is_completed = False

    def complete(self):
        """Marks the task as completed."""
        self.is_completed = True

    def __str__(self):
        """Returns task details as a string."""
        return f"Task {self.task_id}: {self.description} - {'Completed' if self.is_completed else 'Pending'}"
