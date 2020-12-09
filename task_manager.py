import task_queue
import pathlib

from task import Task
import humorous
import sys
import pickle

class TaskManager:
    """
    task manager with priority queue
    """
    
    def __init__(self):
        self.tasks = task_queue.TaskQueue()
        self.finished_tasks = []
        self.load_from_disk()
        
    def pickle_path(self):
        return pathlib.Path.home() / ".yatama.pickle"
        
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
    
    def add_task(self, task_desc):
        # do not allow procrastination of determining task priority.
        # if a task is added, then the user must determine its
        # priority immediately.
                
        print(f"adding task: {task_desc}")
        t = Task(task_desc) 
        self.tasks.insert(t)

    def remove_task(self, idx):
        return self.tasks.remove(idx)

    def get_task(self, idx):
        return self.tasks[idx]
    
    def show_all_tasks(self):
        for n, t in enumerate(self.tasks):
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
