import task_queue
import pathlib
import err

from task import Task
import humorous
import sys, os
import pickle

class TaskManager:
    """
    task manager with priority queue
    """
    
    def __init__(self):
        self.tasks = task_queue.TaskQueue()
        self.finished_tasks = []
        self.load_from_disk()
        self.lock = None
        
    def pickle_path(self):
        return pathlib.Path.home() / ".yatama.pickle"

    def lockfile_path(self):
        return pathlib.Path.home() / ".yatama.pickle.lock"
    
    def to_csv(self):
        lines = []
        for t in self.tasks:
            lines.append(", ".join(t.to_csv()))
        return lines
    
    def load_from_disk(self):
        try:
            self.tasks, self.finished_tasks = pickle.load(open(self.pickle_path(),'rb'))
        except FileNotFoundError as e:
            pass # ok, first run.
        
    def save_to_disk(self):
        obj = (self.tasks, self.finished_tasks)
        pickle.dump(obj, open(self.pickle_path(), 'wb'))

    def run(self, cmd):
        print(f"TaskManager is doing {cmd}")
        return True
    
    def add_task(self, description):
        # do not allow procrastination of determining task priority.
        # if a task is added, then the user must determine its
        # priority immediately.
        print(f"adding task: {description}")
        t = Task(description)
        self.tasks.insert(t)

    # def add_deadline_property(self):
    #     for t in self.tasks:
    #         t.add_deadline_property()
    #     for t in self.finished_tasks:
    #         t.add_deadline_property()
        
    def set_task_description(self, task_num, new_desc):
        self.tasks[task_num].set_description(new_desc)

    def set_task_deadline(self, task_num, date):
        task = self.tasks[task_num]
        self.tasks[task_num].set_deadline(date)
        
    def add_full_task(self, task):
        self.tasks.insert(task)
        
    def swap(self, idx1, idx2):
        self.tasks[idx1], self.tasks[idx2] = self.tasks[idx2], self.tasks[idx1]
        
    def remove_task(self, idx):
        return self.tasks.remove(idx)
    
    def remove_finished_task(self, idx):
        return self.finished_tasks.pop(idx)

    def get_task(self, idx):
        return self.tasks[idx]
    
    def show_all_tasks(self):
        for n, t in enumerate(self.tasks):
            print(f"({n}):  {t}")

    def show_all_finished_tasks(self):
        for n, t in enumerate(self.finished_tasks):
            print(f"({n}):  {t}")
            
    def list_tasks_with_tag(self, tag):
        for n, t in enumerate(self.tasks):
            if tag in t.tags:
                print(f"({n}):  {t}")
            
    def finish_task(self, idx):
        task = self.remove_task(idx)
        self.finished_tasks.append(task)
        self.show_finished_tasks()
        
    def show_finished_tasks(self):
        print("---------------------------------")
        print("FINISHED TASKS")
        for n, t in enumerate(self.finished_tasks):
            print(f"({n}):  {t}")

    def set_duration(self, idx, duration):
        try:
            self.tasks[idx].set_duration(duration)
        except IndexError:
            print(f"there is no task with that number: {idx}")        
            
    def quit(self):
        print("todo: cleanup")
        self.save_to_disk()
        humorous.parting_message()
        sys.exit(0)
