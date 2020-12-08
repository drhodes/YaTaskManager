"""
Commander

intepret user input as modular commands.

"""

import lorem
import task
from err import *

class CommandI:
    def name(self): raise Exception("Unimplemented")
    def run(self): raise Exception("Unimplemented")

class TaskAdd(CommandI):
    def name(self):
        return "add"
    def run(self, task_mgr):
        print(" enter task description (enter nothing to skip)")
        task_desc = input(">> ").strip()
        if task_desc == "":
            pass
        else:
            task_mgr.add_task(task_desc)

class EstimateDuration(CommandI):
    def name(self):
        return "est"
    def run(self, task_mgr):
        print(" To estimate the duration of a task, enter its task number:")
        task_number = input(">> ").strip()
        print(" What is your estimate for task duration?")
        print(" formatting is 10m for 10 minutes, 3h for 3 hours, 4d for 4 day, 5w, 6m, 7y...")
        duration = input(">> ").strip()
        
        try:
            task_number = int(task_number)
        except Exception as e:
            print(f"Sorry, couldn't handle task_number: {e}")
            
        task_mgr.set_duration(task_number, duration)

class TaskList(CommandI):
    def name(self):
        return "ls"
    def run(self, task_mgr):
        task_mgr.show_all_tasks()
    
class TaskAddRandom(CommandI):
    def name(self):
        return "add random tasks"

    def run(self, task_mgr):
        print("how many random tasks to add?")
        num_tasks = input(">> ")
        for _ in range(int(num_tasks)):
            task_mgr.add_task(lorem.sentence())

class RemoveTask(CommandI):
    def name(self):
        return "rm"

    def run(self, task_mgr):
        print("which task to remove? (enter task number)?")
        task_num = input(">> ")
        try:
            task_num = int(task_num)
        except ValueError as e:
            print(f"Sorry, couldn't parse task_number: {e}")            
            print("task not removed")
        print(f"removing task: {task_num}")
        task_mgr.remove_task(task_num)


        
        
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
        ]
        for cmd in cmdlist:
            self.commands[cmd.name()] = cmd

    def run(self, txt, task_mgr):
        txt=txt.strip()
        if txt in self.commands:
            self.commands[txt].run(task_mgr)
        else:
            raise UnknownCommand(f"Unknown command: {txt}")
