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
        self.tags = set()
        # self.priority = 0
        self.setup()

    def set_duration(self, dur):
        self.duration = dur

    def add_tag(self, tag):
        self.tags.add(tag)
        
    def setup(self):
        "manage the monotonically increasing task id"
        self.task_id = self._TASK_ID_
        self.task_id += 1
        
    def has_priority_over(self, task):
        print(f"Do ({str(self)}) before ({str(task)})? ([y]/n)")
        response = input(">> ").strip().lower()
        return response in ["y", "yes", ""]
        
    def __repr__(self):
        s = self.description
        if self.duration != None:
            s += f"({self.duration})"
        if self.tags:
            s += "  [" + " ".join(self.tags) + "]"
        return s
