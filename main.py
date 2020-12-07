import calendar
    

class TaskManager:
    """
    task manager with priority queue
    """
    pass

class Agenda:
    """
    build an agenda for a given day
    """
    pass

class REPL:
    def __init__(self):
        pass

    def go(self):
        while 1:            
            cmd = input(">> ")
            print(f"doing {cmd}")
            
def main():
    REPL().go()

if __name__ == "__main__":
    print("building agenda!")
    main()
