from task_manager import TaskManager
from command import Commander
from err import *
import humorous
import signal
import random
import sys


class REPL:
    """Read Eval Print Loop"""
    def __init__(self):
        self.tmgr = TaskManager()
        self.cmdr = Commander()
        self.history = []
        self.setup_signal_handlers()
        
    def setup_signal_handlers(self):
        # handle quits to ensure db is intact.
        
        def quit(*args):
            print("\n\n")
            print(random.choice(humorous.messages))
            print("todo: save state")
            print("")
            sys.exit(0)
            
        signal.signal(signal.SIGHUP, quit)
        signal.signal(signal.SIGINT, quit)
        signal.signal(signal.SIGTERM, quit)
        
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
    
