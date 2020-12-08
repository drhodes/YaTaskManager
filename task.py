"""
docstring
"""

import datetime

class Task:
    """A task is a unit of human work!"""
    _TASK_ID_ = 0
    
    def __init__(self, description):
        # should tasks have a lifetime?
        assert(type(description) == str)
        self.description = description
        self.created = datetime.datetime.now()
        self.subtasks = None # think about this.
        self.duration = None # 
        # self.priority = 0
        self.setup()

    def setup(self):
        "manage the monotonically increasing task id"
        self.task_id = self._TASK_ID_
        self.task_id += 1
        
    def has_priority_over(self, task):
        print(f"1) {str(self)}")
        print(f"2) {str(task)}")
        print("Does task 1 have priority over task 2?")
        response = input(">> ").strip().lower()
        return response in ["y", "yes", ""]
        
    def __repr__(self):
        return self.description
