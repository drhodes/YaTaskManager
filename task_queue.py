
class TaskQueue:
    def __init__(self):
        self.tasks = []

    def insert_task_helper(self, task, idxL, idxR):
        if idxL == idxR:
            self.tasks.insert(idxL, task)
        else:
            idxM = idxL + (idxR - idxL) // 2
            midTask = self.tasks[idxM]
            if task.has_priority_over(midTask):
                # insert to the left, as the highest priorities are at the front.
                self.insert_task_helper(task, idxL, idxM)
            else:
                self.insert_task_helper(task, idxM+1, idxR)
    
    def insert(self, task):
        if len(self.tasks) == 0:
            self.tasks.append(task)
        else:
            self.insert_task_helper(task, 0, len(self.tasks))
            
    def __iter__(self):
        return iter(self.tasks)
