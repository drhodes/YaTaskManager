"""
Commander

intepret user input as modular commands.
"""
import lorem
import tk_cal
from err import unimplemented, UnknownCommand

class CommandI:
    def name(self):
        """the name of the command"""
        unimplemented(self)
        
    def desc(self):
        """a description of the command"""
        unimplemented(self)
        
    def run(self):
        """run the command on the task manager"""
        unimplemented(self)
    
# ------------------------------------------------------------------
def get_input():
    return input(f">> ").strip()

def ask(msg):
    print(" ", msg)
    return get_input()

def get_task_number():
    task_num = ask("enter task number")
    try:
        task_num = int(task_num)
    except ValueError as e:
        print(f"Sorry, couldn't parse task_number: {e}")
        raise e
    return task_num

# ------------------------------------------------------------------
# These are the commands available to users. 

class TaskAdd(CommandI):
    def name(self): return "add"
    def desc(self): return "add a task to the queue"

    def run(self, task_mgr):
        task_desc = ask("enter task description (enter nothing to skip)")
        if task_desc:
            task_mgr.add_task(task_desc)
            
class EstimateDuration(CommandI):
    def name(self): return "est"
    def desc(self): return "estimate the duration of a task"

    def run(self, task_mgr):
        print(self.desc())
        try:
            task_number = get_task_number()
            print(" What is your estimate for task duration?")            
            duration = ask(" formatting is 10m for 10 minutes, 3h, 4d, 5w, 6m, 7y...")
            task_mgr.set_duration(task_number, duration)
        except ValueError as e:
            print(f"could not set the estimate duration")

class AddDeadline(CommandI):
    def name(self): return "dl"
    def desc(self): return "set a deadline for a task"

    def run(self, task_mgr):
        try:
            task_number = get_task_number()
            date = tk_cal.get_date()
            if date:
                task_mgr.set_task_deadline(task_number, date)
            else:
                print(f"Date not found, got: {date} instead")
        except ValueError as e:
            print(f"Couldn't set a deadline: {e}")
            
class TaskList(CommandI):
    def name(self): return "ls"
    def desc(self): return "list all tasks"

    def run(self, task_mgr):
        task_mgr.show_all_tasks()

class TaskAddRandom(CommandI):
    def name(self): return "add random tasks"
    def desc(self): return "a command for testing this program, safe to ignore"

    def run(self, task_mgr):
        num_tasks = ask("how many random tasks to add?")
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

class RenameTask(CommandI):
    def name(self): return "rename"
    def desc(self): return "change the description of a task"

    def run(self, task_mgr):
        try:
            task_num = get_task_number()
            new_desc = ask("enter the new description")
            task_mgr.set_task_description(task_num, new_desc)
        except ValueError as e:
            print(f"Sorry, couldn't parse task_number: {e}")
            print("task not renamed")
            
class Quit(CommandI):
    def name(self): return "q"
    def desc(self): return "quit yatama"

    def run(self, task_mgr):
        task_mgr.quit()

class ListTag(CommandI):
    def name(self): return "lst"
    def desc(self): return "list tasks with a given tag"

    def run(self, task_mgr):
        try:
            tag = ask("enter tag")
            task_mgr.list_tasks_with_tag(tag)
        except ValueError as e:
            print(f"Couldn't list tasks with tag because: {e}")            
        
class FinishTask(CommandI):
    def name(self): return "fin"
    def desc(self): return "finish a task an remove it from the queue"

    def run(self, task_mgr):
        try:
            task_num = get_task_number()
            print(f"finishing task: {task_num}")
            task_mgr.finish_task(task_num)
        except ValueError as e:
            print(f"Couldn't finish task because: {e}")            

class ReprioritizeTask(CommandI):
    def name(self): return "ch"
    def desc(self): return "change the priority of a task"

    def run(self, task_mgr):
        task_num = get_task_number()
        task = task_mgr.remove_task(task_num)
        task_mgr.add_task(task.description)

class ListFinishedTasks(CommandI):
    def name(self): return "lsf"
    def desc(self): return "list finished tasks"
    def run(self, task_mgr):
        task_mgr.show_all_finished_tasks()
        
class Ressurect(CommandI):
    def name(self): return "res"
    def desc(self): return "resurrect a task and put it back on the queue"

    def run(self, task_mgr):
        task_mgr.show_all_finished_tasks()
        task_num = get_task_number()
        task = task_mgr.remove_finished_task(task_num)
        task_mgr.add_full_task(task)
        
class TagTask(CommandI):
    def name(self): return "tag"
    def desc(self): return "add a tag to a task"

    def run(self, task_mgr):
        task_num = get_task_number()
        task = task_mgr.get_task(task_num)
        tag = ask(f"enter the tag for '{task}'")
        if tag: task.add_tag(tag)

class RemoveTag(CommandI):
    def name(self): return "rmt"
    def desc(self): return "remove a tag from a task"

    def run(self, task_mgr):
        try:
            task_num = get_task_number()
            tag = ask("enter a tag to remove")
            task_mgr.remove_task_tag(task_num, tag)
        except ValueError as e:
            print("couldn't remove tag:{tag}, because {e}")
            
        
class ToCSV(CommandI):
    def name(self): return "csv"
    def desc(self): return "output tasks as CSV format"

    def run(self, task_mgr):
        for line in task_mgr.to_csv():
            print(line)

class Swap(CommandI):
    def name(self): return "swap"
    def desc(self): return "swap the priority of two tasks"

    def run(self, task_mgr):
        try:
            tasknum1 = get_task_number()
            tasknum2 = get_task_number()
            task_mgr.swap(tasknum1, tasknum2)
        except ValueError:
            print("Couldn't swap tasks")

class Top(CommandI):
    def name(self): return "top"
    def desc(self): return "send task to top of priority"

    def run(self, task_mgr):
        try:
            tasknum1 = get_task_number()
            tasknum2 = 0
            task_mgr.swap(tasknum1, tasknum2)
        except ValueError:
            print("send task to front of queue")
            
# ------------------------------------------------------------------
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
            FinishTask(),
            ListFinishedTasks(),
            ListTag(),
            RemoveTask(), 
            RemoveTag(),
            RenameTask(),
            ReprioritizeTask(),
            Ressurect(),
            Swap(),
            Top(),
            TagTask(),
            ToCSV(),
            Quit(),
            AddDeadline(),
        ]
        for cmd in cmdlist:
            self.commands[cmd.name()] = cmd

    def run(self, txt, task_mgr):
        """
        Dispatch a text command
        """        
        txt=txt.strip()
        if txt in ["h", "?", "help"]:
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
