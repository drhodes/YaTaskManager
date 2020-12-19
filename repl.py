from task_manager import TaskManager
from command import Commander
from err import *
import humorous
import signal
import random
import sys
import datetime

class REPL:
    """Read Eval Print Loop"""
    def __init__(self):
        self.tmgr = TaskManager()
        self.cmdr = Commander()
        self.history = []
        self.setup_signal_handlers()
        
    def setup_signal_handlers(self):
        def quit(*args):
            print("\n\n")
            print(random.choice(humorous.messages))
            print("")
            sys.exit(0)
        signal.signal(signal.SIGHUP, quit)
        signal.signal(signal.SIGINT, quit)
        signal.signal(signal.SIGTERM, quit)
        
    def loop(self):
        while 1:
            try:
                now = datetime.datetime.now()
                print(now.strftime("%m/%d, %H:%M"))
                cmd = input(">> ").strip()
                if cmd == "": continue                
                self.tmgr.load_from_disk()
                self.cmdr.run(cmd, self.tmgr)
                self.tmgr.save_to_disk()
                print()
            except UnknownCommand as e:
                print(f"!! {e}")
