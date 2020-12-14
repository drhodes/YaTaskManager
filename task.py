"""
docstring
"""

import datetime

class Task:
    """A task is a unit of human work!"""
    
    def __init__(self, description):
        # should tasks have a lifetime?
        assert(type(description) == str)
        self.description = description
        self.created = datetime.datetime.now()
        self.subtasks = None # think about this.
        self.duration = None #
        self.tags = set()

    def set_duration(self, dur):
        self.duration = dur

    def set_description(self, desc):
        self.description = desc
        
    def add_tag(self, tag):
        self.tags.add(tag)

    def has_priority_over(self, task):
        print(f"Do ({str(self)}) before ({str(task)})? ([y]/n)")
        response = input(">> ").strip().lower()
        return response in ["y", "yes", ""]

    def to_csv(self):
        return (str(self.description),
                str(int(self.created.timestamp())),
                str(self.duration),
                "/".join(self.tags))

    def __repr__(self):
        s = self.description
        if self.duration != None:
            s += f"({self.duration})"
        if self.tags:
            s += "  [" + " ".join(self.tags) + "]"
        return s
