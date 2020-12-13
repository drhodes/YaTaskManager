from err import unimplemented

class StoreI:
    '''
    An interface for Store to support different data store targets, pickle, litesql
    '''
    def fetch_queue(self):
        '''When StoreI is init'd fetch all the data and instantiate the
        task_manager
        '''
        unimplemented(self)
        
    def update_one_task(self, task):
        unimplemented(self)
        
    def dump_queue(self):
        '''
        Dump the queue out to the store. 
        This operation should be atomic.
        '''
        unimplemented(self)

    
# class PickleStore(StoreI):
#     def __init__(self, task_mgr):
#         self.task_mgr = task_mgr


class SqliteStore(StoreI):
    pass


class PostgresStore(StoreI):
    pass
