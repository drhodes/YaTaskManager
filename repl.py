import pickle
from pathlib import Path
from task_manager import TaskManager
import cmd 
from err import *

class REPL:
    """Read Eval Print Loop"""
    def __init__(self):
        self.tmgr = TaskManager()
        self.cmdr = cmd.Commander()
        self.history = []
        
    def loop(self):
        while 1:
            try:
                cmd = input(">> ")
                self.cmdr.run(cmd, self.tmgr)                
            except UnknownCommand as e:
                print(f"!! {e}")
        
    def writeln(self, txt):
        # maybe keep a history.
        print(txt)
    
    def intro(self):
        pass
    
