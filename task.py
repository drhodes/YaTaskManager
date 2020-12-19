"""
docstring
"""
import datetime
import json

class Task():
    """A task is a unit of human work!"""

    def __init__(self, description):
        # should tasks have a lifetime? 
        assert type(description) == str
        self.description = description
        self.created = datetime.datetime.now()
        self.subtasks = None # think about this.
        self.duration = None #
        self.deadline = None
        self.tags = set()

    def add_deadline_property(self):
        self.deadline = None

    def set_duration(self, dur):
        self.duration = dur

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
        
    def set_deadline(self, date):
        # change these prints to calls to a logger.
        print(f"setting deadline of task:'{self}' to {date}")
        self.deadline = date

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

    def to_json(self):
        return json.dumps(self)
    
    def __repr__(self):
        s = ""
        if len(self.description) > 45:
            s = self.description[:45] + "…"
        else:
            s = self.description            
        if self.duration:
            s += f"({self.duration})"
        if self.deadline:
            s += f" (due* {self.deadline})"
        if self.tags:
            s += "  [" + " ".join(self.tags) + "]"
        return s
