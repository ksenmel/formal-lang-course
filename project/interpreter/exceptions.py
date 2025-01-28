class InterpreterException(Exception):
    def __init__(self, msg: str):
        self.msg = msg


class VariableNotFoundException(InterpreterException):
    """
    Raises if variable is not found in the scope
    """

    def __init__(self, name: str):
        self.msg = f"Variable name '{name}' is not defined in the scope"


class RemoveGlobalScopeException(InterpreterException):
    """
    Raises when the global scope trying to be removed
    """

    def __init__(self):
        self.msg = "You can not remove the global scope"
