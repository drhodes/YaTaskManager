"""
Commander

intepret user input as modular commands.
"""
import lorem
from err import *

class CommandI:
    def name(self): raise Exception("Unimplemented")
    def desc(self): raise Exception(self.__class__.__name__ + " needs to implement method desc()")
    def run(self): raise Exception("Unimplemented")    

# ----------------------------------------------------------------------------------------
def get_task_number():
    print("enter task number")
    task_num = input(">> ")
    try:
        task_num = int(task_num)
    except ValueError as e:
        print(f"Sorry, couldn't parse task_number: {e}")
        raise e
    return task_num


class TaskAdd(CommandI):
    def name(self): return "add"
    def desc(self): return "add a task to the queue"
    
    def run(self, task_mgr):
        print(" enter task description (enter nothing to skip)")
        task_desc = input(">> ").strip()
        if task_desc == "":
            pass
        else:
            task_mgr.add_task(task_desc)

class EstimateDuration(CommandI):
    def name(self): return "est"
    def desc(self): return "estimate the duration of a task"

    def run(self, task_mgr):
        print(self.desc())
        try:
            task_number = get_task_number()
            print(" What is your estimate for task duration?")
            print(" formatting is 10m for 10 minutes, 3h for 3 hours, 4d for 4 day, 5w, 6m, 7y...")
            duration = input(">> ").strip()
            task_mgr.set_duration(task_number, duration)
        except ValueError as e:
            print(f"could not set the estimate duration")

class TaskList(CommandI):
    def name(self): return "ls"
    def desc(self): return "list all tasks"
    
    def run(self, task_mgr):
        task_mgr.show_all_tasks()
    
class TaskAddRandom(CommandI):
    def name(self): return "add random tasks"
    def desc(self): return "a command for testing this program, safe to ignore"

    def run(self, task_mgr):
        print("how many random tasks to add?")
        num_tasks = input(">> ")
        for _ in range(int(num_tasks)):
            task_mgr.add_task(lorem.sentence())

class RemoveTask(CommandI):
    def name(self): return "rm"
    def desc(self): return "remove a task from the queue"
    
    def run(self, task_mgr):
        print(self.desc())
        try:
            task_num = get_task_number()
            print(f"removing task: {task_num}")
            task_mgr.remove_task(task_num)
        except ValueError as e:
            print(f"Sorry, couldn't parse task_number: {e}")            
            print("task not removed")

class Quit(CommandI):
    def name(self): return "q"
    def desc(self): return "quit yatama"

    def run(self, task_mgr):
        task_mgr.quit()

        
class FinishTask(CommandI):
    def name(self): return "fin"
    def desc(self): return "finish a task an remove it from the queue"

    def run(self, task_mgr):
        task_num = get_task_number()
        print(f"finishing task: {task_num}")
        task_mgr.finish_task(task_num)

class ReprioritizeTask(CommandI):
    def name(self): return "rt"
    def desc(self): return "change the priority of a task"
    
    def run(self, task_mgr):
        task_num = get_task_number()
        task = task_mgr.remove_task(task_num)
        task_mgr.add_task(task.description)

class TagTask(CommandI):
    def name(self): return "tag"
    def desc(self): return "add a tag to a task"

    
    def run(self, task_mgr):
        task_num = get_task_number()
        task = task_mgr.get_task(task_num)

        print(f"enter the tag for {task}")
        tag = input(">> ").strip()
        task.add_tag(tag)


# ----------------------------------------------------------------------------------------

class Commander:
    def __init__(self):
        self.commands = {}
        self.setup()

    def setup(self):
        cmdlist = [
            TaskAdd(),
            TaskAddRandom(),
            TaskList(),
            EstimateDuration(),
            RemoveTask(),
            Quit(),
            FinishTask(),
            ReprioritizeTask(),
            TagTask(),
        ]
        for cmd in cmdlist:
            self.commands[cmd.name()] = cmd

    def run(self, txt, task_mgr):
        txt=txt.strip()
        if txt in ["h", "?"]:
            self.show_help()
        elif txt in self.commands:
            self.commands[txt].run(task_mgr)
        else:
            raise UnknownCommand(f"Unknown command: {txt}")

    def show_help(self):
        print("available commands: ")
        print("--")
        for name, cmd in self.commands.items():
            print(f" {name:<20} {cmd.desc()}")
