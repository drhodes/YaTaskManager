"""
docstring for mr. tasky mc'task face.
"""

import datetime

class Task:
    """A task is a unit of human work!"""
    _TASK_ID_ = 0
    
    def __init__(self, description):
        self.description = description
        self.created = datetime.datetime.now()
        self.subtasks = None # think about this.
        self.priority = 0
        self.setup()

    def setup(self):
        "manage the monotonically increasing task id"
        self.task_id = self._TASK_ID_
        self.task_id += 1

    def user_cmp(self, task):
        "the user compares these two tasks"
        print(f"1) {self}")
        print(f"1) {self}")
        print(f"2) {task}")

    def __repr__(self):
        return self.description
