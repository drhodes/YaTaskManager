import task_queue
from task import Task

class TaskManager:
    """
    task manager with priority queue
    """
    
    def __init__(self):
        self.tasks = task_queue.TaskQueue()
        
    def load_from_disk(self):
        pass
        
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
        self.tasks.remove(idx)
        
    def show_all_tasks(self):
        for n, t in enumerate(self.tasks):
            print(f"({n}):  {t}")

    def set_duration(self, idx, duration):
        try:
            self.tasks[idx].set_duration(duration)
        except IndexError:
            print(f"there is no task with that number: {idx}")        
            
