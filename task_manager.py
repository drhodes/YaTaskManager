
class TaskManager:
    """
    task manager with priority queue
    """
    def __init__(self):
        self.tasks = [] # this will be a taskheap
        
    def run(self, cmd):
        print(f"TaskManager is doing {cmd}")
        return True
    
    def add_task(self, task):
        # do not allow procrastination of determining task priority.
        # if a task is added, then the user must determine its
        # priority immediately.
                
        print(f"adding task: {task}")
        self.tasks.append(task)
        
    def show_all_tasks(self):
        for n, t in enumerate(self.tasks):
            print(f"({n}):  {t}")
