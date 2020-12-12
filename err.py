import inspect

class UnknownCommand(Exception): pass

class UnimplementedMethod(Exception): pass

def unimplemented(obj):
    stack = inspect.stack()
    parent_function_name = stack[2][4][0].strip()
    msg = obj.__class__.__name__ + f" needs to implement method {parent_function_name}"
    raise UnimplementedMethod(msg)

class LockfileExists(Exception): pass
