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
        return "+"
    def run(self, task_mgr):
        print(" enter task description (enter nothing to skip)")
        task_desc = input(">> ").strip()
        if task_desc == "":
            pass
        else:
            task_mgr.add_task(task_desc)

#class EstimateDuration(CommandI)

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

class Commander:
    def __init__(self):
        self.commands = {}
        self.setup()

    def setup(self):
        cmdlist = [
            TaskAdd(),
            TaskAddRandom(),
            TaskList(),
        ]
        for cmd in cmdlist:
            self.commands[cmd.name()] = cmd

    def run(self, txt, task_mgr):
        txt=txt.strip()
        if txt in self.commands:
            self.commands[txt].run(task_mgr)
        else:
            raise UnknownCommand(f"Unknown command: {txt}")
